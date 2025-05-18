# SPDX-FileCopyrightText: 2025-present louanbel <louanbelicaud63@gmail.com>
#
# SPDX-License-Identifier: MIT
from ._client import ReSMS, SendResult, ReSMSError
from importlib.metadata import PackageNotFoundError, version

__all__ = ["ReSMS", "SendResult", "ReSMSError"]

# enable type checkers for downstream users
try:
    __version__ = version(__name__)
except PackageNotFoundError:  # package not installed
    __version__ = "0.0.0"