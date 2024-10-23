from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.student_attempts import StudentAttempts
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        StudentAttempts,
        StudentAttempts,
        StudentAttempts,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/reset_student_attempts",
    }

    if isinstance(body, StudentAttempts):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, StudentAttempts):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, StudentAttempts):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StudentAttempts]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StudentAttempts.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StudentAttempts]:
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
        StudentAttempts,
        StudentAttempts,
        StudentAttempts,
    ],
) -> Response[StudentAttempts]:
    """Takes some of the following query parameters
    - problem_to_reset is a urlname of a problem
    - unique_student_identifier is an email or username
    - all_students is a boolean
        requires instructor access
        mutually exclusive with delete_module
        mutually exclusive with delete_module
    - delete_module is a boolean
        requires instructor access
        mutually exclusive with all_students

    Args:
        course_id (str):
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudentAttempts]
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
        StudentAttempts,
        StudentAttempts,
        StudentAttempts,
    ],
) -> Optional[StudentAttempts]:
    """Takes some of the following query parameters
    - problem_to_reset is a urlname of a problem
    - unique_student_identifier is an email or username
    - all_students is a boolean
        requires instructor access
        mutually exclusive with delete_module
        mutually exclusive with delete_module
    - delete_module is a boolean
        requires instructor access
        mutually exclusive with all_students

    Args:
        course_id (str):
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudentAttempts
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
        StudentAttempts,
        StudentAttempts,
        StudentAttempts,
    ],
) -> Response[StudentAttempts]:
    """Takes some of the following query parameters
    - problem_to_reset is a urlname of a problem
    - unique_student_identifier is an email or username
    - all_students is a boolean
        requires instructor access
        mutually exclusive with delete_module
        mutually exclusive with delete_module
    - delete_module is a boolean
        requires instructor access
        mutually exclusive with all_students

    Args:
        course_id (str):
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudentAttempts]
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
        StudentAttempts,
        StudentAttempts,
        StudentAttempts,
    ],
) -> Optional[StudentAttempts]:
    """Takes some of the following query parameters
    - problem_to_reset is a urlname of a problem
    - unique_student_identifier is an email or username
    - all_students is a boolean
        requires instructor access
        mutually exclusive with delete_module
        mutually exclusive with delete_module
    - delete_module is a boolean
        requires instructor access
        mutually exclusive with all_students

    Args:
        course_id (str):
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.
        body (StudentAttempts): Serializer for resetting a students attempts counter or starts a
            task to reset all students
            attempts counters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudentAttempts
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
