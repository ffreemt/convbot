# convbot
[![tests](https://github.com/ffreemt/convbot/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/convbot/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/convbot.svg)](https://badge.fury.io/py/convbot)

A conversational bot based on huggingface transformers

## Install it

```shell
pip install convbot
# or poetry add convbot
# pip install git+htts://github.com/ffreemt/convbot
# poetry add git+htts://github.com/ffreemt/convbot

# To upgrade
pip install convbot -U
# or poetry add convbot@latest
```

## Use it
```python
from convbot import convbot

prin(convertbot("How are you?"))
# I am good  # or along that line
```

The async version `aconvbot`, potentialy for `fastapi` or `Nonebot` plugins and such,  is rather artificial since it's based on `ThreadPoolExecutor`. Hence it's not intended for production. You probably should not spawn too many instances.
```python
from convbot import aconvbot

async def afunc(text):
    resp = await aconvbot(text)
    ...
```

Interactive

```bash
python -m convbot
```
## Not tested in Windows 10 and Mac

The module uses pytorch that is installed differently in Windows than in Linux. To run `convbot` in Windows or Mac, you may give it a spin  by cloning the repo (git clone [https://github.com/ffreemt/convbot](https://github.com/ffreemt/convbot)) and installing pytorch manually.
