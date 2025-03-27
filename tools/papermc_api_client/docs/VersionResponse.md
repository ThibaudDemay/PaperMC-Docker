# VersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**builds** | **List[int]** |  | [optional] 

## Example

```python
from papermc_api_client.models.version_response import VersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionResponse from a JSON string
version_response_instance = VersionResponse.from_json(json)
# print the JSON string representation of the object
print(VersionResponse.to_json())

# convert the object into a dict
version_response_dict = version_response_instance.to_dict()
# create an instance of VersionResponse from a dict
version_response_from_dict = VersionResponse.from_dict(version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


