# BuildsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**builds** | [**List[VersionBuild]**](VersionBuild.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.builds_response import BuildsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuildsResponse from a JSON string
builds_response_instance = BuildsResponse.from_json(json)
# print the JSON string representation of the object
print(BuildsResponse.to_json())

# convert the object into a dict
builds_response_dict = builds_response_instance.to_dict()
# create an instance of BuildsResponse from a dict
builds_response_from_dict = BuildsResponse.from_dict(builds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


