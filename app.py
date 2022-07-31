"""Run."""
# pylint: disable=invalid-name
from random import choice
import gradio as gr

from convbot import convbot

lost_msg = [
    "I don't follow.",
    "Say it agan?",
    "Come again?",
    "I am afraid I dont't understand.",
    "I am lost.",
]


def bot(message: str) -> str:
    try:
        res = convbot(message)
    except Exception as exc:
        res = f"{choice(lost_msg)} (reason: {exc})"
    return res


iface = gr.Interface(fn=bot, inputs="text", outputs="text")
iface.launch()
