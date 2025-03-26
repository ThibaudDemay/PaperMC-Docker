# Change


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from papermc_api_client.models.change import Change

# TODO update the JSON string below
json = "{}"
# create an instance of Change from a JSON string
change_instance = Change.from_json(json)
# print the JSON string representation of the object
print(Change.to_json())

# convert the object into a dict
change_dict = change_instance.to_dict()
# create an instance of Change from a dict
change_from_dict = Change.from_dict(change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


