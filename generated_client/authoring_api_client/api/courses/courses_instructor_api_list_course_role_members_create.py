from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.role_name import RoleName
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Dict[str, Any],  # Ensure body is passed as a dictionary
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {
        "Content-Type": "application/json",
    }

    # Define the kwargs for the HTTP request
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/courses/{course_id}/instructor/api/list_course_role_members",
        "json": body,  # Ensure the body is passed as JSON (dict)
        "headers": headers,
    }

    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RoleName]:

    if response.status_code == HTTPStatus.OK:
        import json
        response_data = response.content.decode('utf-8')  # Decode bytes to string
        response_dict = json.loads(response_data)  # Convert JSON string to dict
        # Return an instance of StudentProgressUrl created from the response dictionary
        return RoleName.from_dict(response_dict)

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RoleName]:
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
    body: RoleName,
) -> Response[RoleName]:
    """Handles POST request to list instructors and staff.

    Args:
        request (HttpRequest): The request object containing user data.
        course_id (str): The ID of the course to list instructors and staff for.

    Returns:
        Response: A Response object containing the list of instructors and staff or an error message.

    Raises:
        Http404: If the course does not exist.

    Args:
        course_id (str):
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoleName]
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
        RoleName,
    ],
) -> Optional[RoleName]:
    """Handles POST request to list instructors and staff.

    Args:
        request (HttpRequest): The request object containing user data.
        course_id (str): The ID of the course to list instructors and staff for.

    Returns:
        Response: A Response object containing the list of instructors and staff or an error message.

    Raises:
        Http404: If the course does not exist.

    Args:
        course_id (str):
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoleName
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
    )


async def asyncio_detailed(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[

        RoleName,
    ],
) -> Response[RoleName]:
    """Handles POST request to list instructors and staff.

    Args:
        request (HttpRequest): The request object containing user data.
        course_id (str): The ID of the course to list instructors and staff for.

    Returns:
        Response: A Response object containing the list of instructors and staff or an error message.

    Raises:
        Http404: If the course does not exist.

    Args:
        course_id (str):
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoleName]
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
        RoleName,
        RoleName,
        RoleName,
    ],
) -> Optional[RoleName]:
    """Handles POST request to list instructors and staff.

    Args:
        request (HttpRequest): The request object containing user data.
        course_id (str): The ID of the course to list instructors and staff for.

    Returns:
        Response: A Response object containing the list of instructors and staff or an error message.

    Raises:
        Http404: If the course does not exist.

    Args:
        course_id (str):
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.
        body (RoleName): Serializer that describes the response of the problem response report
            generation API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoleName
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
