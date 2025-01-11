import math
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

def atmf_straddle_price(S, T, r, sigma):
    call_price = black_scholes_price(S, S, T, r, sigma, option_type="call")
    put_price = black_scholes_price(S, S, T, r, sigma, option_type="put")
    return call_price + put_price

def calculate_altman_z_score(working_capital, total_assets, retained_earnings, ebit, market_value_of_equity, total_liabilities, sales):
    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit / total_assets
    X4 = market_value_of_equity / total_liabilities
    X5 = sales / total_assets

    z_score = 1.2 * X1 + 1.4 * X2 + 3.3 * X3 + 0.6 * X4 + 1.0 * X5
    return z_score

if __name__ == "__main__":
    # Inputs for ATMF Straddle
    S = 100  # Current stock price
    T = 0.5  # Time to maturity in years
    r = 0.05  # Risk-free interest rate (5%)
    sigma = 0.2  # Volatility (20%)

    straddle_price = atmf_straddle_price(S, T, r, sigma)
    print(f"The approximate price of the ATMF straddle is: {straddle_price:.2f}")

    working_capital = 500000  # Example value
    total_assets = 2000000  # Example value
    retained_earnings = 300000  # Example value
    ebit = 400000  # Example value
    market_value_of_equity = 1500000  # Example value
    total_liabilities = 800000  # Example value
    sales = 2500000  # Example value

    z_score = calculate_altman_z_score(working_capital, total_assets, retained_earnings, ebit, market_value_of_equity, total_liabilities, sales)
    print(f"The Altman Z-Score is: {z_score:.2f}")

