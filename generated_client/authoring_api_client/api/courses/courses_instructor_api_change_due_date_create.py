from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_due_date import BlockDueDate
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        BlockDueDate,
        BlockDueDate,
        BlockDueDate,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/change_due_date",
    }

    if isinstance(body, BlockDueDate):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, BlockDueDate):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BlockDueDate):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BlockDueDate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BlockDueDate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BlockDueDate]:
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
        BlockDueDate,
        BlockDueDate,
        BlockDueDate,
    ],
) -> Response[BlockDueDate]:
    """Grants a due date extension to a student for a particular unit.

    params:
        url (str): The URL related to the block that needs the due date update.
        due_datetime (str): The new due date and time for the block.
        student (str): The email or username of the student whose access is being modified.

    Args:
        course_id (str):
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockDueDate]
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
        BlockDueDate,
        BlockDueDate,
        BlockDueDate,
    ],
) -> Optional[BlockDueDate]:
    """Grants a due date extension to a student for a particular unit.

    params:
        url (str): The URL related to the block that needs the due date update.
        due_datetime (str): The new due date and time for the block.
        student (str): The email or username of the student whose access is being modified.

    Args:
        course_id (str):
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockDueDate
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
        BlockDueDate,
        BlockDueDate,
        BlockDueDate,
    ],
) -> Response[BlockDueDate]:
    """Grants a due date extension to a student for a particular unit.

    params:
        url (str): The URL related to the block that needs the due date update.
        due_datetime (str): The new due date and time for the block.
        student (str): The email or username of the student whose access is being modified.

    Args:
        course_id (str):
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockDueDate]
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
        BlockDueDate,
        BlockDueDate,
        BlockDueDate,
    ],
) -> Optional[BlockDueDate]:
    """Grants a due date extension to a student for a particular unit.

    params:
        url (str): The URL related to the block that needs the due date update.
        due_datetime (str): The new due date and time for the block.
        student (str): The email or username of the student whose access is being modified.

    Args:
        course_id (str):
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.
        body (BlockDueDate): Serializer for handling block due date updates for a specific
            student.
            Fields:
                url (str): The URL related to the block that needs the due date update.
                due_datetime (str): The new due date and time for the block.
                student (str): The email or username of the student whose access is being modified.
                reason (str): Reason why updating this.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockDueDate
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
