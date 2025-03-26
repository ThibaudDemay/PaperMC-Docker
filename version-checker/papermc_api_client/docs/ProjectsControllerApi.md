# papermc_api_client.ProjectsControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects**](ProjectsControllerApi.md#projects) | **GET** /v2/projects | Gets a list of all available projects.


# **projects**
> ProjectsResponse projects()

Gets a list of all available projects.

### Example


```python
import papermc_api_client
from papermc_api_client.models.projects_response import ProjectsResponse
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
    api_instance = papermc_api_client.ProjectsControllerApi(api_client)

    try:
        # Gets a list of all available projects.
        api_response = api_instance.projects()
        print("The response of ProjectsControllerApi->projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsControllerApi->projects: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

