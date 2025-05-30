# coding: utf-8

"""
    Flight Booking System

    Book and manage flight tickets

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flight_sdk.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_book_flight_flights_flight_id_book_post(self) -> None:
        """Test case for book_flight_flights_flight_id_book_post

        Book Flight
        """
        pass

    def test_cancel_booking_bookings_booking_id_delete(self) -> None:
        """Test case for cancel_booking_bookings_booking_id_delete

        Cancel Booking
        """
        pass

    def test_create_flight_flights_post(self) -> None:
        """Test case for create_flight_flights_post

        Create Flight
        """
        pass

    def test_get_flight_flights_flight_id_get(self) -> None:
        """Test case for get_flight_flights_flight_id_get

        Get Flight
        """
        pass

    def test_get_flights_flights_get(self) -> None:
        """Test case for get_flights_flights_get

        Get Flights
        """
        pass


if __name__ == '__main__':
    unittest.main()
