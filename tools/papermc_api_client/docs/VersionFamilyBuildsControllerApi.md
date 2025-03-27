# papermc_api_client.VersionFamilyBuildsControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**family_builds**](VersionFamilyBuildsControllerApi.md#family_builds) | **GET** /v2/projects/{project}/version_group/{family}/builds | Gets all available builds for a project&#39;s version group.


# **family_builds**
> VersionFamilyBuildsResponse family_builds(project, family)

Gets all available builds for a project's version group.

### Example


```python
import papermc_api_client
from papermc_api_client.models.version_family_builds_response import VersionFamilyBuildsResponse
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
    api_instance = papermc_api_client.VersionFamilyBuildsControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    family = 'family_example' # str | The version group name.

    try:
        # Gets all available builds for a project's version group.
        api_response = api_instance.family_builds(project, family)
        print("The response of VersionFamilyBuildsControllerApi->family_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionFamilyBuildsControllerApi->family_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **family** | **str**| The version group name. | 

### Return type

[**VersionFamilyBuildsResponse**](VersionFamilyBuildsResponse.md)

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

