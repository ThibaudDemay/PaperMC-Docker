# BuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**channel** | **str** |  | [optional] 
**promoted** | **bool** |  | [optional] 
**changes** | [**List[Change]**](Change.md) |  | [optional] 
**downloads** | [**Dict[str, Download]**](Download.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.build_response import BuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuildResponse from a JSON string
build_response_instance = BuildResponse.from_json(json)
# print the JSON string representation of the object
print(BuildResponse.to_json())

# convert the object into a dict
build_response_dict = build_response_instance.to_dict()
# create an instance of BuildResponse from a dict
build_response_from_dict = BuildResponse.from_dict(build_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


