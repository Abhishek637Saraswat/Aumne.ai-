# coding: utf-8

"""
    Flight Booking System

    Book and manage flight tickets

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flight_sdk.models.flight_create import FlightCreate

class TestFlightCreate(unittest.TestCase):
    """FlightCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlightCreate:
        """Test FlightCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlightCreate`
        """
        model = FlightCreate()
        if include_optional:
            return FlightCreate(
                flight_number = '',
                airline = '',
                departure = '',
                destination = '',
                departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total_seats = 56
            )
        else:
            return FlightCreate(
                flight_number = '',
                airline = '',
                departure = '',
                destination = '',
                departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total_seats = 56,
        )
        """

    def testFlightCreate(self):
        """Test FlightCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
