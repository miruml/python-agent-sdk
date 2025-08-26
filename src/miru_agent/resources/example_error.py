# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.example_error_retrieve_response import ExampleErrorRetrieveResponse

__all__ = ["ExampleErrorResource", "AsyncExampleErrorResource"]


class ExampleErrorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExampleErrorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-agent-sdk#accessing-raw-response-data-eg-headers
        """
        return ExampleErrorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExampleErrorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-agent-sdk#with_streaming_response
        """
        return ExampleErrorResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExampleErrorRetrieveResponse:
        """Get an error"""
        return self._get(
            "/example-error",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExampleErrorRetrieveResponse,
        )


class AsyncExampleErrorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExampleErrorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/miruml/python-agent-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExampleErrorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExampleErrorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/miruml/python-agent-sdk#with_streaming_response
        """
        return AsyncExampleErrorResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExampleErrorRetrieveResponse:
        """Get an error"""
        return await self._get(
            "/example-error",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExampleErrorRetrieveResponse,
        )


class ExampleErrorResourceWithRawResponse:
    def __init__(self, example_error: ExampleErrorResource) -> None:
        self._example_error = example_error

        self.retrieve = to_raw_response_wrapper(
            example_error.retrieve,
        )


class AsyncExampleErrorResourceWithRawResponse:
    def __init__(self, example_error: AsyncExampleErrorResource) -> None:
        self._example_error = example_error

        self.retrieve = async_to_raw_response_wrapper(
            example_error.retrieve,
        )


class ExampleErrorResourceWithStreamingResponse:
    def __init__(self, example_error: ExampleErrorResource) -> None:
        self._example_error = example_error

        self.retrieve = to_streamed_response_wrapper(
            example_error.retrieve,
        )


class AsyncExampleErrorResourceWithStreamingResponse:
    def __init__(self, example_error: AsyncExampleErrorResource) -> None:
        self._example_error = example_error

        self.retrieve = async_to_streamed_response_wrapper(
            example_error.retrieve,
        )
