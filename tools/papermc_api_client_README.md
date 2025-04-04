# papermc-api
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The `papermc_api_client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3, < 3.0.0
* python-dateutil >= 2.8.2
* pydantic >= 2
* typing-extensions >= 4.7.1

## Getting Started

In your own code, to use this library to connect and interact with papermc-api,
you can run the following:

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
    except ApiException as e:
        print("Exception when calling DownloadControllerApi->download: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.papermc.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DownloadControllerApi* | [**download**](papermc_api_client/docs/DownloadControllerApi.md#download) | **GET** /v2/projects/{project}/versions/{version}/builds/{build}/downloads/{download} | Downloads the given file from a build&#39;s data.
*ProjectControllerApi* | [**project**](papermc_api_client/docs/ProjectControllerApi.md#project) | **GET** /v2/projects/{project} | Gets information about a project.
*ProjectsControllerApi* | [**projects**](papermc_api_client/docs/ProjectsControllerApi.md#projects) | **GET** /v2/projects | Gets a list of all available projects.
*VersionBuildControllerApi* | [**build**](papermc_api_client/docs/VersionBuildControllerApi.md#build) | **GET** /v2/projects/{project}/versions/{version}/builds/{build} | Gets information related to a specific build.
*VersionBuildsControllerApi* | [**builds**](papermc_api_client/docs/VersionBuildsControllerApi.md#builds) | **GET** /v2/projects/{project}/versions/{version}/builds | Gets all available builds for a project&#39;s version.
*VersionControllerApi* | [**version**](papermc_api_client/docs/VersionControllerApi.md#version) | **GET** /v2/projects/{project}/versions/{version} | Gets information about a version.
*VersionFamilyBuildsControllerApi* | [**family_builds**](papermc_api_client/docs/VersionFamilyBuildsControllerApi.md#family_builds) | **GET** /v2/projects/{project}/version_group/{family}/builds | Gets all available builds for a project&#39;s version group.
*VersionFamilyControllerApi* | [**family**](papermc_api_client/docs/VersionFamilyControllerApi.md#family) | **GET** /v2/projects/{project}/version_group/{family} | Gets information about a project&#39;s version group.


## Documentation For Models

 - [BuildResponse](papermc_api_client/docs/BuildResponse.md)
 - [BuildsResponse](papermc_api_client/docs/BuildsResponse.md)
 - [Change](papermc_api_client/docs/Change.md)
 - [Download](papermc_api_client/docs/Download.md)
 - [ProjectResponse](papermc_api_client/docs/ProjectResponse.md)
 - [ProjectsResponse](papermc_api_client/docs/ProjectsResponse.md)
 - [VersionBuild](papermc_api_client/docs/VersionBuild.md)
 - [VersionFamilyBuild](papermc_api_client/docs/VersionFamilyBuild.md)
 - [VersionFamilyBuildsResponse](papermc_api_client/docs/VersionFamilyBuildsResponse.md)
 - [VersionFamilyResponse](papermc_api_client/docs/VersionFamilyResponse.md)
 - [VersionResponse](papermc_api_client/docs/VersionResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




