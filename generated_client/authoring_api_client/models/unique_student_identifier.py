from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UniqueStudentIdentifier")


@_attrs_define
class UniqueStudentIdentifier:
    """Serializer for identifying unique_student.

    Attributes:
        unique_student_identifier (str): Email or username of user to change access
    """

    unique_student_identifier: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_student_identifier = self.unique_student_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        unique_student_identifier = (None, str(self.unique_student_identifier).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        import pdb;
        pdb.set_trace()
        d = src_dict.copy()
        unique_student_identifier = d.pop("unique_student_identifier")

        unique_student_identifier = cls(
            unique_student_identifier=unique_student_identifier,
        )

        unique_student_identifier.additional_properties = d
        return unique_student_identifier

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
