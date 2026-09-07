# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_gallons=((sqft_walls/sqft_per_gallon)+(sqft_ceiling/sqft_per_gallon))
    cost =total_gallons*cost_per_gallon
    return cost

# Check your answer
q3.check()
