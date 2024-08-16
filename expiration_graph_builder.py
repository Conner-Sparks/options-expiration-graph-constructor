import matplotlib.pyplot as plt
import numpy as np

# Given a portfolio of options, constructs expiration graph

def construct_graph(portfolio):
    """
    
    Args:
        portfolio (dict): Dictionary containing the combination of options selected by the user. 
    """

    # Calculate how much it costs to establish position. 
    
    call_prices = [i[0] * i[1] for i in portfolio["calls"]]
    put_prices = [i[0] * i[1] for i in portfolio["puts"]]
    position_cost = np.round(sum(call_prices) + sum(put_prices), 3)
    
    print(f"Cost to establish position : {position_cost}")
    
    # Extract call and put exercise prices.
    call_x_prices = []
    [call_x_prices.append(i[2]) for i in portfolio["calls"] if i[2] not in call_x_prices]
    put_x_prices = []
    [put_x_prices.append(i[2]) for i in portfolio["puts"] if i[2] not in put_x_prices]
    
    x_prices = list(call_x_prices)
    x_prices.extend(i for i in put_x_prices if i not in x_prices)
    
    print(f"Exercise prices : {x_prices}")
    
    # Calculate value of portfolio at each exercise price.
    
    call_values = {}
    put_values = {}
    portfolio_values = {}
    for price in x_prices:
        call_values[price] = 0
        put_values[price] = 0
    
    for price in x_prices: # Loop through each strike price
        for call in portfolio["calls"]:
            if call[0] > 0: # short call
                if price <= call[2]: 
                    call_values[price] += call[0] * (call[2] - price) + (call[0] * call[1])
                elif price > call[2]: 
                    call_values[price] += call[0] * (call[2] - price) + (call[0] * call[1])
            
            elif call[0] < 0: # long call
                if price <= call[2]: 
                    call_values[price] += call[0] * call[1]
                elif price > call[2]: 
                    call_values[price] += -call[0] * (price - call[2]) - (call[0] * call[1])
                    
        for put in portfolio["puts"]:
            if put[0] > 0: # short put
                if price < put[2]:
                    put_values[price] += put[0] * (price - put[2]) + (put[0] * put[1])
                elif price >= put[2]:
                    put_values[price] += put[0] * put[1]
                    
            elif put[0] < 0: # long put 
                if price < put[2]:
                    put_values[price] += -put[0] * (put[2] - price) + (put[0] * put[1])
                elif price >= put[2]:
                    put_values[price] += put[0] * put[1]
                    
        portfolio_values[price] = np.round(call_values[price] + put_values[price], 3)
        
    s = list(portfolio_values.keys())
    s.sort()
    portfolio_values = {i : portfolio_values[i] for i in s}
            
    print(f'Value of portfolio at each exercise price : {portfolio_values}')
    
    # Make axis
    x_axis = np.arange(min(x_prices) - 10, max(x_prices) + 10, 1)
    y_axis = np.arange(-10, 10, 1)
    
    # Build graph.
    
    x = list(portfolio_values.keys())
    y = list(portfolio_values.values())
    
    # x_ticks = range(len(x))
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['bottom'].set_position('zero')

    plt.plot(x, y)
    plt.show()
    
def __main__():
    
    # Portfolio dictionary will be created by data_intake.py. Dictionary with keys "calls" and "puts". 
    # Each key contains a list of calls and puts which holds tuples containing the nature of the position
    # (long/short), the price of the option, and the exercise/strike price of the option.

    # portfolio["calls"][0] == -1, indicating this portfolio is long one call, the price is contained in 
    # the 1st index position, $5.50 here, and the exercise price is contained within the 2nd index position, $95 here.
    # We can see that this portfolio is also long 3 puts at $1.15 each, each with an exercise price of $105.
     
    portfolio = {
    "calls" : [(1, 9.35, 90), (-2, 2.70, 100)],
    "puts" : [(4, 1.55, 95), (-2, 3.70, 100)]
    }   
    construct_graph(portfolio)

__main__()