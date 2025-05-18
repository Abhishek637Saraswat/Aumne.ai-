# FlightOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flight_number** | **str** |  | 
**airline** | **str** |  | 
**departure** | **str** |  | 
**destination** | **str** |  | 
**departure_time** | **datetime** |  | 
**total_seats** | **int** |  | 
**id** | **int** |  | 
**available_seats** | **int** |  | 

## Example

```python
from flight_sdk.models.flight_out import FlightOut

# TODO update the JSON string below
json = "{}"
# create an instance of FlightOut from a JSON string
flight_out_instance = FlightOut.from_json(json)
# print the JSON string representation of the object
print(FlightOut.to_json())

# convert the object into a dict
flight_out_dict = flight_out_instance.to_dict()
# create an instance of FlightOut from a dict
flight_out_from_dict = FlightOut.from_dict(flight_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


