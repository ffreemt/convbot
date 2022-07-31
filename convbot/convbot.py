"""Generate a response."""
# pylint:disable=line-too-long, too-many-argument
import torch
from logzero import logger
from transformers import AutoModelForCausalLM, AutoTokenizer

from .force_async import force_async

# model_name = "microsoft/DialoGPT-large"
# model_name = "microsoft/DialoGPT-small"
# pylint: disable=invalid-name
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def _convbot(
    text: str,
    max_length: int = 1000,
    do_sample: bool = True,
    top_p: float = 0.95,
    top_k: int = 0,
    temperature: float = 0.75,
) -> str:
    """Generate a reponse.

    Args
        n_retires: retry if response is  "" or the same as previouse resp.

    Returns
        reply
    """
    try:
        chat_history_ids = _convbot.chat_history_ids
    except AttributeError:
        chat_history_ids = ""

    try:
        chat_history_ids = _convbot.chat_history_ids
    except AttributeError:
        chat_history_ids = ""

    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    if isinstance(chat_history_ids, torch.Tensor):
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
    else:
        bot_input_ids = input_ids

    # generate a bot response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=max_length,
        do_sample=do_sample,
        top_p=top_p,
        top_k=top_k,
        temperature=temperature,
        pad_token_id=tokenizer.eos_token_id,
    )

    output = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
    )
    _convbot.chat_history_ids = chat_history_ids

    return output


def convbot(
    text: str,
    n_retries: int = 3,
    max_length: int = 1000,
    do_sample: bool = True,
    top_p: float = 0.95,
    top_k: int = 0,
    temperature: float = 0.75,
) -> str:
    """Generate a response."""
    try:
        n_retries = int(n_retries)
    except Exception as e:
        logger.error(e)
        raise
    try:
        prev_resp = convbot.prev_resp
    except AttributeError:
        prev_resp = ""

    resp = _convbot(text, max_length, do_sample, top_p, top_k, temperature)

    # retry n_retries if resp is empty
    if not resp.strip():
        idx = 0
        while idx < n_retries:
            idx += 1
            _convbot.chat_history_ids = ""
            resp = _convbot(text, max_length, do_sample, top_p, top_k, temperature)
            if resp.strip():
                break
        else:
            logger.warning("bot acting up (empty response), something has gone awry")

    # check repeated responses
    if resp.strip() == prev_resp:
        idx = 0
        while idx < n_retries:
            idx += 1
            resp = _convbot(text, max_length, do_sample, top_p, top_k, temperature)
            if resp.strip() != prev_resp:
                break
        else:
            logger.warning("bot acting up (repeating), something has gone awry")

    convbot.prev_resp = resp

    return resp


@force_async
def aconvbot(
    text: str,
    n_retries: int = 3,
    max_length: int = 1000,
    do_sample: bool = True,
    top_p: float = 0.95,
    top_k: int = 0,
    temperature: float = 0.75,
) -> str:
    try:
        _ = convbot(text, n_retries, max_length, do_sample, top_p, top_k, temperature)
    except Exception as e:
        logger.error(e)
        raise
    return _


def main():
    print("Bot: Talk to me")
    while 1:
        text = input("You: ")
        resp = _convbot(text)
        print("Bot: ", resp)


if __name__ == "__main__":
    main()
