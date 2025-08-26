# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .hash import (
    HashResource,
    AsyncHashResource,
    HashResourceWithRawResponse,
    AsyncHashResourceWithRawResponse,
    HashResourceWithStreamingResponse,
    AsyncHashResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConfigSchemasResource", "AsyncConfigSchemasResource"]


class ConfigSchemasResource(SyncAPIResource):
    @cached_property
    def hash(self) -> HashResource:
        return HashResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#accessing-raw-response-data-eg-headers
        """
        return ConfigSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#with_streaming_response
        """
        return ConfigSchemasResourceWithStreamingResponse(self)


class AsyncConfigSchemasResource(AsyncAPIResource):
    @cached_property
    def hash(self) -> AsyncHashResource:
        return AsyncHashResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-agent-python#with_streaming_response
        """
        return AsyncConfigSchemasResourceWithStreamingResponse(self)


class ConfigSchemasResourceWithRawResponse:
    def __init__(self, config_schemas: ConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

    @cached_property
    def hash(self) -> HashResourceWithRawResponse:
        return HashResourceWithRawResponse(self._config_schemas.hash)


class AsyncConfigSchemasResourceWithRawResponse:
    def __init__(self, config_schemas: AsyncConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

    @cached_property
    def hash(self) -> AsyncHashResourceWithRawResponse:
        return AsyncHashResourceWithRawResponse(self._config_schemas.hash)


class ConfigSchemasResourceWithStreamingResponse:
    def __init__(self, config_schemas: ConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

    @cached_property
    def hash(self) -> HashResourceWithStreamingResponse:
        return HashResourceWithStreamingResponse(self._config_schemas.hash)


class AsyncConfigSchemasResourceWithStreamingResponse:
    def __init__(self, config_schemas: AsyncConfigSchemasResource) -> None:
        self._config_schemas = config_schemas

    @cached_property
    def hash(self) -> AsyncHashResourceWithStreamingResponse:
        return AsyncHashResourceWithStreamingResponse(self._config_schemas.hash)
