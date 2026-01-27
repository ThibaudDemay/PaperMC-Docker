# Support


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **date** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from papermc_api_client.models.support import Support

# TODO update the JSON string below
json = "{}"
# create an instance of Support from a JSON string
support_instance = Support.from_json(json)
# print the JSON string representation of the object
print(Support.to_json())

# convert the object into a dict
support_dict = support_instance.to_dict()
# create an instance of Support from a dict
support_from_dict = Support.from_dict(support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


