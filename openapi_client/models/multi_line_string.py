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


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.coordinate2_d import Coordinate2D

class MultiLineString(BaseModel):
    """
    MultiLineString
    """
    coordinates: conlist(conlist(Coordinate2D)) = Field(...)
    __properties = ["coordinates"]

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
    def from_json(cls, json_str: str) -> MultiLineString:
        """Create an instance of MultiLineString from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in coordinates (list of list)
        _items = []
        if self.coordinates:
            for _item in self.coordinates:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['coordinates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MultiLineString:
        """Create an instance of MultiLineString from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MultiLineString.parse_obj(obj)

        _obj = MultiLineString.parse_obj({
            "coordinates": [
                    [Coordinate2D.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj.get("coordinates")
                ] if obj.get("coordinates") is not None else None
        })
        return _obj


