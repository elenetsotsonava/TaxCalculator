def tax_calculator():
    # Dictionary of predefined state tax rates
    state_tax_rates = {
        'Alabama': 4.00,
        'Alaska': 0.00,
        'Arizona': 5.60,
        'Arkansas': 6.50,
        'California': 7.25,
        'Connecticut': 6.35,
        'Delaware': 0.00,
        'Florida': 6.00,
        'Georgia': 4.00,
        'Hawaii': 4.00,
        'Idaho': 6.00,
        'Illinois': 6.25,
        'Indiana': 7.00,
        'Iowa': 6.00,
        'Kansas': 6.50,
        'Kentucky': 6.00,
        'Louisiana': 4.45,
        'Maine': 5.50,
        'Maryland': 6.00,
        'Massachusetts': 6.25,
        'Michigan': 6.00,
        'Minnesota': 6.875,
        'Mississippi': 7.00,
        'Missouri': 4.225,
        'Montana': 0.00,
        'Nebraska': 5.50,
        'Nevada': 6.85,
        'New Hampshire': 0.00,
        'New Jersey': 6.625,
        'New Mexico': 4.875,
        'New York': 4.00,
        'North Carolina': 4.75,
        'North Dakota': 5.00,
        'Ohio': 5.75,
        'Oklahoma': 4.50,
        'Oregon': 0.00,
        'Pennsylvania': 6.00,
        'Rhode Island': 7.00,
        'South Carolina': 6.00,
        'South Dakota': 4.20,
        'Tennessee': 7.00,
        'Texas': 6.25,
        'Utah': 6.10,
        'Vermont': 6.00,
        'Virginia': 5.30,
        'Washington': 6.50,
        'West Virginia': 6.00,
        'Wisconsin': 5.00,
        'Wyoming': 4.00,
        'District of Columbia': 6.00
    }

    try:
        # Get user input for cost and tax type
        cost = float(input("Enter the cost of the item: "))
        tax_rate_type = input(
            "Do you want to enter a 'country' tax or a 'state' tax? (enter 'country' or 'state'): ").strip().lower()

        # If user chooses 'country', ask for the tax rate
        if tax_rate_type == 'country':
            tax_rate = float(input("Enter the country tax rate (in percentage): "))
        elif tax_rate_type == 'state':
            # Ask for the state and look up the tax rate from the dictionary
            state = input("Enter the state: ").strip().title()  # Ensure proper case formatting
            if state in state_tax_rates:
                tax_rate = state_tax_rates[state]
                print(f"Tax rate for {state} is {tax_rate}%")
            else:
                print(f"Sorry, we don't have the tax rate for {state}.")
                return
        else:
            print("Invalid input. Please enter 'country' or 'state'.")
            return

        # Calculate the tax and total cost
        tax = (tax_rate / 100) * cost
        total_cost = cost + tax

        # Output the results
        print(f"\nOriginal Cost: ${cost:.2f}")
        print(f"Tax Amount: ${tax:.2f}")
        print(f"Total Cost with Tax: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for cost and tax rate.")


# Call the function
tax_calculator()
