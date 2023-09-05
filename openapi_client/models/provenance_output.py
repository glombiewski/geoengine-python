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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from openapi_client.models.data_id import DataId
from openapi_client.models.provenance import Provenance

class ProvenanceOutput(BaseModel):
    """
    ProvenanceOutput
    """
    data: DataId = Field(...)
    provenance: Optional[conlist(Provenance)] = None
    __properties = ["data", "provenance"]

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
    def from_json(cls, json_str: str) -> ProvenanceOutput:
        """Create an instance of ProvenanceOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in provenance (list)
        _items = []
        if self.provenance:
            for _item in self.provenance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['provenance'] = _items
        # set to None if provenance (nullable) is None
        # and __fields_set__ contains the field
        if self.provenance is None and "provenance" in self.__fields_set__:
            _dict['provenance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProvenanceOutput:
        """Create an instance of ProvenanceOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProvenanceOutput.parse_obj(obj)

        _obj = ProvenanceOutput.parse_obj({
            "data": DataId.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "provenance": [Provenance.from_dict(_item) for _item in obj.get("provenance")] if obj.get("provenance") is not None else None
        })
        return _obj


