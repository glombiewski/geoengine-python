# coding: utf-8

"""
    Geo Engine API

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

from pydantic import Field, StrictFloat, StrictInt, StrictStr

from typing import Any, Optional, Union

from openapi_client.models.describe_coverage_request import DescribeCoverageRequest
from openapi_client.models.get_capabilities_request import GetCapabilitiesRequest
from openapi_client.models.get_coverage_format import GetCoverageFormat
from openapi_client.models.get_coverage_request import GetCoverageRequest
from openapi_client.models.wcs_service import WcsService
from openapi_client.models.wcs_version import WcsVersion

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OGCWCSApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def wcs_capabilities_handler(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], service : WcsService, request : GetCapabilitiesRequest, version : Optional[Any] = None, **kwargs) -> str:  # noqa: E501
        """Get WCS Capabilities  # noqa: E501

        Get WCS Capabilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_capabilities_handler(workflow, service, request, version, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: GetCapabilitiesRequest
        :param version:
        :type version: WcsVersion
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the wcs_capabilities_handler_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.wcs_capabilities_handler_with_http_info(workflow, service, request, version, **kwargs)  # noqa: E501

    @validate_arguments
    def wcs_capabilities_handler_with_http_info(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], service : WcsService, request : GetCapabilitiesRequest, version : Optional[Any] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get WCS Capabilities  # noqa: E501

        Get WCS Capabilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_capabilities_handler_with_http_info(workflow, service, request, version, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: GetCapabilitiesRequest
        :param version:
        :type version: WcsVersion
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
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'workflow',
            'service',
            'request',
            'version'
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
                    " to method wcs_capabilities_handler" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['workflow']:
            _path_params['workflow'] = _params['workflow']


        # process the query parameters
        _query_params = []
        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version'].value))

        if _params.get('service') is not None:  # noqa: E501
            _query_params.append(('service', _params['service'].value))

        if _params.get('request') is not None:  # noqa: E501
            _query_params.append(('request', _params['request'].value))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/xml'])  # noqa: E501

        # authentication setting
        _auth_settings = ['session_token']  # noqa: E501

        _response_types_map = {
            '200': "str",
        }

        return self.api_client.call_api(
            '/wcs/{workflow}?request=GetCapabilities', 'GET',
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

    @validate_arguments
    def wcs_describe_coverage_handler(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], version : WcsVersion, service : WcsService, request : DescribeCoverageRequest, identifiers : StrictStr, **kwargs) -> str:  # noqa: E501
        """Get WCS Coverage Description  # noqa: E501

        Get WCS Coverage Description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_describe_coverage_handler(workflow, version, service, request, identifiers, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param version: (required)
        :type version: WcsVersion
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: DescribeCoverageRequest
        :param identifiers: (required)
        :type identifiers: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the wcs_describe_coverage_handler_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.wcs_describe_coverage_handler_with_http_info(workflow, version, service, request, identifiers, **kwargs)  # noqa: E501

    @validate_arguments
    def wcs_describe_coverage_handler_with_http_info(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], version : WcsVersion, service : WcsService, request : DescribeCoverageRequest, identifiers : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Get WCS Coverage Description  # noqa: E501

        Get WCS Coverage Description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_describe_coverage_handler_with_http_info(workflow, version, service, request, identifiers, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param version: (required)
        :type version: WcsVersion
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: DescribeCoverageRequest
        :param identifiers: (required)
        :type identifiers: str
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
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'workflow',
            'version',
            'service',
            'request',
            'identifiers'
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
                    " to method wcs_describe_coverage_handler" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['workflow']:
            _path_params['workflow'] = _params['workflow']


        # process the query parameters
        _query_params = []
        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version'].value))

        if _params.get('service') is not None:  # noqa: E501
            _query_params.append(('service', _params['service'].value))

        if _params.get('request') is not None:  # noqa: E501
            _query_params.append(('request', _params['request'].value))

        if _params.get('identifiers') is not None:  # noqa: E501
            _query_params.append(('identifiers', _params['identifiers']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/xml'])  # noqa: E501

        # authentication setting
        _auth_settings = ['session_token']  # noqa: E501

        _response_types_map = {
            '200': "str",
        }

        return self.api_client.call_api(
            '/wcs/{workflow}?request=DescribeCoverage', 'GET',
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

    @validate_arguments
    def wcs_get_coverage_handler(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], version : WcsVersion, service : WcsService, request : GetCoverageRequest, format : GetCoverageFormat, identifier : StrictStr, boundingbox : StrictStr, gridbasecrs : StrictStr, gridorigin : Optional[StrictStr] = None, gridoffsets : Optional[StrictStr] = None, time : Optional[Any] = None, resx : Optional[Union[StrictFloat, StrictInt]] = None, resy : Optional[Union[StrictFloat, StrictInt]] = None, nodatavalue : Optional[Union[StrictFloat, StrictInt]] = None, **kwargs) -> bytearray:  # noqa: E501
        """Get WCS Coverage  # noqa: E501

        Get WCS Coverage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_get_coverage_handler(workflow, version, service, request, format, identifier, boundingbox, gridbasecrs, gridorigin, gridoffsets, time, resx, resy, nodatavalue, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param version: (required)
        :type version: WcsVersion
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: GetCoverageRequest
        :param format: (required)
        :type format: GetCoverageFormat
        :param identifier: (required)
        :type identifier: str
        :param boundingbox: (required)
        :type boundingbox: str
        :param gridbasecrs: (required)
        :type gridbasecrs: str
        :param gridorigin:
        :type gridorigin: str
        :param gridoffsets:
        :type gridoffsets: str
        :param time:
        :type time: str
        :param resx:
        :type resx: float
        :param resy:
        :type resy: float
        :param nodatavalue:
        :type nodatavalue: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the wcs_get_coverage_handler_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.wcs_get_coverage_handler_with_http_info(workflow, version, service, request, format, identifier, boundingbox, gridbasecrs, gridorigin, gridoffsets, time, resx, resy, nodatavalue, **kwargs)  # noqa: E501

    @validate_arguments
    def wcs_get_coverage_handler_with_http_info(self, workflow : Annotated[StrictStr, Field(..., description="Workflow id")], version : WcsVersion, service : WcsService, request : GetCoverageRequest, format : GetCoverageFormat, identifier : StrictStr, boundingbox : StrictStr, gridbasecrs : StrictStr, gridorigin : Optional[StrictStr] = None, gridoffsets : Optional[StrictStr] = None, time : Optional[Any] = None, resx : Optional[Union[StrictFloat, StrictInt]] = None, resy : Optional[Union[StrictFloat, StrictInt]] = None, nodatavalue : Optional[Union[StrictFloat, StrictInt]] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get WCS Coverage  # noqa: E501

        Get WCS Coverage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.wcs_get_coverage_handler_with_http_info(workflow, version, service, request, format, identifier, boundingbox, gridbasecrs, gridorigin, gridoffsets, time, resx, resy, nodatavalue, async_req=True)
        >>> result = thread.get()

        :param workflow: Workflow id (required)
        :type workflow: str
        :param version: (required)
        :type version: WcsVersion
        :param service: (required)
        :type service: WcsService
        :param request: (required)
        :type request: GetCoverageRequest
        :param format: (required)
        :type format: GetCoverageFormat
        :param identifier: (required)
        :type identifier: str
        :param boundingbox: (required)
        :type boundingbox: str
        :param gridbasecrs: (required)
        :type gridbasecrs: str
        :param gridorigin:
        :type gridorigin: str
        :param gridoffsets:
        :type gridoffsets: str
        :param time:
        :type time: str
        :param resx:
        :type resx: float
        :param resy:
        :type resy: float
        :param nodatavalue:
        :type nodatavalue: float
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
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'workflow',
            'version',
            'service',
            'request',
            'format',
            'identifier',
            'boundingbox',
            'gridbasecrs',
            'gridorigin',
            'gridoffsets',
            'time',
            'resx',
            'resy',
            'nodatavalue'
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
                    " to method wcs_get_coverage_handler" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['workflow']:
            _path_params['workflow'] = _params['workflow']


        # process the query parameters
        _query_params = []
        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version'].value))

        if _params.get('service') is not None:  # noqa: E501
            _query_params.append(('service', _params['service'].value))

        if _params.get('request') is not None:  # noqa: E501
            _query_params.append(('request', _params['request'].value))

        if _params.get('format') is not None:  # noqa: E501
            _query_params.append(('format', _params['format'].value))

        if _params.get('identifier') is not None:  # noqa: E501
            _query_params.append(('identifier', _params['identifier']))

        if _params.get('boundingbox') is not None:  # noqa: E501
            _query_params.append(('boundingbox', _params['boundingbox']))

        if _params.get('gridbasecrs') is not None:  # noqa: E501
            _query_params.append(('gridbasecrs', _params['gridbasecrs']))

        if _params.get('gridorigin') is not None:  # noqa: E501
            _query_params.append(('gridorigin', _params['gridorigin']))

        if _params.get('gridoffsets') is not None:  # noqa: E501
            _query_params.append(('gridoffsets', _params['gridoffsets']))

        if _params.get('time') is not None:  # noqa: E501
            _query_params.append(('time', _params['time']))

        if _params.get('resx') is not None:  # noqa: E501
            _query_params.append(('resx', _params['resx']))

        if _params.get('resy') is not None:  # noqa: E501
            _query_params.append(('resy', _params['resy']))

        if _params.get('nodatavalue') is not None:  # noqa: E501
            _query_params.append(('nodatavalue', _params['nodatavalue']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['image/png'])  # noqa: E501

        # authentication setting
        _auth_settings = ['session_token']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/wcs/{workflow}?request=GetCoverage', 'GET',
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
