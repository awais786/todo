import attrs
from typing import Union, Dict, Any
from generated_client.authoring_api_client.types import UNSET, Unset


@attrs.define
class StudentProgressUrl:
    """Model for student progress URL request and response."""

    unique_student_identifier: str  # Required field for the request
    course_id: Union[Unset, str] = UNSET  # Optional for request
    progress_url: Union[Unset, str] = UNSET  # Optional, only for response
    additional_properties: Dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the instance to a dictionary."""
        data = {
            "unique_student_identifier": self.unique_student_identifier,
            "course_id": self.course_id if self.course_id is not UNSET else None,
            "progress_url": self.progress_url if self.progress_url is not UNSET else None,
        }
        return {key: value for key, value in data.items() if value is not None}

    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> "StudentProgressUrl":
        course_id = src_dict.get('course_id', UNSET)
        progress_url = src_dict.get('progress_url', UNSET)  # Progress URL for response
        return cls(
            unique_student_identifier='unique_student_identifier',
            course_id=course_id,
            progress_url=progress_url
        )
