# VersionBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**channel** | **str** |  | [optional] 
**promoted** | **bool** |  | [optional] 
**changes** | [**List[Change]**](Change.md) |  | [optional] 
**downloads** | [**Dict[str, Download]**](Download.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.version_build import VersionBuild

# TODO update the JSON string below
json = "{}"
# create an instance of VersionBuild from a JSON string
version_build_instance = VersionBuild.from_json(json)
# print the JSON string representation of the object
print(VersionBuild.to_json())

# convert the object into a dict
version_build_dict = version_build_instance.to_dict()
# create an instance of VersionBuild from a dict
version_build_from_dict = VersionBuild.from_dict(version_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


