import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):
    """
    Calculate the Expected Shortfall (ES) of losses.
    
    losses: array of positively stated loss values
    confidence: risk level (e.g., 0.99 for 99%)
    VaR: dollar value specifying the VaR threshold

    return Expected Shortfall as the average of losses exceeding VaR
    """
    if VaR is None:
        # If VaR is not provided, determine VaR based on the confidence percentile
        VaR = np.percentile(losses, 100 * confidence)
    
    # Calculate ES as the average of losses exceeding the VaR threshold
    es_value = np.mean(losses[losses > VaR])
    return es_value
