from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockDueDate")


@_attrs_define
class BlockDueDate:
    """Serializer for handling block due date updates for a specific student.
    Fields:
        url (str): The URL related to the block that needs the due date update.
        due_datetime (str): The new due date and time for the block.
        student (str): The email or username of the student whose access is being modified.
        reason (str): Reason why updating this.

        Attributes:
            url (str):
            due_datetime (str):
            student (str): Email or username of user to change access
            reason (Union[Unset, str]):
    """

    url: str
    due_datetime: str
    student: str
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        due_datetime = self.due_datetime

        student = self.student

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "due_datetime": due_datetime,
                "student": student,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = (None, str(self.url).encode(), "text/plain")

        due_datetime = (None, str(self.due_datetime).encode(), "text/plain")

        student = (None, str(self.student).encode(), "text/plain")

        reason = self.reason if isinstance(self.reason, Unset) else (None, str(self.reason).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "url": url,
                "due_datetime": due_datetime,
                "student": student,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        due_datetime = d.pop("due_datetime")

        student = d.pop("student")

        reason = d.pop("reason", UNSET)

        block_due_date = cls(
            url=url,
            due_datetime=due_datetime,
            student=student,
            reason=reason,
        )

        block_due_date.additional_properties = d
        return block_due_date

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
