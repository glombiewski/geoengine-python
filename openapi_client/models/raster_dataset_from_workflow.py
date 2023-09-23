# coding: utf-8

"""
    Geo Engine Pro API

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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from openapi_client.models.raster_query_rectangle import RasterQueryRectangle

class RasterDatasetFromWorkflow(BaseModel):
    """
    parameter for the dataset from workflow handler (body)
    """
    as_cog: Optional[StrictBool] = Field(True, alias="asCog")
    description: Optional[StrictStr] = None
    display_name: StrictStr = Field(..., alias="displayName")
    name: Optional[StrictStr] = None
    query: RasterQueryRectangle = Field(...)
    __properties = ["asCog", "description", "displayName", "name", "query"]

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
    def from_json(cls, json_str: str) -> RasterDatasetFromWorkflow:
        """Create an instance of RasterDatasetFromWorkflow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True,
                          # Note: remove as_cog when set to default
                          exclude_defaults=True)
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RasterDatasetFromWorkflow:
        """Create an instance of RasterDatasetFromWorkflow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RasterDatasetFromWorkflow.parse_obj(obj)

        _obj = RasterDatasetFromWorkflow.parse_obj({
            "as_cog": obj.get("asCog") if obj.get("asCog") is not None else True,
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "name": obj.get("name"),
            "query": RasterQueryRectangle.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj


