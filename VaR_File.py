import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def VaR(r, confidence, principal = 1):
    # This function returns the left tail value and displays a histogram
    # r = a vector of stock returns
    # principal = investment initial value
    # <your work>
    # out = principal * positively stated value of r at the 1-alpha percentile
    plt.hist(r, bins=50, alpha=0.75)
    plt.show()
    out=principal*np.abs(percentile(r, (1 - confidence) * 100))
    return out

# Partial demonstration
def percent_var(r, confidence):
    # This function returns the left tail value and displays a histogram
    # r = a vector of stock percent returns
    # out = positively stated value of r at the 1-alpha percentile

    plt.hist(r, bins=50, alpha=0.75)
    plt.show()

    out = abs(np.percentile(r, (1 - confidence) * 100))  # Calculate the percentile
    return abs(out)  # Return the absolute value of the calculated percentile
