from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access import Access
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        Access,
        Access,
        Access,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {
        "Content-Type": "application/json"
    }

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/modify_access",
    }

    if isinstance(body, Access):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, Access):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Access]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Access.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Access]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Access,
        Access,
        Access,
    ],
) -> Response[Access]:
    """Modify staff/instructor access of other user.
    Requires instructor access.

    Args:
        course_id (str):
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Access]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
    )
    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Access,
        Access,
        Access,
    ],
) -> Optional[Access]:
    """Modify staff/instructor access of other user.
    Requires instructor access.

    Args:
        course_id (str):
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Access
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Access,
        Access,
        Access,
    ],
) -> Response[Access]:
    """Modify staff/instructor access of other user.
    Requires instructor access.

    Args:
        course_id (str):
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Access]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Access,
        Access,
        Access,
    ],
) -> Optional[Access]:
    """Modify staff/instructor access of other user.
    Requires instructor access.

    Args:
        course_id (str):
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.
        body (Access): Serializer for managing user access changes.
            This serializer validates and processes the data required to modify
            user access within a system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Access
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
