import enum
import pytest


@enum.unique
class Color(enum.Enum):
    ERROR = '\033[91m'
    WARNING = '\033[93m'
    INFO = '\033[95m'


def fail(message: str, is_exist: bool = True):
    pytest.fail(f"{Color.ERROR.value} {message}")
    if is_exist:
        pytest.exit()


