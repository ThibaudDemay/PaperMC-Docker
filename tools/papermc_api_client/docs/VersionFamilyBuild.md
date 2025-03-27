# VersionFamilyBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**build** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**channel** | **str** |  | [optional] 
**promoted** | **bool** |  | [optional] 
**changes** | [**List[Change]**](Change.md) |  | [optional] 
**downloads** | [**Dict[str, Download]**](Download.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.version_family_build import VersionFamilyBuild

# TODO update the JSON string below
json = "{}"
# create an instance of VersionFamilyBuild from a JSON string
version_family_build_instance = VersionFamilyBuild.from_json(json)
# print the JSON string representation of the object
print(VersionFamilyBuild.to_json())

# convert the object into a dict
version_family_build_dict = version_family_build_instance.to_dict()
# create an instance of VersionFamilyBuild from a dict
version_family_build_from_dict = VersionFamilyBuild.from_dict(version_family_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


