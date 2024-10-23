from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from generated_client.authoring_api_client.types import UNSET, Unset

T = TypeVar("T", bound="RoleName")


@_attrs_define
class RoleName:
    """Serializer that describes the response of the problem response report generation API.

    Attributes:
        rolename (str): Role name
    """
    rolename: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rolename": self.rolename,
        }

    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> "RoleName":
        rolename = src_dict.get('rolename', UNSET)  # Progress URL for response
        return cls(
            rolename=rolename
        )
