"""Run main.

python -m convbot
"""
from convbot import convbot


def main():
    print("Bot: Talk to me (type quit to exit)")
    while 1:
        text = input("You: ")

        if text.lower().strip() in ["quit", "exit", "stop"]:
            break

        resp = convbot(text)
        print("Bot: ", resp)


if __name__ == "__main__":
    main()
