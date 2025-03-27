# papermc_api_client.DownloadControllerApi

All URIs are relative to *https://api.papermc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](DownloadControllerApi.md#download) | **GET** /v2/projects/{project}/versions/{version}/builds/{build}/downloads/{download} | Downloads the given file from a build&#39;s data.


# **download**
> object download(project, version, build, download)

Downloads the given file from a build's data.

### Example


```python
import papermc_api_client
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
    api_instance = papermc_api_client.DownloadControllerApi(api_client)
    project = 'paper' # str | The project identifier.
    version = 'version_example' # str | A version of the project.
    build = 56 # int | A build of the version.
    download = 'download_example' # str | A download of the build.

    try:
        # Downloads the given file from a build's data.
        api_response = api_instance.download(project, version, build, download)
        print("The response of DownloadControllerApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadControllerApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project identifier. | 
 **version** | **str**| A version of the project. | 
 **build** | **int**| A build of the version. | 
 **download** | **str**| A download of the build. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/java-archive

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * ETag - An identifier for a specific version of a resource. It lets caches be more efficient and save bandwidth, as a web server does not need to resend a full response if the content has not changed. <br>  * Content-Disposition - A header indicating that the content is expected to be displayed as an attachment, that is downloaded and saved locally. <br>  * Last-Modified - The date and time at which the origin server believes the resource was last modified. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

