import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):
    if VaR is None:
        VaR = np.percentile(losses, 100 * confidence)
    es_value = np.mean(losses[losses > VaR])
    return es_value
