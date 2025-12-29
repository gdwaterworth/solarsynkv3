def traverse_json(data_structure, indent=""):
    """
    Recursively steps through all fields in a nested JSON structure (dict or list).
    """
    if isinstance(data_structure, dict):
        # Iterate over dictionary items
        for key, value in data_structure.items():
            print(f"{indent}Key: {key}")
            # If the value is another complex structure, recurse
            if isinstance(value, (dict, list)):
                traverse_json(value, indent + "  ")
            else:
                print(f"{indent}  Value: {value}")
    
    elif isinstance(data_structure, list):
        # Iterate over list items
        for index, item in enumerate(data_structure):
            print(f"{indent}Index: {index}")
            # If the item is a complex structure, recurse
            if isinstance(item, (dict, list)):
                traverse_json(item, indent + "  ")
            else:
                print(f"{indent}  Value: {item}")
