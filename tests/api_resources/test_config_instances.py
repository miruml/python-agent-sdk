# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from miru_agent import MiruAgent, AsyncMiruAgent
from tests.utils import assert_matches_type
from miru_agent.types import ConfigInstanceRetrieveLatestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_latest(self, client: MiruAgent) -> None:
        config_instance = client.config_instances.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        )
        assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_latest(self, client: MiruAgent) -> None:
        response = client.config_instances.with_raw_response.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = response.parse()
        assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_latest(self, client: MiruAgent) -> None:
        with client.config_instances.with_streaming_response.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = response.parse()
            assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_latest(self, async_client: AsyncMiruAgent) -> None:
        config_instance = await async_client.config_instances.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        )
        assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_latest(self, async_client: AsyncMiruAgent) -> None:
        response = await async_client.config_instances.with_raw_response.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config_instance = await response.parse()
        assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_latest(self, async_client: AsyncMiruAgent) -> None:
        async with async_client.config_instances.with_streaming_response.retrieve_latest(
            config_schema_digest="sha256:1234567890abcdef",
            config_type_slug="config_type_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config_instance = await response.parse()
            assert_matches_type(ConfigInstanceRetrieveLatestResponse, config_instance, path=["response"])

        assert cast(Any, response.is_closed) is True
