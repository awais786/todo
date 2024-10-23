from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/register_and_enroll_students",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
    """Create new account and Enroll students in this course.
    Passing a csv file that contains a list of students.
    Order in csv should be the following email = 0; username = 1; name = 2; country = 3.
    If there are more than 4 columns in the csv: cohort = 4, course mode = 5.
    Requires staff access.

    -If the email address and username already exists and the user is enrolled in the course,
    do nothing (including no email gets sent out)

    -If the email address already exists, but the username is different,
    match on the email address only and continue to enroll the user in the course using the email
    address
    as the matching criteria. Note the change of username as a warning message (but not a failure).
    Send a standard enrollment email which is the same as the existing manual enrollment

    -If the username already exists (but not the email), assume it is a different user and fail
    to create the new account.
    The failure will be messaged in a response in the browser.

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Create new account and Enroll students in this course.
    Passing a csv file that contains a list of students.
    Order in csv should be the following email = 0; username = 1; name = 2; country = 3.
    If there are more than 4 columns in the csv: cohort = 4, course mode = 5.
    Requires staff access.

    -If the email address and username already exists and the user is enrolled in the course,
    do nothing (including no email gets sent out)

    -If the email address already exists, but the username is different,
    match on the email address only and continue to enroll the user in the course using the email
    address
    as the matching criteria. Note the change of username as a warning message (but not a failure).
    Send a standard enrollment email which is the same as the existing manual enrollment

    -If the username already exists (but not the email), assume it is a different user and fail
    to create the new account.
    The failure will be messaged in a response in the browser.

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
