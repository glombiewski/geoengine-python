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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.linear_gradient_with_type import LinearGradientWithType
from openapi_client.models.logarithmic_gradient_with_type import LogarithmicGradientWithType
from openapi_client.models.palette_colorizer import PaletteColorizer
from openapi_client.models.rgba_colorizer import RgbaColorizer
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

COLORIZER_ONE_OF_SCHEMAS = ["LinearGradientWithType", "LogarithmicGradientWithType", "PaletteColorizer", "RgbaColorizer"]

class Colorizer(BaseModel):
    """
    Colorizer
    """
    # data type: LinearGradientWithType
    oneof_schema_1_validator: Optional[LinearGradientWithType] = None
    # data type: LogarithmicGradientWithType
    oneof_schema_2_validator: Optional[LogarithmicGradientWithType] = None
    # data type: PaletteColorizer
    oneof_schema_3_validator: Optional[PaletteColorizer] = None
    # data type: RgbaColorizer
    oneof_schema_4_validator: Optional[RgbaColorizer] = None
    if TYPE_CHECKING:
        actual_instance: Union[LinearGradientWithType, LogarithmicGradientWithType, PaletteColorizer, RgbaColorizer]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(COLORIZER_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Colorizer.construct()
        error_messages = []
        match = 0
        # validate data type: LinearGradientWithType
        if not isinstance(v, LinearGradientWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LinearGradientWithType`")
        else:
            match += 1
        # validate data type: LogarithmicGradientWithType
        if not isinstance(v, LogarithmicGradientWithType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LogarithmicGradientWithType`")
        else:
            match += 1
        # validate data type: PaletteColorizer
        if not isinstance(v, PaletteColorizer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaletteColorizer`")
        else:
            match += 1
        # validate data type: RgbaColorizer
        if not isinstance(v, RgbaColorizer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RgbaColorizer`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Colorizer with oneOf schemas: LinearGradientWithType, LogarithmicGradientWithType, PaletteColorizer, RgbaColorizer. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Colorizer with oneOf schemas: LinearGradientWithType, LogarithmicGradientWithType, PaletteColorizer, RgbaColorizer. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Colorizer:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Colorizer:
        """Returns the object represented by the json string"""
        instance = Colorizer.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `LinearGradientWithType`
        if _data_type == "LinearGradientWithType":
            instance.actual_instance = LinearGradientWithType.from_json(json_str)
            return instance

        # check if data type is `LogarithmicGradientWithType`
        if _data_type == "LogarithmicGradientWithType":
            instance.actual_instance = LogarithmicGradientWithType.from_json(json_str)
            return instance

        # check if data type is `PaletteColorizer`
        if _data_type == "PaletteColorizer":
            instance.actual_instance = PaletteColorizer.from_json(json_str)
            return instance

        # check if data type is `RgbaColorizer`
        if _data_type == "RgbaColorizer":
            instance.actual_instance = RgbaColorizer.from_json(json_str)
            return instance

        # check if data type is `LinearGradientWithType`
        if _data_type == "linearGradient":
            instance.actual_instance = LinearGradientWithType.from_json(json_str)
            return instance

        # check if data type is `LogarithmicGradientWithType`
        if _data_type == "logarithmicGradient":
            instance.actual_instance = LogarithmicGradientWithType.from_json(json_str)
            return instance

        # check if data type is `PaletteColorizer`
        if _data_type == "palette":
            instance.actual_instance = PaletteColorizer.from_json(json_str)
            return instance

        # check if data type is `RgbaColorizer`
        if _data_type == "rgba":
            instance.actual_instance = RgbaColorizer.from_json(json_str)
            return instance

        # deserialize data into LinearGradientWithType
        try:
            instance.actual_instance = LinearGradientWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LogarithmicGradientWithType
        try:
            instance.actual_instance = LogarithmicGradientWithType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaletteColorizer
        try:
            instance.actual_instance = PaletteColorizer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RgbaColorizer
        try:
            instance.actual_instance = RgbaColorizer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Colorizer with oneOf schemas: LinearGradientWithType, LogarithmicGradientWithType, PaletteColorizer, RgbaColorizer. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Colorizer with oneOf schemas: LinearGradientWithType, LogarithmicGradientWithType, PaletteColorizer, RgbaColorizer. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


