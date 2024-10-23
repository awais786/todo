from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """Serializer for identifying unique_student.

    Attributes:
        unique_student_identifier (str): Email or username of user to change access
        problem_to_reset (str): The URL name of the problem to reset.
        score (str): Score must be a valid number or decimal, e.g., 1.00
    """

    unique_student_identifier: str
    problem_to_reset: str
    score: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_student_identifier = self.unique_student_identifier

        problem_to_reset = self.problem_to_reset

        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
                "problem_to_reset": problem_to_reset,
                "score": score,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        unique_student_identifier = (None, str(self.unique_student_identifier).encode(), "text/plain")

        problem_to_reset = (None, str(self.problem_to_reset).encode(), "text/plain")

        score = (None, str(self.score).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
                "problem_to_reset": problem_to_reset,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_student_identifier = d.pop("unique_student_identifier")

        problem_to_reset = d.pop("problem_to_reset")

        score = d.pop("score")

        problem = cls(
            unique_student_identifier=unique_student_identifier,
            problem_to_reset=problem_to_reset,
            score=score,
        )

        problem.additional_properties = d
        return problem

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
