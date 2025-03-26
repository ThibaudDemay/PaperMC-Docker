# papermc_api_client.VersionControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](VersionControllerApi.md#version) | **GET** /v2/projects/{project}/versions/{version} | Gets information about a version.


# **version**
> VersionResponse version(project, version)

Gets information about a version.

### Example


```python
import papermc_api_client
from papermc_api_client.models.version_response import VersionResponse
from papermc_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.papermc.io
# See configuration.py for a list of all supported configuration parameters.
configuration = papermc_api_client.Configuration(
    host = "https://api.papermc.io"
)


# Enter a context with an instance of the API client
with papermc_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = papermc_api_client.VersionControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    version = 'version_example' # str | A version of the project.

    try:
        # Gets information about a version.
        api_response = api_instance.version(project, version)
        print("The response of VersionControllerApi->version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionControllerApi->version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **version** | **str**| A version of the project. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

