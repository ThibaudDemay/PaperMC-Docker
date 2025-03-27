# VersionFamilyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**version_group** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from papermc_api_client.models.version_family_response import VersionFamilyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionFamilyResponse from a JSON string
version_family_response_instance = VersionFamilyResponse.from_json(json)
# print the JSON string representation of the object
print(VersionFamilyResponse.to_json())

# convert the object into a dict
version_family_response_dict = version_family_response_instance.to_dict()
# create an instance of VersionFamilyResponse from a dict
version_family_response_from_dict = VersionFamilyResponse.from_dict(version_family_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


