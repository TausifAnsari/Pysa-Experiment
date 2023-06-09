# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

LANGUAGE_SESSION_KEY: str = ...

def activate(language: str) -> None: ...
def deactivate() -> None: ...
def gettext(message: str) -> str: ...
def gettext_lazy(*args, **kwargs) -> str: ...
def gettext_noop(message: str) -> str: ...
def ngettext_lazy(singular, plural, number=...): ...
def ugettext(message: str) -> str: ...
def ugettext_lazy(*args, **kwargs) -> str: ...
def ugettext_noop(message: str) -> str: ...
def ungettext_lazy(singular, plural, number=...): ...
