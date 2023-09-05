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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class WcsBoundingbox(BaseModel):
    """
    WcsBoundingbox
    """
    bbox: conlist(Union[StrictFloat, StrictInt]) = Field(...)
    spatial_reference: Optional[StrictStr] = None
    __properties = ["bbox", "spatial_reference"]

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
    def from_json(cls, json_str: str) -> WcsBoundingbox:
        """Create an instance of WcsBoundingbox from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if spatial_reference (nullable) is None
        # and __fields_set__ contains the field
        if self.spatial_reference is None and "spatial_reference" in self.__fields_set__:
            _dict['spatial_reference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WcsBoundingbox:
        """Create an instance of WcsBoundingbox from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WcsBoundingbox.parse_obj(obj)

        _obj = WcsBoundingbox.parse_obj({
            "bbox": obj.get("bbox"),
            "spatial_reference": obj.get("spatial_reference")
        })
        return _obj


