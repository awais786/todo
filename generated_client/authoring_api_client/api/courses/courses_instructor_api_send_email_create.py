from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_email import SendEmail
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        SendEmail,
        SendEmail,
        SendEmail,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/send_email",
    }

    if isinstance(body, SendEmail):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, SendEmail):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, SendEmail):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[SendEmail]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SendEmail.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[SendEmail]:
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
        SendEmail,
        SendEmail,
        SendEmail,
    ],
) -> Response[SendEmail]:
    """Query Parameters:
    - 'send_to' specifies what group the email should be sent to
       Options are defined by the CourseEmail model in
       lms/djangoapps/bulk_email/models.py
    - 'subject' specifies email's subject
    - 'message' specifies email's content

    Args:
        course_id (str):
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendEmail]
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
        SendEmail,
        SendEmail,
        SendEmail,
    ],
) -> Optional[SendEmail]:
    """Query Parameters:
    - 'send_to' specifies what group the email should be sent to
       Options are defined by the CourseEmail model in
       lms/djangoapps/bulk_email/models.py
    - 'subject' specifies email's subject
    - 'message' specifies email's content

    Args:
        course_id (str):
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendEmail
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
        SendEmail,
        SendEmail,
        SendEmail,
    ],
) -> Response[SendEmail]:
    """Query Parameters:
    - 'send_to' specifies what group the email should be sent to
       Options are defined by the CourseEmail model in
       lms/djangoapps/bulk_email/models.py
    - 'subject' specifies email's subject
    - 'message' specifies email's content

    Args:
        course_id (str):
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendEmail]
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
        SendEmail,
        SendEmail,
        SendEmail,
    ],
) -> Optional[SendEmail]:
    """Query Parameters:
    - 'send_to' specifies what group the email should be sent to
       Options are defined by the CourseEmail model in
       lms/djangoapps/bulk_email/models.py
    - 'subject' specifies email's subject
    - 'message' specifies email's content

    Args:
        course_id (str):
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.
        body (SendEmail): Serializer for sending an email with optional scheduling.

            Fields:
                send_to (str): The email address of the recipient. This field is required.
                subject (str): The subject line of the email. This field is required.
                message (str): The body of the email. This field is required.
                schedule (str, optional):
                An optional field to specify when the email should be sent.
                If provided, this should be a string that can be parsed into a
                datetime format or some other scheduling logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendEmail
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
