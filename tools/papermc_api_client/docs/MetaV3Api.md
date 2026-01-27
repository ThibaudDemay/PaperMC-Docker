# papermc_api_client.MetaV3Api

All URIs are relative to *https://fill.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build**](MetaV3Api.md#get_build) | **GET** /v3/projects/{project}/versions/{version}/builds/{build} | Get details of a specific build for a version of a project
[**get_builds**](MetaV3Api.md#get_builds) | **GET** /v3/projects/{project}/versions/{version}/builds | Get a list of builds for a specific version of a project
[**get_latest_build**](MetaV3Api.md#get_latest_build) | **GET** /v3/projects/{project}/versions/{version}/builds/latest | Get details of the latest build for a version of a project
[**get_project**](MetaV3Api.md#get_project) | **GET** /v3/projects/{project} | Get details of a specific project
[**get_projects**](MetaV3Api.md#get_projects) | **GET** /v3/projects | Get a list of all projects
[**get_version**](MetaV3Api.md#get_version) | **GET** /v3/projects/{project}/versions/{version} | Get details of a specific version for a project
[**get_versions**](MetaV3Api.md#get_versions) | **GET** /v3/projects/{project}/versions | Get a list of versions for a specific project


# **get_build**
> BuildResponse get_build(project, version, build)

Get details of a specific build for a version of a project

### Example


```python
import papermc_api_client
from papermc_api_client.models.build_response import BuildResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project
    version = 'version_example' # str | The key of the version
    build = 56 # int | The number of the build

    try:
        # Get details of a specific build for a version of a project
        api_response = api_instance.get_build(project, version, build)
        print("The response of MetaV3Api->get_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 
 **version** | **str**| The key of the version | 
 **build** | **int**| The number of the build | 

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> List[BuildResponse] get_builds(project, version, channel=channel)

Get a list of builds for a specific version of a project

### Example


```python
import papermc_api_client
from papermc_api_client.models.build_response import BuildResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project
    version = 'version_example' # str | The key of the version
    channel = ['channel_example'] # List[str] | Filter builds by one or more channels (optional)

    try:
        # Get a list of builds for a specific version of a project
        api_response = api_instance.get_builds(project, version, channel=channel)
        print("The response of MetaV3Api->get_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 
 **version** | **str**| The key of the version | 
 **channel** | [**List[str]**](str.md)| Filter builds by one or more channels | [optional] 

### Return type

[**List[BuildResponse]**](BuildResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_build**
> BuildResponse get_latest_build(project, version)

Get details of the latest build for a version of a project

### Example


```python
import papermc_api_client
from papermc_api_client.models.build_response import BuildResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project
    version = 'version_example' # str | The key of the version

    try:
        # Get details of the latest build for a version of a project
        api_response = api_instance.get_latest_build(project, version)
        print("The response of MetaV3Api->get_latest_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_latest_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 
 **version** | **str**| The key of the version | 

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectResponse get_project(project)

Get details of a specific project

### Example


```python
import papermc_api_client
from papermc_api_client.models.project_response import ProjectResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project

    try:
        # Get details of a specific project
        api_response = api_instance.get_project(project)
        print("The response of MetaV3Api->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> ProjectsResponse get_projects()

Get a list of all projects

### Example


```python
import papermc_api_client
from papermc_api_client.models.projects_response import ProjectsResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)

    try:
        # Get a list of all projects
        api_response = api_instance.get_projects()
        print("The response of MetaV3Api->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectsResponse**](ProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionResponse get_version(project, version)

Get details of a specific version for a project

### Example


```python
import papermc_api_client
from papermc_api_client.models.version_response import VersionResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project
    version = 'version_example' # str | The key of the version

    try:
        # Get details of a specific version for a project
        api_response = api_instance.get_version(project, version)
        print("The response of MetaV3Api->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 
 **version** | **str**| The key of the version | 

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> VersionsResponse get_versions(project)

Get a list of versions for a specific project

### Example


```python
import papermc_api_client
from papermc_api_client.models.versions_response import VersionsResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fill.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.MetaV3Api(api_client)
    project = 'project_example' # str | The key of the project

    try:
        # Get a list of versions for a specific project
        api_response = api_instance.get_versions(project)
        print("The response of MetaV3Api->get_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV3Api->get_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The key of the project | 

### Return type

[**VersionsResponse**](VersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

