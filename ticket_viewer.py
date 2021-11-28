import requests

#--------User defined functions-------------
def page_tickets(min, max, tickets_lst):
    """
    Based on what page the user is viewing in the tickets list, prompt them the respective option to view the next page, previous page, or exit the
    tickets viewer all together and return the user's choice to the view_tickets function
    """
    view_choice = ""

    # Ask the user if they want to see the next page of the list, go back to the previous page, or stop viewing tickets depending on what page the user is viewing in the if statement
    if min == 0:
        print("1 - Stop viewing tickets")
        print("2 - Next page")
        view_choice = input("")
        
        # Data validation
        while (view_choice != "1") and (view_choice != "2"):
            print("Invalid input! Please select from the following choices")

            print("1 - Stop viewing tickets")
            print("2 - Next page")
            view_choice = input("")

    elif max >= len(tickets_lst):
        print("1 - Stop viewing tickets")
        print("3 - Previous page")
        view_choice = input("")

        # Data validation
        while (view_choice != "1") and (view_choice != "3"):
            print("Invalid input! Please select from the following choices")

            print("1 - Stop viewing tickets")
            print("3 - Previous page")
            view_choice = input("")
    else:
        print("1 - Stop viewing tickets")
        print("2 - Next page")
        print("3 - Previous page")
        view_choice = input("")

        # Data validation
        while (view_choice != "1") and (view_choice != "2") and (view_choice != "3"):
            print("Invalid input! Please select from the following choices")

            print("1 - Stop viewing tickets")
            print("2 - Next page")
            print("3 - Previous page")
            view_choice = input("")

    return view_choice


def view_tickets(auth):
    """
    View all tickets in the account, if there are more than 25 tickets, begin paging
    through the tickets in the account
    """
    # loop control variables to handle paging through an amount of tickets greater than 25
    min = 0
    max = 25
    view_choice = ""

    print("Fetching tickets...")

    # Fetch tickets from the API
    try:
        response = requests.get("https://zccmalabudi5807.zendesk.com/api/v2/requests/", auth=auth)

        # The requests list is a list of ticket dictionaries/hash maps fetched from the API
        requests_lst = response.json()["requests"]

    # Let the user know if a problem occurs with fetching the tickets then exit the function
    except:
        print("A problem has occured while attempting to fetch the tickets!")
        print(f"{response.status_code}")

        # Parse the response json into a dictionary and look into the error key of the object to display the message to the user
        print(f"{response.json()['error']}")

        return "Bad response"
    
    print("---------------------------------------------------------------------------------------------------------------------------------")

    # If there are more than 25 tickets, begin paging through them
    if len(requests_lst) > 25:
        while view_choice != "1":
            # Begin iterating through the requests_lst by paging through 25 tickets
            for ticket in range(min, max):
                try:
                    print(f"\nTicket id: {requests_lst[ticket]['id']}, Status: {requests_lst[ticket]['status']}, Priority: {requests_lst[ticket]['priority']}, Created At: {requests_lst[ticket]['created_at']}")
                    print(f"Subject: {requests_lst[ticket]['subject']}")
                    print(f"Description: {requests_lst[ticket]['description']}\n")
                    print("---------------------------------------------------------------------------------------------------------------------------------")
                
                # If there is an exception that means there are no more item in the requests list
                except:
                    print("---------------------------------------------------------------------------------------------------------------------------------")
                    break

            # Page through the list of tickets
            view_choice = page_tickets(min, max, requests_lst)

            # If the user decides to go to the next or previous page, allow the loop control vars to accomodate for the user's choice
            if view_choice == '2':
                min += 25
                max += 25
            elif view_choice == '3':
                min -= 25
                max -= 25

    # If there are 25 or less tickets
    else:
        for ticket in range(len(requests_lst)):
            # Display ticket
            print(f"\nTicket id: {requests_lst[ticket]['id']}, Status: {requests_lst[ticket]['status']}, Priority: {requests_lst[ticket]['priority']}, Created At: {requests_lst[ticket]['created_at']}")
            print(f"Subject: {requests_lst[ticket]['subject']}")
            print(f"Description: {requests_lst[ticket]['description']}")
            print("\n")
            print("---------------------------------------------------------------------------------------------------------------------------------")

    # After fetching the tickets and the user is done viewing them, return a string saying the response was succesful
    return "Success"


def view_ticket_by_id(ticket_id, auth):
    """
    Ask the user for the ticked id that they would like to view, if it exists then the
    display the information about the ticket, else raise an error for the user and let 
    them keep entering a ticket id until they enter a valid input
    """

    print("Fetching ticket...")

    # Send a get request to fetch the ticket from the API and use the request key to access the data within that ticket in the json
    response = requests.get(f"https://zccmalabudi5807.zendesk.com/api/v2/requests/{ticket_id}", auth = auth)

    # If the status code for the get response is not a 200 (OK) then we let the user know immediately there was a problem and exit the function
    if response.ok == False:
        print("A problem has occured while requesting the ticket!")
        print(f"{response.status_code}")

        # Parse the response json into a dictionary and look into the error key of the object to display the message to the user
        print(f"{response.json()['error']}")

        return "Bad response"


    # Find the ticket
    ticket = response.json()['request']

    # Display ticket information
    print("---------------------------------------------------------------------------------------------")
    print(f"Ticket id:  {ticket['id']}, Status: {ticket['status']}, Priority: {ticket['priority']}, Created At: {ticket['created_at']}")
    print(f"Subject: {ticket['subject']}")
    print(f"Description:\n{ticket['description']}")
    print("---------------------------------------------------------------------------------------------")

    # After the user successfully fetches the ticket, return success string for the unit test        
    return "Success"



#------------- Main function --------------
def main():
    # Store Authentication with an API token in the auth tuple
    token = "bvJwx9uKm6ieRuYv0P0jmA7YojKhwfBUYmbSV1jx"
    auth = ("mohamadalabudi42@gmail.com/token", token)

    # choice will hold the user's choice after user_input is all lower case
    main_choice = ""
    sub_menu_choice = ""

    # Store boolean for when the user is in the menu
    isInMenu = True

    ticket_id = 0

    # Display the main menu to the user
    print("Welcome to the ticket viewer program")
    print("'1' - Close the program")
    print("'2' - Display a menu of options to choose from")

    # Begin allowing the user to use the ticket viewer program
    while isInMenu:
        # Ask the user if they want to see the menu (1) or exit (2) the program
        main_choice = input("")


        # Exit program
        if main_choice == "1":
            print("Thank you for using the ticket viewer program.")
            break
        
        # Display sub-menu
        elif main_choice == "2":
            # Display the menu with how they want to view the ticket(s) to the user and ask the user to pick a option from the menu
            print("     Select view options (1-3):")

            while isInMenu:
                print("       '1' - Close the program")
                print("       '2' - View all tickets")
                print("       '3' - Select a ticket to view")
                sub_menu_choice = input("")

                # Exit the program
                if(sub_menu_choice == "1"):
                    print("Thank you for using the ticket viewer program.")
                    isInMenu = False

                # View all tickets
                elif (sub_menu_choice == "2"):
                    view_tickets(auth)

                # View a specific ticket
                elif(sub_menu_choice == "3"):
                    # Ask the user for the ticket id
                    ticket_id = input("Please enter the ticket id: ")

                    # View a ticket by ticket id
                    view_ticket_by_id(ticket_id, auth)
                
                # If the user did not enter a valid option from the menu, keep asking them to input until they enter a valid option
                else:
                    print("     Invalid input, please select from the following (1-3)")

        # If the user has not entered a valid option from the main menu, run data validation
        else:
            # Display error message to the user
            print("\nInvalid input, plase select from the following options\n")
            print("'1' - Close the program")
            print("'2' - Display a menu of options to choose from")

            # Ask for user input again and validate the input
            main_choice = ""
            continue                   



if __name__ == "__main__":
    main()