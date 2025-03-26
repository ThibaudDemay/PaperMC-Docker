# papermc_api_client.VersionBuildControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build**](VersionBuildControllerApi.md#build) | **GET** /v2/projects/{project}/versions/{version}/builds/{build} | Gets information related to a specific build.


# **build**
> BuildResponse build(project, version, build)

Gets information related to a specific build.

### Example


```python
import papermc_api_client
from papermc_api_client.models.build_response import BuildResponse
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
    api_instance = papermc_api_client.VersionBuildControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    version = 'version_example' # str | A version of the project.
    build = 56 # int | A build of the version.

    try:
        # Gets information related to a specific build.
        api_response = api_instance.build(project, version, build)
        print("The response of VersionBuildControllerApi->build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionBuildControllerApi->build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **version** | **str**| A version of the project. | 
 **build** | **int**| A build of the version. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

