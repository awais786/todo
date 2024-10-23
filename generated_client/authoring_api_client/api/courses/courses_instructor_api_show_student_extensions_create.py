from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.show_student_extension import ShowStudentExtension
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        ShowStudentExtension,
        ShowStudentExtension,
        ShowStudentExtension,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/show_student_extensions",
    }

    if isinstance(body, ShowStudentExtension):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ShowStudentExtension):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ShowStudentExtension):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ShowStudentExtension]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ShowStudentExtension.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ShowStudentExtension]:
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
        ShowStudentExtension,
        ShowStudentExtension,
        ShowStudentExtension,
    ],
) -> Response[ShowStudentExtension]:
    """Handles POST requests to retrieve due date extensions for a specific student
    within a specified course.

    Parameters:
    - `request`: The HTTP request object containing user-submitted data.
    - `course_id`: The ID of the course for which the extensions are being queried.

    Data expected in the request:
    - `student`: A required field containing the identifier of the student for whom
      the due date extensions are being retrieved. This data is extracted from the
      request body.

    Returns:
    - A JSON response containing the details of the due date extensions granted to
      the specified student in the specified course.

    Args:
        course_id (str):
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShowStudentExtension]
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
        ShowStudentExtension,
        ShowStudentExtension,
        ShowStudentExtension,
    ],
) -> Optional[ShowStudentExtension]:
    """Handles POST requests to retrieve due date extensions for a specific student
    within a specified course.

    Parameters:
    - `request`: The HTTP request object containing user-submitted data.
    - `course_id`: The ID of the course for which the extensions are being queried.

    Data expected in the request:
    - `student`: A required field containing the identifier of the student for whom
      the due date extensions are being retrieved. This data is extracted from the
      request body.

    Returns:
    - A JSON response containing the details of the due date extensions granted to
      the specified student in the specified course.

    Args:
        course_id (str):
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShowStudentExtension
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
        ShowStudentExtension,
        ShowStudentExtension,
        ShowStudentExtension,
    ],
) -> Response[ShowStudentExtension]:
    """Handles POST requests to retrieve due date extensions for a specific student
    within a specified course.

    Parameters:
    - `request`: The HTTP request object containing user-submitted data.
    - `course_id`: The ID of the course for which the extensions are being queried.

    Data expected in the request:
    - `student`: A required field containing the identifier of the student for whom
      the due date extensions are being retrieved. This data is extracted from the
      request body.

    Returns:
    - A JSON response containing the details of the due date extensions granted to
      the specified student in the specified course.

    Args:
        course_id (str):
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShowStudentExtension]
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
        ShowStudentExtension,
        ShowStudentExtension,
        ShowStudentExtension,
    ],
) -> Optional[ShowStudentExtension]:
    """Handles POST requests to retrieve due date extensions for a specific student
    within a specified course.

    Parameters:
    - `request`: The HTTP request object containing user-submitted data.
    - `course_id`: The ID of the course for which the extensions are being queried.

    Data expected in the request:
    - `student`: A required field containing the identifier of the student for whom
      the due date extensions are being retrieved. This data is extracted from the
      request body.

    Returns:
    - A JSON response containing the details of the due date extensions granted to
      the specified student in the specified course.

    Args:
        course_id (str):
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.
        body (ShowStudentExtension): Serializer for validating and processing the student
            identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShowStudentExtension
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
