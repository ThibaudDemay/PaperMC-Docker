# Java


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**JavaFlags**](JavaFlags.md) |  | [optional] 
**version** | [**JavaVersion**](JavaVersion.md) |  | [optional] 

## Example

```python
from papermc_api_client.models.java import Java

# TODO update the JSON string below
json = "{}"
# create an instance of Java from a JSON string
java_instance = Java.from_json(json)
# print the JSON string representation of the object
print(Java.to_json())

# convert the object into a dict
java_dict = java_instance.to_dict()
# create an instance of Java from a dict
java_from_dict = Java.from_dict(java_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


