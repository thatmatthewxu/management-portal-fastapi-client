<a name="__pageTop"></a>
# openapi_client.apis.tags.openstack_api.OpenstackApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_projects_and_quotas_api_openstack_quotas_all_get**](#get_all_projects_and_quotas_api_openstack_quotas_all_get) | **get** /api/openstack/quotas/all | Get All Projects And Quotas
[**get_all_projects_api_openstack_projects_all_get**](#get_all_projects_api_openstack_projects_all_get) | **get** /api/openstack/projects/all | Get All Projects
[**get_project_by_name_or_id_api_openstack_project_get**](#get_project_by_name_or_id_api_openstack_project_get) | **get** /api/openstack/project | Get Project By Name Or Id
[**get_project_quotas_by_name_or_id_api_openstack_quotas_get**](#get_project_quotas_by_name_or_id_api_openstack_quotas_get) | **get** /api/openstack/quotas | Get Project Quotas By Name Or Id

# **get_all_projects_and_quotas_api_openstack_quotas_all_get**
<a name="get_all_projects_and_quotas_api_openstack_quotas_all_get"></a>
> ProjectsQuotasResponse get_all_projects_and_quotas_api_openstack_quotas_all_get(cloud_name)

Get All Projects And Quotas

Return all the projects with the quotas

### Example

```python
import openapi_client
from openapi_client.apis.tags import openstack_api
from openapi_client.model.projects_quotas_response import ProjectsQuotasResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openstack_api.OpenstackApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'cloud_name': "cloud_name_example",
    }
    try:
        # Get All Projects And Quotas
        api_response = api_instance.get_all_projects_and_quotas_api_openstack_quotas_all_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenstackApi->get_all_projects_and_quotas_api_openstack_quotas_all_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cloud_name | CloudNameSchema | | 


# CloudNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_projects_and_quotas_api_openstack_quotas_all_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_all_projects_and_quotas_api_openstack_quotas_all_get.ApiResponseFor422) | Validation Error

#### get_all_projects_and_quotas_api_openstack_quotas_all_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectsQuotasResponse**](../../models/ProjectsQuotasResponse.md) |  | 


#### get_all_projects_and_quotas_api_openstack_quotas_all_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_projects_api_openstack_projects_all_get**
<a name="get_all_projects_api_openstack_projects_all_get"></a>
> ProjectsResponse get_all_projects_api_openstack_projects_all_get(cloud_name)

Get All Projects

Return the detail of all the projects

### Example

```python
import openapi_client
from openapi_client.apis.tags import openstack_api
from openapi_client.model.projects_response import ProjectsResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openstack_api.OpenstackApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'cloud_name': "cloud_name_example",
    }
    try:
        # Get All Projects
        api_response = api_instance.get_all_projects_api_openstack_projects_all_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenstackApi->get_all_projects_api_openstack_projects_all_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cloud_name | CloudNameSchema | | 


# CloudNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_projects_api_openstack_projects_all_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_all_projects_api_openstack_projects_all_get.ApiResponseFor422) | Validation Error

#### get_all_projects_api_openstack_projects_all_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectsResponse**](../../models/ProjectsResponse.md) |  | 


#### get_all_projects_api_openstack_projects_all_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_by_name_or_id_api_openstack_project_get**
<a name="get_project_by_name_or_id_api_openstack_project_get"></a>
> ProjectResponse get_project_by_name_or_id_api_openstack_project_get(cloud_nameproject_name_or_id)

Get Project By Name Or Id

Return the detail of a project by project name or id

### Example

```python
import openapi_client
from openapi_client.apis.tags import openstack_api
from openapi_client.model.project_response import ProjectResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openstack_api.OpenstackApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'cloud_name': "cloud_name_example",
        'project_name_or_id': "project_name_or_id_example",
    }
    try:
        # Get Project By Name Or Id
        api_response = api_instance.get_project_by_name_or_id_api_openstack_project_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenstackApi->get_project_by_name_or_id_api_openstack_project_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cloud_name | CloudNameSchema | | 
project_name_or_id | ProjectNameOrIdSchema | | 


# CloudNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectNameOrIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_by_name_or_id_api_openstack_project_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_project_by_name_or_id_api_openstack_project_get.ApiResponseFor422) | Validation Error

#### get_project_by_name_or_id_api_openstack_project_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectResponse**](../../models/ProjectResponse.md) |  | 


#### get_project_by_name_or_id_api_openstack_project_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_quotas_by_name_or_id_api_openstack_quotas_get**
<a name="get_project_quotas_by_name_or_id_api_openstack_quotas_get"></a>
> ProjectQuotasResponse get_project_quotas_by_name_or_id_api_openstack_quotas_get(cloud_nameproject_name_or_id)

Get Project Quotas By Name Or Id

Return the quotas of a project by name or id

### Example

```python
import openapi_client
from openapi_client.apis.tags import openstack_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.project_quotas_response import ProjectQuotasResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openstack_api.OpenstackApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'cloud_name': "cloud_name_example",
        'project_name_or_id': "project_name_or_id_example",
    }
    try:
        # Get Project Quotas By Name Or Id
        api_response = api_instance.get_project_quotas_by_name_or_id_api_openstack_quotas_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenstackApi->get_project_quotas_by_name_or_id_api_openstack_quotas_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cloud_name | CloudNameSchema | | 
project_name_or_id | ProjectNameOrIdSchema | | 


# CloudNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectNameOrIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_quotas_by_name_or_id_api_openstack_quotas_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_project_quotas_by_name_or_id_api_openstack_quotas_get.ApiResponseFor422) | Validation Error

#### get_project_quotas_by_name_or_id_api_openstack_quotas_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectQuotasResponse**](../../models/ProjectQuotasResponse.md) |  | 


#### get_project_quotas_by_name_or_id_api_openstack_quotas_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

