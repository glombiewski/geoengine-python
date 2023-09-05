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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.typed_geometry_one_of import TypedGeometryOneOf
from openapi_client.models.typed_geometry_one_of1 import TypedGeometryOneOf1
from openapi_client.models.typed_geometry_one_of2 import TypedGeometryOneOf2
from openapi_client.models.typed_geometry_one_of3 import TypedGeometryOneOf3
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

TYPEDGEOMETRY_ONE_OF_SCHEMAS = ["TypedGeometryOneOf", "TypedGeometryOneOf1", "TypedGeometryOneOf2", "TypedGeometryOneOf3"]

class TypedGeometry(BaseModel):
    """
    TypedGeometry
    """
    # data type: TypedGeometryOneOf
    oneof_schema_1_validator: Optional[TypedGeometryOneOf] = None
    # data type: TypedGeometryOneOf1
    oneof_schema_2_validator: Optional[TypedGeometryOneOf1] = None
    # data type: TypedGeometryOneOf2
    oneof_schema_3_validator: Optional[TypedGeometryOneOf2] = None
    # data type: TypedGeometryOneOf3
    oneof_schema_4_validator: Optional[TypedGeometryOneOf3] = None
    if TYPE_CHECKING:
        actual_instance: Union[TypedGeometryOneOf, TypedGeometryOneOf1, TypedGeometryOneOf2, TypedGeometryOneOf3]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(TYPEDGEOMETRY_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

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
        instance = TypedGeometry.construct()
        error_messages = []
        match = 0
        # validate data type: TypedGeometryOneOf
        if not isinstance(v, TypedGeometryOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TypedGeometryOneOf`")
        else:
            match += 1
        # validate data type: TypedGeometryOneOf1
        if not isinstance(v, TypedGeometryOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TypedGeometryOneOf1`")
        else:
            match += 1
        # validate data type: TypedGeometryOneOf2
        if not isinstance(v, TypedGeometryOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TypedGeometryOneOf2`")
        else:
            match += 1
        # validate data type: TypedGeometryOneOf3
        if not isinstance(v, TypedGeometryOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TypedGeometryOneOf3`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TypedGeometry with oneOf schemas: TypedGeometryOneOf, TypedGeometryOneOf1, TypedGeometryOneOf2, TypedGeometryOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TypedGeometry with oneOf schemas: TypedGeometryOneOf, TypedGeometryOneOf1, TypedGeometryOneOf2, TypedGeometryOneOf3. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TypedGeometry:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TypedGeometry:
        """Returns the object represented by the json string"""
        instance = TypedGeometry.construct()
        error_messages = []
        match = 0

        # deserialize data into TypedGeometryOneOf
        try:
            instance.actual_instance = TypedGeometryOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TypedGeometryOneOf1
        try:
            instance.actual_instance = TypedGeometryOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TypedGeometryOneOf2
        try:
            instance.actual_instance = TypedGeometryOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TypedGeometryOneOf3
        try:
            instance.actual_instance = TypedGeometryOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TypedGeometry with oneOf schemas: TypedGeometryOneOf, TypedGeometryOneOf1, TypedGeometryOneOf2, TypedGeometryOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TypedGeometry with oneOf schemas: TypedGeometryOneOf, TypedGeometryOneOf1, TypedGeometryOneOf2, TypedGeometryOneOf3. Details: " + ", ".join(error_messages))
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


