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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.provenance import Provenance
from openapi_client.models.symbology import Symbology
from openapi_client.models.typed_result_descriptor import TypedResultDescriptor

class Dataset(BaseModel):
    """
    Dataset
    """
    description: StrictStr = Field(...)
    display_name: StrictStr = Field(..., alias="displayName")
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    provenance: Optional[conlist(Provenance)] = None
    result_descriptor: TypedResultDescriptor = Field(..., alias="resultDescriptor")
    source_operator: StrictStr = Field(..., alias="sourceOperator")
    symbology: Optional[Symbology] = None
    __properties = ["description", "displayName", "id", "name", "provenance", "resultDescriptor", "sourceOperator", "symbology"]

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
    def from_json(cls, json_str: str) -> Dataset:
        """Create an instance of Dataset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in provenance (list)
        _items = []
        if self.provenance:
            for _item in self.provenance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['provenance'] = _items
        # override the default output from pydantic by calling `to_dict()` of result_descriptor
        if self.result_descriptor:
            _dict['resultDescriptor'] = self.result_descriptor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of symbology
        if self.symbology:
            _dict['symbology'] = self.symbology.to_dict()
        # set to None if provenance (nullable) is None
        # and __fields_set__ contains the field
        if self.provenance is None and "provenance" in self.__fields_set__:
            _dict['provenance'] = None

        # set to None if symbology (nullable) is None
        # and __fields_set__ contains the field
        if self.symbology is None and "symbology" in self.__fields_set__:
            _dict['symbology'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Dataset:
        """Create an instance of Dataset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Dataset.parse_obj(obj)

        _obj = Dataset.parse_obj({
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "provenance": [Provenance.from_dict(_item) for _item in obj.get("provenance")] if obj.get("provenance") is not None else None,
            "result_descriptor": TypedResultDescriptor.from_dict(obj.get("resultDescriptor")) if obj.get("resultDescriptor") is not None else None,
            "source_operator": obj.get("sourceOperator"),
            "symbology": Symbology.from_dict(obj.get("symbology")) if obj.get("symbology") is not None else None
        })
        return _obj


