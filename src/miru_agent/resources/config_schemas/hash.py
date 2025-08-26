# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, Base64FileInput
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.config_schemas import hash_serialize_params
from ...types.config_schemas.hash_serialize_response import HashSerializeResponse

__all__ = ["HashResource", "AsyncHashResource"]


class HashResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HashResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-agent-sdk#accessing-raw-response-data-eg-headers
        """
        return HashResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HashResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-agent-sdk#with_streaming_response
        """
        return HashResourceWithStreamingResponse(self)

    def serialize(
        self,
        *,
        format: Literal["json", "yaml"],
        schema: Union[str, Base64FileInput],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HashSerializeResponse:
        """
        Hash a serialized config schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config_schemas/hash/serialized",
            body=maybe_transform(
                {
                    "format": format,
                    "schema": schema,
                },
                hash_serialize_params.HashSerializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HashSerializeResponse,
        )


class AsyncHashResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHashResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-agent-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHashResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHashResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-agent-sdk#with_streaming_response
        """
        return AsyncHashResourceWithStreamingResponse(self)

    async def serialize(
        self,
        *,
        format: Literal["json", "yaml"],
        schema: Union[str, Base64FileInput],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HashSerializeResponse:
        """
        Hash a serialized config schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config_schemas/hash/serialized",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "schema": schema,
                },
                hash_serialize_params.HashSerializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HashSerializeResponse,
        )


class HashResourceWithRawResponse:
    def __init__(self, hash: HashResource) -> None:
        self._hash = hash

        self.serialize = to_raw_response_wrapper(
            hash.serialize,
        )


class AsyncHashResourceWithRawResponse:
    def __init__(self, hash: AsyncHashResource) -> None:
        self._hash = hash

        self.serialize = async_to_raw_response_wrapper(
            hash.serialize,
        )


class HashResourceWithStreamingResponse:
    def __init__(self, hash: HashResource) -> None:
        self._hash = hash

        self.serialize = to_streamed_response_wrapper(
            hash.serialize,
        )


class AsyncHashResourceWithStreamingResponse:
    def __init__(self, hash: AsyncHashResource) -> None:
        self._hash = hash

        self.serialize = async_to_streamed_response_wrapper(
            hash.serialize,
        )
