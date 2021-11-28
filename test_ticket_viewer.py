import unittest
from unittest.mock import patch
from ticket_viewer import view_tickets, view_ticket_by_id           # Only import the view_tickets and view_ticket_by_id functions to test them

# auth: ("mohamadalabudi42@gmail.com/token", "bvJwx9uKm6ieRuYv0P0jmA7YojKhwfBUYmbSV1jx")

class Test_Ticket_Viewer(unittest.TestCase):

    # Define/Setup variables useful for unit testing
    def setUp(self):
        print("\nSet up\n")

        # Set up the auth tuple for authentication when sending get requests to the API
        self.auth = ("mohamadalabudi42@gmail.com/token", "bvJwx9uKm6ieRuYv0P0jmA7YojKhwfBUYmbSV1jx")


    # Tear the variable(s) in set up after unit testing
    def tearDown(self):
        print("\nTear down\n")


    # Test the view_ticket_by_id function to make sure that the code can fetch a ticket with a valid ticket ID
    def test_view_ticket_by_id(self):
        with patch("ticket_viewer.requests.get") as mocked_get:

            # -----Test Valid ticket ID URL-----
            mocked_get.return_value.ok = True

            # The return value or response of the view_ticket_by_id function
            ticket = view_ticket_by_id('2112', self.auth)

            # make sure the get request was called with the correct url
            mocked_get.assert_called_with("https://zccmalabudi5807.zendesk.com/api/v2/requests/2112", auth = self.auth)

            # Display the string that the function returns
            print(ticket)

            # Check if the output is what we expect with the unit test
            self.assertEqual(ticket, "Success")


            # -----Test Invalid ticket ID URL (numerical ID, ticket ID 1 is invalid because it has been deleted and can no longer be accessed)------
            mocked_get.return_value.ok = False

            ticket = view_ticket_by_id('1', self.auth)

            # make sure the get request was called with the bad url
            mocked_get.assert_called_with("https://zccmalabudi5807.zendesk.com/api/v2/requests/1", auth = self.auth)

            print(ticket)

            self.assertEqual(ticket, "Bad response")


            # -----Test Invalid ticket ID URL (non-numerical user input)-----
            mocked_get.return_value.ok = False

            ticket = view_ticket_by_id("abc", self.auth)

            # make sure the get request was called with the bad url
            mocked_get.assert_called_with("https://zccmalabudi5807.zendesk.com/api/v2/requests/abc", auth = self.auth)

            print(ticket)

            self.assertEqual(ticket, "Bad response")
    

    # Test the view_tickets function to make sure that we use the correct URL for fetching all tickets
    def test_view_tickets(self):

        # patch used as a context manager that mocks a get request
        with patch("ticket_viewer.requests.get") as mocked_get:

            #-----Test Valid URL-----
            mocked_get.return_value.ok = True

            # The return value or response of the view_tickets function
            ticket = view_tickets(self.auth)

            # make sure the get request was called with the correct url
            mocked_get.assert_called_with("https://zccmalabudi5807.zendesk.com/api/v2/requests/", auth = self.auth)

            # Print the string that the test functions returns
            print(ticket)

            # Check if the output is what we expect with the unit test
            self.assertEqual(ticket, "Success")



if __name__ == '__main__':
    unittest.main()