def compound_interest_result(initial_investment, interest_percentage, num_periods):
    return initial_investment * ((1 + interest_percentage / 100.0) ** num_periods)
