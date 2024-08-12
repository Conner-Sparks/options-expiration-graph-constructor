import matplotlib as plt
import numpy as np

# Given a portfolio of options, constructs expiration graph

def construct_graph(portfolio):
    """
    
    Args:
        portfolio (dict): Dictionary containing the combination of options selected by the user. 
    """
    # Determine profit/loss at each exercise price.
    num_calls = len(portfolio["calls"])
    num_puts = len(portfolio["puts"])
    print(f"num calls: {num_calls}")
    print(f"num puts: {num_puts}")
    
    call_prices = [i[0] for i in portfolio["calls"]]
    put_prices = [i[0] for i in portfolio["puts"]]
    
    call_x_prices = []
    [call_x_prices.append(i[1]) for i in portfolio["calls"] if i[1] not in call_x_prices]
    
    put_x_prices = []
    [put_x_prices.append(i[1]) for i in portfolio["puts"] if i[1] not in put_x_prices]
    
    exercise_prices = call_x_prices + put_x_prices
        
    # Calculate how much it cost to establish position. 
    position_cost = np.round(sum(call_prices) + sum(put_prices), 3)
    print(f"Cost to establish position : {position_cost}")
    print(f"Exercise prices : {exercise_prices}")
    
def __main__():
    portfolio = {
    "calls" : [(-5.50, 105)],
    "puts" : [(1.15, 95), (1.15, 95), (1.15, 95)]
    }   
    construct_graph(portfolio)

__main__()