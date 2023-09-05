# coding: utf-8

"""
    Geo Engine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TimeReference(str, Enum):
    """
    TimeReference
    """

    """
    allowed enum values
    """
    START = 'start'
    END = 'end'

    @classmethod
    def from_json(cls, json_str: str) -> TimeReference:
        """Create an instance of TimeReference from a JSON string"""
        return TimeReference(json.loads(json_str))


