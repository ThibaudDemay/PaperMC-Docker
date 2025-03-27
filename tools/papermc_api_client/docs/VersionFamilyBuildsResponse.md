# VersionFamilyBuildsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**version_group** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 
**builds** | [**List[VersionFamilyBuild]**](VersionFamilyBuild.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.version_family_builds_response import VersionFamilyBuildsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionFamilyBuildsResponse from a JSON string
version_family_builds_response_instance = VersionFamilyBuildsResponse.from_json(json)
# print the JSON string representation of the object
print(VersionFamilyBuildsResponse.to_json())

# convert the object into a dict
version_family_builds_response_dict = version_family_builds_response_instance.to_dict()
# create an instance of VersionFamilyBuildsResponse from a dict
version_family_builds_response_from_dict = VersionFamilyBuildsResponse.from_dict(version_family_builds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


