# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InfoCheckResponse"]


class InfoCheckResponse(BaseModel):
    status: str
    """The status of the agent"""
