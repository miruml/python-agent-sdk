# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigInstanceRetrieveLatestParams"]


class ConfigInstanceRetrieveLatestParams(TypedDict, total=False):
    config_schema_digest: Required[str]
    """The digest of the config schema"""

    config_type_slug: Required[str]
    """The slug of the config type"""
