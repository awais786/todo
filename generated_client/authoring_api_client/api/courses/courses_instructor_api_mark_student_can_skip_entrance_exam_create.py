from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unique_student_identifier import UniqueStudentIdentifier
from ...types import Response


def _get_kwargs(
        course_id: str,
        *,
        body: Union[
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
        ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/mark_student_can_skip_entrance_exam",
    }

    if isinstance(body, UniqueStudentIdentifier):
        _json_body = body.to_dict()
        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    if isinstance(body, UniqueStudentIdentifier):
        _data_body = body.to_dict()
        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
        *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UniqueStudentIdentifier]:
    response_data = response.json()
    return response_data


def _build_response(
        *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UniqueStudentIdentifier]:
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
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
        ],
) -> Response[UniqueStudentIdentifier]:
    """Takes `unique_student_identifier` as required POST parameter.

    Args:
        course_id (str):
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniqueStudentIdentifier]
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
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
        ],
) -> Optional[UniqueStudentIdentifier]:
    """Takes `unique_student_identifier` as required POST parameter.

    Args:
        course_id (str):
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniqueStudentIdentifier
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
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
        ],
) -> Response[UniqueStudentIdentifier]:
    """Takes `unique_student_identifier` as required POST parameter.

    Args:
        course_id (str):
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniqueStudentIdentifier]
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
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
            UniqueStudentIdentifier,
        ],
) -> Optional[UniqueStudentIdentifier]:
    """Takes `unique_student_identifier` as required POST parameter.

    Args:
        course_id (str):
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.
        body (unique_student_identifier): Serializer for identifying unique_student.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniqueStudentIdentifier
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
