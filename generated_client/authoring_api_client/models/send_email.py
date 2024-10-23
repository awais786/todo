from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendEmail")


@_attrs_define
class SendEmail:
    """Serializer for sending an email with optional scheduling.

    Fields:
        send_to (str): The email address of the recipient. This field is required.
        subject (str): The subject line of the email. This field is required.
        message (str): The body of the email. This field is required.
        schedule (str, optional):
        An optional field to specify when the email should be sent.
        If provided, this should be a string that can be parsed into a
        datetime format or some other scheduling logic.

        Attributes:
            send_to (str):
            subject (str):
            message (str):
            schedule (Union[Unset, str]):
    """

    send_to: str
    subject: str
    message: str
    schedule: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_to = self.send_to

        subject = self.subject

        message = self.message

        schedule = self.schedule

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "send_to": send_to,
                "subject": subject,
                "message": message,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        send_to = (None, str(self.send_to).encode(), "text/plain")

        subject = (None, str(self.subject).encode(), "text/plain")

        message = (None, str(self.message).encode(), "text/plain")

        schedule = (
            self.schedule if isinstance(self.schedule, Unset) else (None, str(self.schedule).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "send_to": send_to,
                "subject": subject,
                "message": message,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_to = d.pop("send_to")

        subject = d.pop("subject")

        message = d.pop("message")

        schedule = d.pop("schedule", UNSET)

        send_email = cls(
            send_to=send_to,
            subject=subject,
            message=message,
            schedule=schedule,
        )

        send_email.additional_properties = d
        return send_email

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
