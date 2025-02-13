def typeBasedTransformer(**kwargs):
    transformed_data = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Square numbers
            transformed_data[key] = value ** 2
        elif isinstance(value, str):  # Reverse strings
            transformed_data[key] = value[::-1]
        elif isinstance(value, bool):  # Invert booleans
            transformed_data[key] = not value
        elif isinstance(value, (list, tuple)):  # Reverse lists & tuples
            transformed_data[key] = value[::-1]
        elif isinstance(value, dict):  # Swap keys & values (assuming unique values)
            transformed_data[key] = {v: k for k, v in value.items()}
        else:  # Keep other types unchanged
            transformed_data[key] = value

    return transformed_data
