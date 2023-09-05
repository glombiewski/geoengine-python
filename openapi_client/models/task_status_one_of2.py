# coding: utf-8

"""
    Geo Engine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator

class TaskStatusOneOf2(BaseModel):
    """
    TaskStatusOneOf2
    """
    clean_up: Optional[Dict[str, Any]] = Field(None, alias="cleanUp")
    status: Optional[StrictStr] = None
    __properties = ["cleanUp", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('aborted'):
            raise ValueError("must be one of enum values ('aborted')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TaskStatusOneOf2:
        """Create an instance of TaskStatusOneOf2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskStatusOneOf2:
        """Create an instance of TaskStatusOneOf2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskStatusOneOf2.parse_obj(obj)

        _obj = TaskStatusOneOf2.parse_obj({
            "clean_up": obj.get("cleanUp"),
            "status": obj.get("status")
        })
        return _obj


