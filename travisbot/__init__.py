"""Travis bot package."""

import sys

from .api import api  # noqa
from .bot import Bot  # noqa
from .conf import URL, HOST, PORT, TRAVIS_CONFIG_URL  # noqa
from .web import make_app  # noqa


if sys.version_info < (3, 5):
    raise ImportError("travisbot requires Python 3.5+ because asyncio. <3")
