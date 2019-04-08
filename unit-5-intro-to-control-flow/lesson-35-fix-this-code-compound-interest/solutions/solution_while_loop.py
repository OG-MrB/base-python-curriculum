def compound_interest_result(initial_investment, interest_percentage, num_periods):
    total = initial_investment
    count = 0
    while count < num_periods:
        total += total * .1
        count += 1
    return total
