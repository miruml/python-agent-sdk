# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import config_instance_retrieve_latest_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.config_instance_retrieve_latest_response import ConfigInstanceRetrieveLatestResponse

__all__ = ["ConfigInstancesResource", "AsyncConfigInstancesResource"]


class ConfigInstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#accessing-raw-response-data-eg-headers
        """
        return ConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#with_streaming_response
        """
        return ConfigInstancesResourceWithStreamingResponse(self)

    def retrieve_latest(
        self,
        *,
        config_schema_digest: str,
        config_type_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceRetrieveLatestResponse:
        """
        Get the latest config instance

        Args:
          config_schema_digest: The digest of the config schema

          config_type_slug: The slug of the config type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config_instances/deployed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "config_schema_digest": config_schema_digest,
                        "config_type_slug": config_type_slug,
                    },
                    config_instance_retrieve_latest_params.ConfigInstanceRetrieveLatestParams,
                ),
            ),
            cast_to=ConfigInstanceRetrieveLatestResponse,
        )


class AsyncConfigInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#with_streaming_response
        """
        return AsyncConfigInstancesResourceWithStreamingResponse(self)

    async def retrieve_latest(
        self,
        *,
        config_schema_digest: str,
        config_type_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigInstanceRetrieveLatestResponse:
        """
        Get the latest config instance

        Args:
          config_schema_digest: The digest of the config schema

          config_type_slug: The slug of the config type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config_instances/deployed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "config_schema_digest": config_schema_digest,
                        "config_type_slug": config_type_slug,
                    },
                    config_instance_retrieve_latest_params.ConfigInstanceRetrieveLatestParams,
                ),
            ),
            cast_to=ConfigInstanceRetrieveLatestResponse,
        )


class ConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve_latest = to_raw_response_wrapper(
            config_instances.retrieve_latest,
        )


class AsyncConfigInstancesResourceWithRawResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve_latest = async_to_raw_response_wrapper(
            config_instances.retrieve_latest,
        )


class ConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: ConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve_latest = to_streamed_response_wrapper(
            config_instances.retrieve_latest,
        )


class AsyncConfigInstancesResourceWithStreamingResponse:
    def __init__(self, config_instances: AsyncConfigInstancesResource) -> None:
        self._config_instances = config_instances

        self.retrieve_latest = async_to_streamed_response_wrapper(
            config_instances.retrieve_latest,
        )
