classes = {
    "apple_pie": 0, 
    "cheesecake": 1, 
    "chicken_curry": 2, 
    "french_fries": 3, 
    "fried_rice": 4, 
    "hamburger": 5,
    "hot_dog": 6,
    "ice_cream": 7,
    "omelette": 8, 
    "pizza": 9, 
    "sushi": 10
}


# Helper function with Exponential Weighted Moving Average implementation for smoothing the lines
def smooth(scalars, weight=0.9):  # Weight between 0 and 1
    last = scalars[0]                                           
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value

    return smoothed
