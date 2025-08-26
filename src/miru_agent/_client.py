# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import device, health, version, example_error, config_instances
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MiruAgentError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.version import VersionResource, AsyncVersionResource
from .resources.config_schemas import config_schemas

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "MiruAgent",
    "AsyncMiruAgent",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://configs.dev.api.miruml.com/{audience}/{version}",
    "environment_1": "https://configs.api.miruml.com/{audience}/{version}",
}


class MiruAgent(SyncAPIClient):
    health: health.HealthResource
    version: version.VersionResource
    config_instances: config_instances.ConfigInstancesResource
    config_schemas: config_schemas.ConfigSchemasResource
    device: device.DeviceResource
    example_error: example_error.ExampleErrorResource
    with_raw_response: MiruAgentWithRawResponse
    with_streaming_response: MiruAgentWithStreamedResponse

    # client options
    api_key: str
    audience: str
    version: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        audience: str | None = None,
        version: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous MiruAgent client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MIRU_AGENT_API_KEY`
        - `audience` from `MIRU_AGENT_AUDIENCE`
        - `version` from `MIRU_AGENT_VERSION`
        """
        if api_key is None:
            api_key = os.environ.get("MIRU_AGENT_API_KEY")
        if api_key is None:
            raise MiruAgentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MIRU_AGENT_API_KEY environment variable"
            )
        self.api_key = api_key

        if audience is None:
            audience = os.environ.get("MIRU_AGENT_AUDIENCE") or "agent"
        self.audience = audience

        if version is None:
            version = os.environ.get("MIRU_AGENT_VERSION") or "v1"
        self.version = version

        self._environment = environment

        base_url_env = os.environ.get("MIRU_AGENT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIRU_AGENT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health = health.HealthResource(self)
        self.version = VersionResource(self)
        self.config_instances = config_instances.ConfigInstancesResource(self)
        self.config_schemas = config_schemas.ConfigSchemasResource(self)
        self.device = device.DeviceResource(self)
        self.example_error = example_error.ExampleErrorResource(self)
        self.with_raw_response = MiruAgentWithRawResponse(self)
        self.with_streaming_response = MiruAgentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        audience: str | None = None,
        version: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            audience=audience or self.audience,
            version=version or self.version,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMiruAgent(AsyncAPIClient):
    health: health.AsyncHealthResource
    version: version.AsyncVersionResource
    config_instances: config_instances.AsyncConfigInstancesResource
    config_schemas: config_schemas.AsyncConfigSchemasResource
    device: device.AsyncDeviceResource
    example_error: example_error.AsyncExampleErrorResource
    with_raw_response: AsyncMiruAgentWithRawResponse
    with_streaming_response: AsyncMiruAgentWithStreamedResponse

    # client options
    api_key: str
    audience: str
    version: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        audience: str | None = None,
        version: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMiruAgent client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MIRU_AGENT_API_KEY`
        - `audience` from `MIRU_AGENT_AUDIENCE`
        - `version` from `MIRU_AGENT_VERSION`
        """
        if api_key is None:
            api_key = os.environ.get("MIRU_AGENT_API_KEY")
        if api_key is None:
            raise MiruAgentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MIRU_AGENT_API_KEY environment variable"
            )
        self.api_key = api_key

        if audience is None:
            audience = os.environ.get("MIRU_AGENT_AUDIENCE") or "agent"
        self.audience = audience

        if version is None:
            version = os.environ.get("MIRU_AGENT_VERSION") or "v1"
        self.version = version

        self._environment = environment

        base_url_env = os.environ.get("MIRU_AGENT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIRU_AGENT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health = health.AsyncHealthResource(self)
        self.version = AsyncVersionResource(self)
        self.config_instances = config_instances.AsyncConfigInstancesResource(self)
        self.config_schemas = config_schemas.AsyncConfigSchemasResource(self)
        self.device = device.AsyncDeviceResource(self)
        self.example_error = example_error.AsyncExampleErrorResource(self)
        self.with_raw_response = AsyncMiruAgentWithRawResponse(self)
        self.with_streaming_response = AsyncMiruAgentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        audience: str | None = None,
        version: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            audience=audience or self.audience,
            version=version or self.version,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MiruAgentWithRawResponse:
    def __init__(self, client: MiruAgent) -> None:
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.version = version.VersionResourceWithRawResponse(client.version)
        self.config_instances = config_instances.ConfigInstancesResourceWithRawResponse(client.config_instances)
        self.config_schemas = config_schemas.ConfigSchemasResourceWithRawResponse(client.config_schemas)
        self.device = device.DeviceResourceWithRawResponse(client.device)
        self.example_error = example_error.ExampleErrorResourceWithRawResponse(client.example_error)


class AsyncMiruAgentWithRawResponse:
    def __init__(self, client: AsyncMiruAgent) -> None:
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.version = version.AsyncVersionResourceWithRawResponse(client.version)
        self.config_instances = config_instances.AsyncConfigInstancesResourceWithRawResponse(client.config_instances)
        self.config_schemas = config_schemas.AsyncConfigSchemasResourceWithRawResponse(client.config_schemas)
        self.device = device.AsyncDeviceResourceWithRawResponse(client.device)
        self.example_error = example_error.AsyncExampleErrorResourceWithRawResponse(client.example_error)


class MiruAgentWithStreamedResponse:
    def __init__(self, client: MiruAgent) -> None:
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.version = version.VersionResourceWithStreamingResponse(client.version)
        self.config_instances = config_instances.ConfigInstancesResourceWithStreamingResponse(client.config_instances)
        self.config_schemas = config_schemas.ConfigSchemasResourceWithStreamingResponse(client.config_schemas)
        self.device = device.DeviceResourceWithStreamingResponse(client.device)
        self.example_error = example_error.ExampleErrorResourceWithStreamingResponse(client.example_error)


class AsyncMiruAgentWithStreamedResponse:
    def __init__(self, client: AsyncMiruAgent) -> None:
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.version = version.AsyncVersionResourceWithStreamingResponse(client.version)
        self.config_instances = config_instances.AsyncConfigInstancesResourceWithStreamingResponse(
            client.config_instances
        )
        self.config_schemas = config_schemas.AsyncConfigSchemasResourceWithStreamingResponse(client.config_schemas)
        self.device = device.AsyncDeviceResourceWithStreamingResponse(client.device)
        self.example_error = example_error.AsyncExampleErrorResourceWithStreamingResponse(client.example_error)


Client = MiruAgent

AsyncClient = AsyncMiruAgent
