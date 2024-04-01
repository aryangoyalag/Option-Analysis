from scipy.stats import norm
from numpy import sqrt
def bachelier_vega(S, K, T, sigma):
    d = (S - K) / (sigma * sqrt(T))
    return norm.pdf(d)*sqrt(T)
def bachelier_option_price(S, K, T, sigma):
    return (S-K)*norm.cdf((S-K)/(sigma*sqrt(T))) + sigma*sqrt(T)*norm.pdf((S-K)/(sigma*sqrt(T)))
def implied_volatility(S, K, T, premium, max_iter=10000, tol=1e-8):
    sigma = 0.4  # Initial guess for implied volatility
    for i in range(max_iter):
        option_price = bachelier_option_price(S, K, T, sigma)
        vega = bachelier_vega(S, K, T, sigma)
        diff = premium - option_price
        if abs(diff) < tol:
            return sigma
        sigma += diff / vega
    return None  # If convergence fails

# Example usage:
S = 94.820  # Spot price
K = 94.6875  # Strike price
T = 74.22/365  # Time to expiration (in years)
premium = 14.5/100  # Option premium
implied_vol = implied_volatility(S, K, T, premium)
print("Implied volatility:", round(implied_vol*100,2))