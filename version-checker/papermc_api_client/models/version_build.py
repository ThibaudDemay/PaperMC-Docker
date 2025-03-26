# coding: utf-8

"""
    PaperMC API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from papermc_api_client.models.change import Change
from papermc_api_client.models.download import Download
from typing import Optional, Set
from typing_extensions import Self

class VersionBuild(BaseModel):
    """
    VersionBuild
    """ # noqa: E501
    build: Optional[Annotated[int, Field(strict=True)]] = None
    time: Optional[datetime] = None
    channel: Optional[StrictStr] = None
    promoted: Optional[StrictBool] = None
    changes: Optional[List[Change]] = None
    downloads: Optional[Dict[str, Download]] = None
    __properties: ClassVar[List[str]] = ["build", "time", "channel", "promoted", "changes", "downloads"]

    @field_validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'experimental']):
            raise ValueError("must be one of enum values ('default', 'experimental')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VersionBuild from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item_changes in self.changes:
                if _item_changes:
                    _items.append(_item_changes.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in downloads (dict)
        _field_dict = {}
        if self.downloads:
            for _key_downloads in self.downloads:
                if self.downloads[_key_downloads]:
                    _field_dict[_key_downloads] = self.downloads[_key_downloads].to_dict()
            _dict['downloads'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VersionBuild from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build": obj.get("build"),
            "time": obj.get("time"),
            "channel": obj.get("channel"),
            "promoted": obj.get("promoted"),
            "changes": [Change.from_dict(_item) for _item in obj["changes"]] if obj.get("changes") is not None else None,
            "downloads": dict(
                (_k, Download.from_dict(_v))
                for _k, _v in obj["downloads"].items()
            )
            if obj.get("downloads") is not None
            else None
        })
        return _obj


