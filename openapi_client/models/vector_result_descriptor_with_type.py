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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.bounding_box2_d import BoundingBox2D
from openapi_client.models.vector_column_info import VectorColumnInfo
from openapi_client.models.vector_data_type import VectorDataType

class VectorResultDescriptorWithType(BaseModel):
    """
    VectorResultDescriptorWithType
    """
    bbox: Optional[BoundingBox2D] = None
    columns: Dict[str, VectorColumnInfo] = Field(...)
    data_type: VectorDataType = Field(..., alias="dataType")
    spatial_reference: StrictStr = Field(..., alias="spatialReference")
    time: Optional[StrictStr] = None
    type: StrictStr = Field(...)
    __properties = ["bbox", "columns", "dataType", "spatialReference", "time", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('vector'):
            raise ValueError("must be one of enum values ('vector')")
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
    def from_json(cls, json_str: str) -> VectorResultDescriptorWithType:
        """Create an instance of VectorResultDescriptorWithType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bbox
        if self.bbox:
            _dict['bbox'] = self.bbox.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in columns (dict)
        _field_dict = {}
        if self.columns:
            for _key in self.columns:
                if self.columns[_key]:
                    _field_dict[_key] = self.columns[_key].to_dict()
            _dict['columns'] = _field_dict
        # set to None if bbox (nullable) is None
        # and __fields_set__ contains the field
        if self.bbox is None and "bbox" in self.__fields_set__:
            _dict['bbox'] = None

        # set to None if time (nullable) is None
        # and __fields_set__ contains the field
        if self.time is None and "time" in self.__fields_set__:
            _dict['time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VectorResultDescriptorWithType:
        """Create an instance of VectorResultDescriptorWithType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VectorResultDescriptorWithType.parse_obj(obj)

        _obj = VectorResultDescriptorWithType.parse_obj({
            "bbox": BoundingBox2D.from_dict(obj.get("bbox")) if obj.get("bbox") is not None else None,
            "columns": dict(
                (_k, VectorColumnInfo.from_dict(_v))
                for _k, _v in obj.get("columns").items()
            )
            if obj.get("columns") is not None
            else None,
            "data_type": obj.get("dataType"),
            "spatial_reference": obj.get("spatialReference"),
            "time": obj.get("time"),
            "type": obj.get("type")
        })
        return _obj


