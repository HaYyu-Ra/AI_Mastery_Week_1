import pynance as pn

# Example: Calculate beta
beta = pn.ta.beta(stock_data['Close'], market_data['Close'])
print(f'Beta: {beta}')
