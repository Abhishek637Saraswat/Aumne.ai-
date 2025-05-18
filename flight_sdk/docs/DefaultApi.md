# flight_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_flight_flights_flight_id_book_post**](DefaultApi.md#book_flight_flights_flight_id_book_post) | **POST** /flights/{flight_id}/book | Book Flight
[**cancel_booking_bookings_booking_id_delete**](DefaultApi.md#cancel_booking_bookings_booking_id_delete) | **DELETE** /bookings/{booking_id} | Cancel Booking
[**create_flight_flights_post**](DefaultApi.md#create_flight_flights_post) | **POST** /flights/ | Create Flight
[**get_flight_flights_flight_id_get**](DefaultApi.md#get_flight_flights_flight_id_get) | **GET** /flights/{flight_id} | Get Flight
[**get_flights_flights_get**](DefaultApi.md#get_flights_flights_get) | **GET** /flights/ | Get Flights


# **book_flight_flights_flight_id_book_post**
> BookingOut book_flight_flights_flight_id_book_post(flight_id, booking_create)

Book Flight

### Example


```python
import flight_sdk
from flight_sdk.models.booking_create import BookingCreate
from flight_sdk.models.booking_out import BookingOut
from flight_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flight_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flight_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flight_sdk.DefaultApi(api_client)
    flight_id = 56 # int | 
    booking_create = flight_sdk.BookingCreate() # BookingCreate | 

    try:
        # Book Flight
        api_response = api_instance.book_flight_flights_flight_id_book_post(flight_id, booking_create)
        print("The response of DefaultApi->book_flight_flights_flight_id_book_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->book_flight_flights_flight_id_book_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flight_id** | **int**|  | 
 **booking_create** | [**BookingCreate**](BookingCreate.md)|  | 

### Return type

[**BookingOut**](BookingOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_booking_bookings_booking_id_delete**
> object cancel_booking_bookings_booking_id_delete(booking_id)

Cancel Booking

### Example


```python
import flight_sdk
from flight_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flight_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flight_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flight_sdk.DefaultApi(api_client)
    booking_id = 56 # int | 

    try:
        # Cancel Booking
        api_response = api_instance.cancel_booking_bookings_booking_id_delete(booking_id)
        print("The response of DefaultApi->cancel_booking_bookings_booking_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_booking_bookings_booking_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flight_flights_post**
> FlightOut create_flight_flights_post(flight_create)

Create Flight

### Example


```python
import flight_sdk
from flight_sdk.models.flight_create import FlightCreate
from flight_sdk.models.flight_out import FlightOut
from flight_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flight_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flight_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flight_sdk.DefaultApi(api_client)
    flight_create = flight_sdk.FlightCreate() # FlightCreate | 

    try:
        # Create Flight
        api_response = api_instance.create_flight_flights_post(flight_create)
        print("The response of DefaultApi->create_flight_flights_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_flight_flights_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flight_create** | [**FlightCreate**](FlightCreate.md)|  | 

### Return type

[**FlightOut**](FlightOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flight_flights_flight_id_get**
> FlightOut get_flight_flights_flight_id_get(flight_id)

Get Flight

### Example


```python
import flight_sdk
from flight_sdk.models.flight_out import FlightOut
from flight_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flight_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flight_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flight_sdk.DefaultApi(api_client)
    flight_id = 56 # int | 

    try:
        # Get Flight
        api_response = api_instance.get_flight_flights_flight_id_get(flight_id)
        print("The response of DefaultApi->get_flight_flights_flight_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_flight_flights_flight_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flight_id** | **int**|  | 

### Return type

[**FlightOut**](FlightOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flights_flights_get**
> List[FlightOut] get_flights_flights_get()

Get Flights

### Example


```python
import flight_sdk
from flight_sdk.models.flight_out import FlightOut
from flight_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flight_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flight_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flight_sdk.DefaultApi(api_client)

    try:
        # Get Flights
        api_response = api_instance.get_flights_flights_get()
        print("The response of DefaultApi->get_flights_flights_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_flights_flights_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FlightOut]**](FlightOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

