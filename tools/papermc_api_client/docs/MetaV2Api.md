# papermc_api_client.MetaV2Api

All URIs are relative to *https://fill.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_family**](MetaV2Api.md#get_family) | **GET** /v2/projects/{project}/version_group/{family} | 
[**get_family_builds**](MetaV2Api.md#get_family_builds) | **GET** /v2/projects/{project}/version_group/{family}/builds | 
[**get_project1**](MetaV2Api.md#get_project1) | **GET** /v2/projects/{project} | 
[**get_projects1**](MetaV2Api.md#get_projects1) | **GET** /v2/projects | 
[**get_version1**](MetaV2Api.md#get_version1) | **GET** /v2/projects/{project}/versions/{version} | 
[**get_version_build**](MetaV2Api.md#get_version_build) | **GET** /v2/projects/{project}/versions/{version}/builds/{build} | 
[**get_version_builds**](MetaV2Api.md#get_version_builds) | **GET** /v2/projects/{project}/versions/{version}/builds | 


# **get_family**
> object get_family(project, family)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 
    family = 'family_example' # str | 

    try:
        api_response = api_instance.get_family(project, family)
        print("The response of MetaV2Api->get_family:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_family: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **family** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_family_builds**
> object get_family_builds(project, family)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 
    family = 'family_example' # str | 

    try:
        api_response = api_instance.get_family_builds(project, family)
        print("The response of MetaV2Api->get_family_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_family_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **family** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project1**
> object get_project1(project)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 

    try:
        api_response = api_instance.get_project1(project)
        print("The response of MetaV2Api->get_project1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_project1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects1**
> object get_projects1()

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)

    try:
        api_response = api_instance.get_projects1()
        print("The response of MetaV2Api->get_projects1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_projects1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version1**
> object get_version1(project, version)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_version1(project, version)
        print("The response of MetaV2Api->get_version1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_version1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **version** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_build**
> object get_version_build(project, version, build)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 
    version = 'version_example' # str | 
    build = 56 # int | 

    try:
        api_response = api_instance.get_version_build(project, version, build)
        print("The response of MetaV2Api->get_version_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_version_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **version** | **str**|  | 
 **build** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_builds**
> object get_version_builds(project, version)

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.MetaV2Api(api_client)
    project = 'project_example' # str | 
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_version_builds(project, version)
        print("The response of MetaV2Api->get_version_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaV2Api->get_version_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **version** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

