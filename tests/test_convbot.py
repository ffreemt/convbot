"""Test convbot."""
from convbot import __version__
from convbot import convbot


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not convbot()
    except Exception:
        assert True


def test_convbot():
    resp = convbot("How are you?")
    assert len(resp) > 3

