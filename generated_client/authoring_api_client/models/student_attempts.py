from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StudentAttempts")


@_attrs_define
class StudentAttempts:
    """Serializer for resetting a students attempts counter or starts a task to reset all students
    attempts counters.

        Attributes:
            problem_to_reset (str): The identifier or description of the problem that needs to be reset.
            unique_student_identifier (Union[Unset, str]): Email or username of student.
            all_students (Union[Unset, str]):
            delete_module (Union[Unset, str]):
    """

    problem_to_reset: str
    unique_student_identifier: Union[Unset, str] = UNSET
    all_students: Union[Unset, str] = UNSET
    delete_module: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        problem_to_reset = self.problem_to_reset

        unique_student_identifier = self.unique_student_identifier

        all_students = self.all_students

        delete_module = self.delete_module

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "problem_to_reset": problem_to_reset,
            }
        )
        if unique_student_identifier is not UNSET:
            field_dict["unique_student_identifier"] = unique_student_identifier
        if all_students is not UNSET:
            field_dict["all_students"] = all_students
        if delete_module is not UNSET:
            field_dict["delete_module"] = delete_module

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        problem_to_reset = (None, str(self.problem_to_reset).encode(), "text/plain")

        unique_student_identifier = (
            self.unique_student_identifier
            if isinstance(self.unique_student_identifier, Unset)
            else (None, str(self.unique_student_identifier).encode(), "text/plain")
        )

        all_students = (
            self.all_students
            if isinstance(self.all_students, Unset)
            else (None, str(self.all_students).encode(), "text/plain")
        )

        delete_module = (
            self.delete_module
            if isinstance(self.delete_module, Unset)
            else (None, str(self.delete_module).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "problem_to_reset": problem_to_reset,
            }
        )
        if unique_student_identifier is not UNSET:
            field_dict["unique_student_identifier"] = unique_student_identifier
        if all_students is not UNSET:
            field_dict["all_students"] = all_students
        if delete_module is not UNSET:
            field_dict["delete_module"] = delete_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        problem_to_reset = d.pop("problem_to_reset")

        unique_student_identifier = d.pop("unique_student_identifier", UNSET)

        all_students = d.pop("all_students", UNSET)

        delete_module = d.pop("delete_module", UNSET)

        student_attempts = cls(
            problem_to_reset=problem_to_reset,
            unique_student_identifier=unique_student_identifier,
            all_students=all_students,
            delete_module=delete_module,
        )

        student_attempts.additional_properties = d
        return student_attempts

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
