from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListInstructorTaskInput")


@_attrs_define
class ListInstructorTaskInput:
    """Serializer for handling the input data for the problem response report generation API.

    Attributes:
        unique_student_identifier (str): The email or username of the student.
                                          This field is optional, but if provided, the `problem_location_str`
                                          must also be provided.
        problem_location_str (str): The string representing the location of the problem within the course.
                                    This field is optional, unless `unique_student_identifier` is provided.

        Attributes:
            unique_student_identifier (Union[Unset, str]): Email or username of student
            problem_location_str (Union[Unset, str]): Problem location
    """

    unique_student_identifier: Union[Unset, str] = UNSET
    problem_location_str: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_student_identifier = self.unique_student_identifier

        problem_location_str = self.problem_location_str

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_student_identifier is not UNSET:
            field_dict["unique_student_identifier"] = unique_student_identifier
        if problem_location_str is not UNSET:
            field_dict["problem_location_str"] = problem_location_str

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        unique_student_identifier = (
            self.unique_student_identifier
            if isinstance(self.unique_student_identifier, Unset)
            else (None, str(self.unique_student_identifier).encode(), "text/plain")
        )

        problem_location_str = (
            self.problem_location_str
            if isinstance(self.problem_location_str, Unset)
            else (None, str(self.problem_location_str).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if unique_student_identifier is not UNSET:
            field_dict["unique_student_identifier"] = unique_student_identifier
        if problem_location_str is not UNSET:
            field_dict["problem_location_str"] = problem_location_str

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_student_identifier = d.pop("unique_student_identifier", UNSET)

        problem_location_str = d.pop("problem_location_str", UNSET)

        list_instructor_task_input = cls(
            unique_student_identifier=unique_student_identifier,
            problem_location_str=problem_location_str,
        )

        list_instructor_task_input.additional_properties = d
        return list_instructor_task_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
