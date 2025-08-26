# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["DeviceSyncResponse"]


class DeviceSyncResponse(BaseModel):
    code: str
    """The code of the result."""

    last_synced_at: datetime
    """Timestamp of when the device was last synced"""

    message: str
    """The message of the result."""

    success: bool
    """Whether the device was successfully synced.

    If false, the device was not able to be synced.
    """
