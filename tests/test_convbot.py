"""Test convbot."""
# import asyncio
import pytest

from convbot import __version__
from convbot import convbot, aconvbot

pytestmark = pytest.mark.asyncio


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Sanity check."""
    try:
        assert not convbot("")
    except Exception:
        assert True


def test_convbot():
    """Test convbot."""
    resp = convbot("How are you?")
    assert len(resp) > 3

    # 2nd call uses chat_history_ids
    resp = convbot("How old are you?")
    assert len(resp) > 3


async def tests_aconvbot():
    """Test aconvbot."""
    resp = await aconvbot("How are you?")
    assert len(resp) > 3

    # 2nd call uses chat_history_ids
    resp = await aconvbot("How old are you?")
    assert len(resp) > 3
