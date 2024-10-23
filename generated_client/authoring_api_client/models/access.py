from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_enum import ActionEnum

T = TypeVar("T", bound="Access")

@_attrs_define
class Access:
    """Serializer for managing user access changes.
    This serializer validates and processes the data required to modify
    user access within a system.

        Attributes:
            unique_student_identifier (str): Email or username of user to change access
            rolename (str): Role name to assign to the user
            action (ActionEnum): * `allow` - allow
                * `revoke` - revoke
    """

    unique_student_identifier: str
    rolename: str
    action: ActionEnum
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_student_identifier = self.unique_student_identifier
        rolename = self.rolename
        action = self.action.value
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
                "rolename": rolename,
                "action": action,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        unique_student_identifier = (None, str(self.unique_student_identifier).encode(), "text/plain")

        rolename = (None, str(self.rolename).encode(), "text/plain")

        action = (None, str(self.action.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "unique_student_identifier": unique_student_identifier,
                "rolename": rolename,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_student_identifier = d.pop("unique_student_identifier")

        rolename = d.pop("rolename")

        action = ActionEnum(d.pop("action"))

        access = cls(
            unique_student_identifier=unique_student_identifier,
            rolename=rolename,
            action=action,
        )

        access.additional_properties = d
        return access

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
