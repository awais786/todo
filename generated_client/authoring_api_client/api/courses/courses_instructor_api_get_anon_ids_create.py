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
        "url": f"/courses/{course_id}/instructor/api/get_anon_ids",
    }

    return _kwargs

import json
def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    status_code = response.status_code

    if status_code == HTTPStatus.OK:
        response_data = response.content.decode('utf-8')  # Decode bytes to string
        response_dict = json.loads(response_data)  # Convert JSON string to dict
        return status_code, response_dict  # Return status code and response dictionary

    if client.raise_on_unexpected_status:
        raise Exception(f"Unexpected status: {status_code}, Content: {response.content.decode('utf-8')}")

    return status_code, None  # Return status code and None if not OK


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    if not isinstance(response, httpx.Response):
        raise TypeError(f"Expected httpx.Response object, got {type(response).__name__}.")

        # Log the response type for debugging
    print(f"Response Type: {type(response).__name__}")

    # Call _parse_response to get the parsed content
    status_code, parsed_content = _parse_response(client=client, response=response)

    return Response(
        status_code=status_code,
        content=response.content,
        headers=response.headers,
        parsed=parsed_content,  # Use parsed_content from _parse_response
    )


def sync_detailed(
    course_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Handle POST request to generate a CSV output.

    Returns:
        Response: A CSV file with two columns: `user-id` and `anonymized-user-id`.

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
    """Handle POST request to generate a CSV output.

    Returns:
        Response: A CSV file with two columns: `user-id` and `anonymized-user-id`.

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


def sync(
        course_id: str,
        *,
        client: Union[AuthenticatedClient, Client],
):
    """Post method for validating incoming data and generating progress URL
    Returns:
        StudentProgressUrl
    """
    response = sync_detailed(
        course_id=course_id,
        client=client,
    ).parsed

    return _build_response(client=client, response=response)

