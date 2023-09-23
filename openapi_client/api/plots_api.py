# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from openapi_client.models.wrapped_plot_output import WrappedPlotOutput

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_plot_handler(self, bbox : StrictStr, time : StrictStr, spatial_resolution : StrictStr, id : Annotated[StrictStr, Field(..., description="Workflow id")], crs : Optional[StrictStr] = None, **kwargs) -> WrappedPlotOutput:  # noqa: E501
        """Generates a plot.  # noqa: E501

        Generates a plot.  # Example  1. Upload the file `plain_data.csv` with the following content:  ```csv a 1 2 ``` 2. Create a dataset from it using the \"Plain Data\" example at `/dataset`. 3. Create a statistics workflow using the \"Statistics Plot\" example at `/workflow`. 4. Generate the plot with this handler.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plot_handler(bbox, time, spatial_resolution, id, crs, async_req=True)
        >>> result = thread.get()

        :param bbox: (required)
        :type bbox: str
        :param time: (required)
        :type time: str
        :param spatial_resolution: (required)
        :type spatial_resolution: str
        :param id: Workflow id (required)
        :type id: str
        :param crs:
        :type crs: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WrappedPlotOutput
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_plot_handler_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_plot_handler_with_http_info(bbox, time, spatial_resolution, id, crs, **kwargs)  # noqa: E501

    @validate_arguments
    def get_plot_handler_with_http_info(self, bbox : StrictStr, time : StrictStr, spatial_resolution : StrictStr, id : Annotated[StrictStr, Field(..., description="Workflow id")], crs : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Generates a plot.  # noqa: E501

        Generates a plot.  # Example  1. Upload the file `plain_data.csv` with the following content:  ```csv a 1 2 ``` 2. Create a dataset from it using the \"Plain Data\" example at `/dataset`. 3. Create a statistics workflow using the \"Statistics Plot\" example at `/workflow`. 4. Generate the plot with this handler.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plot_handler_with_http_info(bbox, time, spatial_resolution, id, crs, async_req=True)
        >>> result = thread.get()

        :param bbox: (required)
        :type bbox: str
        :param time: (required)
        :type time: str
        :param spatial_resolution: (required)
        :type spatial_resolution: str
        :param id: Workflow id (required)
        :type id: str
        :param crs:
        :type crs: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WrappedPlotOutput, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'bbox',
            'time',
            'spatial_resolution',
            'id',
            'crs'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plot_handler" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('bbox') is not None:  # noqa: E501
            _query_params.append(('bbox', _params['bbox']))

        if _params.get('crs') is not None:  # noqa: E501
            _query_params.append(('crs', _params['crs']))

        if _params.get('time') is not None:  # noqa: E501
            _query_params.append(('time', _params['time']))

        if _params.get('spatial_resolution') is not None:  # noqa: E501
            _query_params.append(('spatialResolution', _params['spatial_resolution']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['session_token']  # noqa: E501

        _response_types_map = {
            '200': "WrappedPlotOutput",
        }

        return self.api_client.call_api(
            '/plot/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
