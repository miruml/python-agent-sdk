# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from miru_agent import MiruAgent, AsyncMiruAgent
from tests.utils import assert_matches_type
from miru_agent.types.config_schemas import HashSerializeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHash:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_serialize(self, client: MiruAgent) -> None:
        hash = client.config_schemas.hash.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        )
        assert_matches_type(HashSerializeResponse, hash, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_serialize(self, client: MiruAgent) -> None:
        response = client.config_schemas.hash.with_raw_response.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hash = response.parse()
        assert_matches_type(HashSerializeResponse, hash, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_serialize(self, client: MiruAgent) -> None:
        with client.config_schemas.hash.with_streaming_response.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hash = response.parse()
            assert_matches_type(HashSerializeResponse, hash, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHash:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_serialize(self, async_client: AsyncMiruAgent) -> None:
        hash = await async_client.config_schemas.hash.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        )
        assert_matches_type(HashSerializeResponse, hash, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_serialize(self, async_client: AsyncMiruAgent) -> None:
        response = await async_client.config_schemas.hash.with_raw_response.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hash = await response.parse()
        assert_matches_type(HashSerializeResponse, hash, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_serialize(self, async_client: AsyncMiruAgent) -> None:
        async with async_client.config_schemas.hash.with_streaming_response.serialize(
            format="json",
            schema="ewogICIkc2NoZW1hIjogImh0dHBzOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LzIwMjAtMTIvc2NoZW1hIiwKICAidHlwZSI6ICJvYmplY3QiLAogICJwcm9wZXJ0aWVzIjogewogICAgImRldmljZV9pZCI6IHsKICAgICAgInR5cGUiOiAic3RyaW5nIgogICAgfSwKICAgICJzcGVlZCI6IHsKICAgICAgInR5cGUiOiAiaW50ZWdlciIsCiAgICAgICJtaW5pbXVtIjogMSwKICAgICAgImRlZmF1bHQiOiAxMAogICAgfQogIH0sCiAgInJlcXVpcmVkIjogWyJkZXZpY2VfaWQiLCAic3BlZWQiXQp9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hash = await response.parse()
            assert_matches_type(HashSerializeResponse, hash, path=["response"])

        assert cast(Any, response.is_closed) is True
