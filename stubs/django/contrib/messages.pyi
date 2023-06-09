# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

from typing import List

from django.http import HttpRequest

DEBUG: int = ...
INFO: int = ...
SUCCESS: int = ...
WARNING: int = ...
ERROR: int = ...

def add_message(request: HttpRequest, int, str) -> None: ...
def get_messages(request: HttpRequest) -> List[str]: ...
