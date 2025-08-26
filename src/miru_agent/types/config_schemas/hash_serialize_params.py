# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["HashSerializeParams"]


class HashSerializeParams(TypedDict, total=False):
    format: Required[Literal["json", "yaml"]]

    schema: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
