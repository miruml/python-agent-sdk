# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ExampleErrorRetrieveResponse", "Error"]


class Error(BaseModel):
    code: str

    debug_message: str

    message: str

    params: object


class ExampleErrorRetrieveResponse(BaseModel):
    error: Error
