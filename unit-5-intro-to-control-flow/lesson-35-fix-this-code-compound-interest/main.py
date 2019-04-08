def compound_interest_result(initial_investment, interest_percentage, num_periods):
    total = initial_investment
    count = 0
    while count < num_periods:
        total += initial_investment * .1
        count += 1
    return total


# Use the "Run Code" button to try your code. This will not affect your solution or tests:
print(round(compound_interest_result(1000, 10, 5), 2))
