from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_instructor_task_input import ListInstructorTaskInput
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        ListInstructorTaskInput,
        ListInstructorTaskInput,
        ListInstructorTaskInput,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/list_instructor_tasks",
    }

    if isinstance(body, ListInstructorTaskInput):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ListInstructorTaskInput):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ListInstructorTaskInput):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListInstructorTaskInput]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListInstructorTaskInput.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListInstructorTaskInput]:
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
        ListInstructorTaskInput,
        ListInstructorTaskInput,
        ListInstructorTaskInput,
    ],
) -> Response[ListInstructorTaskInput]:
    """List instructor tasks.

    Args:
        course_id (str):
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInstructorTaskInput]
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
        ListInstructorTaskInput,
        ListInstructorTaskInput,
        ListInstructorTaskInput,
    ],
) -> Optional[ListInstructorTaskInput]:
    """List instructor tasks.

    Args:
        course_id (str):
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInstructorTaskInput
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
        ListInstructorTaskInput,
        ListInstructorTaskInput,
        ListInstructorTaskInput,
    ],
) -> Response[ListInstructorTaskInput]:
    """List instructor tasks.

    Args:
        course_id (str):
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInstructorTaskInput]
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
        ListInstructorTaskInput,
        ListInstructorTaskInput,
        ListInstructorTaskInput,
    ],
) -> Optional[ListInstructorTaskInput]:
    """List instructor tasks.

    Args:
        course_id (str):
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.
        body (ListInstructorTaskInput): Serializer for handling the input data for the problem
            response report generation API.

            Attributes:
                unique_student_identifier (str): The email or username of the student.
                                                  This field is optional, but if provided, the
            `problem_location_str`
                                                  must also be provided.
                problem_location_str (str): The string representing the location of the problem within
            the course.
                                            This field is optional, unless `unique_student_identifier`
            is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInstructorTaskInput
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
