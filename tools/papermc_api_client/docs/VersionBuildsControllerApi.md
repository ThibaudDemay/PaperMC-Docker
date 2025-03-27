# papermc_api_client.VersionBuildsControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**builds**](VersionBuildsControllerApi.md#builds) | **GET** /v2/projects/{project}/versions/{version}/builds | Gets all available builds for a project&#39;s version.


# **builds**
> BuildsResponse builds(project, version)

Gets all available builds for a project's version.

### Example


```python
import papermc_api_client
from papermc_api_client.models.builds_response import BuildsResponse
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
    api_instance = papermc_api_client.VersionBuildsControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    version = 'version_example' # str | A version of the project.

    try:
        # Gets all available builds for a project's version.
        api_response = api_instance.builds(project, version)
        print("The response of VersionBuildsControllerApi->builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionBuildsControllerApi->builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **version** | **str**| A version of the project. | 

### Return type

[**BuildsResponse**](BuildsResponse.md)

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

