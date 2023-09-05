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
from openapi_client.models.raster_properties_entry_type import RasterPropertiesEntryType
from openapi_client.models.raster_properties_key import RasterPropertiesKey

class GdalMetadataMapping(BaseModel):
    """
    GdalMetadataMapping
    """
    source_key: RasterPropertiesKey = Field(...)
    target_key: RasterPropertiesKey = Field(...)
    target_type: RasterPropertiesEntryType = Field(...)
    __properties = ["source_key", "target_key", "target_type"]

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
    def from_json(cls, json_str: str) -> GdalMetadataMapping:
        """Create an instance of GdalMetadataMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_key
        if self.source_key:
            _dict['source_key'] = self.source_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_key
        if self.target_key:
            _dict['target_key'] = self.target_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GdalMetadataMapping:
        """Create an instance of GdalMetadataMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GdalMetadataMapping.parse_obj(obj)

        _obj = GdalMetadataMapping.parse_obj({
            "source_key": RasterPropertiesKey.from_dict(obj.get("source_key")) if obj.get("source_key") is not None else None,
            "target_key": RasterPropertiesKey.from_dict(obj.get("target_key")) if obj.get("target_key") is not None else None,
            "target_type": obj.get("target_type")
        })
        return _obj


