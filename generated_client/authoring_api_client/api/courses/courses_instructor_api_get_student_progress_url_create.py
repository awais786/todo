from http import HTTPStatus
from typing import Any, Dict, Optional, Union

from ...client import AuthenticatedClient, Client
from ...models.student_progress_url import StudentProgressUrl
from ...types import Response
import json


def _get_kwargs(course_id: str, body: StudentProgressUrl) -> Dict[str, Any]:
    """Constructs the parameters for the HTTP request."""
    return {
        "method": "POST",
        "url": f"/courses/{course_id}/instructor/api/get_student_progress_url",
        "json": body.to_dict(),  # Serialize the model to a dictionary
    }


def _parse_response(
        *, client: Union[AuthenticatedClient, Client], response: Response
) -> Optional[StudentProgressUrl]:
    if response.status_code == HTTPStatus.OK:
        response_data = response.content.decode('utf-8')  # Decode bytes to string
        response_dict = json.loads(response_data)  # Convert JSON string to dict
        # Return an instance of StudentProgressUrl created from the response dictionary
        return StudentProgressUrl.from_dict(response_dict)

    if client.raise_on_unexpected_status:
        raise Exception(f"Unexpected status: {response.status_code}, Content: {response.content}")

    return None


def _build_response(client: Union[AuthenticatedClient, Client], response: Response) -> Response[StudentProgressUrl]:
    """Constructs a Response object to standardize the response format."""
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
        body: StudentProgressUrl,
) -> Response[StudentProgressUrl]:
    """Sends a POST request to retrieve the student progress URL."""
    kwargs = _get_kwargs(course_id=course_id, body=body)
    response = client.get_httpx_client().request(**kwargs)
    return _build_response(client=client, response=response)


def sync(
        course_id: str,
        *,
        client: Union[AuthenticatedClient, Client],
        body: Union[
            StudentProgressUrl,
        ],
) -> Optional[StudentProgressUrl]:
    """Post method for validating incoming data and generating progress URL
    Returns:
        StudentProgressUrl
    """
    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
    ).parsed
