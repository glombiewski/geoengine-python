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



from pydantic import BaseModel, Field
from openapi_client.models.format_specifics_one_of_csv import FormatSpecificsOneOfCsv

class FormatSpecificsOneOf(BaseModel):
    """
    FormatSpecificsOneOf
    """
    csv: FormatSpecificsOneOfCsv = Field(...)
    __properties = ["csv"]

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
    def from_json(cls, json_str: str) -> FormatSpecificsOneOf:
        """Create an instance of FormatSpecificsOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of csv
        if self.csv:
            _dict['csv'] = self.csv.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormatSpecificsOneOf:
        """Create an instance of FormatSpecificsOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FormatSpecificsOneOf.parse_obj(obj)

        _obj = FormatSpecificsOneOf.parse_obj({
            "csv": FormatSpecificsOneOfCsv.from_dict(obj.get("csv")) if obj.get("csv") is not None else None
        })
        return _obj


