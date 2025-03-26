# papermc_api_client.ProjectControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project**](ProjectControllerApi.md#project) | **GET** /v2/projects/{project} | Gets information about a project.


# **project**
> ProjectResponse project(project)

Gets information about a project.

### Example


```python
import papermc_api_client
from papermc_api_client.models.project_response import ProjectResponse
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
    api_instance = papermc_api_client.ProjectControllerApi(api_client)
    project = 'paper' # str | The project identifier.

    try:
        # Gets information about a project.
        api_response = api_instance.project(project)
        print("The response of ProjectControllerApi->project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectControllerApi->project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

