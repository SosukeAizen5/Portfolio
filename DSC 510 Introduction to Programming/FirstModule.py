def calculate_cost(feet):
    float_value = float(feet)
    if float_value <= 100:
        cost = 0.87
    elif 100 < float_value <= 250:
        cost = 0.80
    elif 250 < float_value <= 500:
        cost = 0.70
    else:
        cost = 0.50

    return float_value * cost
