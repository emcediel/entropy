import numpy as np

def entropy(probs):
    """Assumes that it is a numpy array and that it is a valid probability vector."""
    entropy=-(probs*np.log(probs))
    return entropy.value
    
if __name__ == "__main__":
    pass
