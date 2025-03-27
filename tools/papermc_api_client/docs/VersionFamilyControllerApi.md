# papermc_api_client.VersionFamilyControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**family**](VersionFamilyControllerApi.md#family) | **GET** /v2/projects/{project}/version_group/{family} | Gets information about a project&#39;s version group.


# **family**
> VersionFamilyResponse family(project, family)

Gets information about a project's version group.

### Example


```python
import papermc_api_client
from papermc_api_client.models.version_family_response import VersionFamilyResponse
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
    api_instance = papermc_api_client.VersionFamilyControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    family = 'family_example' # str | The version group name.

    try:
        # Gets information about a project's version group.
        api_response = api_instance.family(project, family)
        print("The response of VersionFamilyControllerApi->family:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionFamilyControllerApi->family: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **family** | **str**| The version group name. | 

### Return type

[**VersionFamilyResponse**](VersionFamilyResponse.md)

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

