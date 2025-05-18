# BookingOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**passenger_name** | **str** |  | 
**passport_number** | **str** |  | 
**flight_id** | **int** |  | 
**is_cancelled** | **bool** |  | 

## Example

```python
from flight_sdk.models.booking_out import BookingOut

# TODO update the JSON string below
json = "{}"
# create an instance of BookingOut from a JSON string
booking_out_instance = BookingOut.from_json(json)
# print the JSON string representation of the object
print(BookingOut.to_json())

# convert the object into a dict
booking_out_dict = booking_out_instance.to_dict()
# create an instance of BookingOut from a dict
booking_out_from_dict = BookingOut.from_dict(booking_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


