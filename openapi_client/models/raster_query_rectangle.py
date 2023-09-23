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



from pydantic import BaseModel, Field
from openapi_client.models.spatial_partition2_d import SpatialPartition2D
from openapi_client.models.spatial_resolution import SpatialResolution
from openapi_client.models.time_interval import TimeInterval

class RasterQueryRectangle(BaseModel):
    """
    A spatio-temporal rectangle with a specified resolution
    """
    spatial_bounds: SpatialPartition2D = Field(..., alias="spatialBounds")
    spatial_resolution: SpatialResolution = Field(..., alias="spatialResolution")
    time_interval: TimeInterval = Field(..., alias="timeInterval")
    __properties = ["spatialBounds", "spatialResolution", "timeInterval"]

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
    def from_json(cls, json_str: str) -> RasterQueryRectangle:
        """Create an instance of RasterQueryRectangle from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of spatial_bounds
        if self.spatial_bounds:
            _dict['spatialBounds'] = self.spatial_bounds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_resolution
        if self.spatial_resolution:
            _dict['spatialResolution'] = self.spatial_resolution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_interval
        if self.time_interval:
            _dict['timeInterval'] = self.time_interval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RasterQueryRectangle:
        """Create an instance of RasterQueryRectangle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RasterQueryRectangle.parse_obj(obj)

        _obj = RasterQueryRectangle.parse_obj({
            "spatial_bounds": SpatialPartition2D.from_dict(obj.get("spatialBounds")) if obj.get("spatialBounds") is not None else None,
            "spatial_resolution": SpatialResolution.from_dict(obj.get("spatialResolution")) if obj.get("spatialResolution") is not None else None,
            "time_interval": TimeInterval.from_dict(obj.get("timeInterval")) if obj.get("timeInterval") is not None else None
        })
        return _obj


