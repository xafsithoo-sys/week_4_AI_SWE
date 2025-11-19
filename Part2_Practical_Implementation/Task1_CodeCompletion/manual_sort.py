# manual_sort.py
# Manual implementation: sort list of dictionaries by a specific key.
def sort_dicts(data, key):
    """
    Sort a list of dictionaries by the given key.
    Assumes every dict contains the key.
    """
    return sorted(data, key=lambda x: x[key])

# Example usage
if __name__ == "__main__":
    items = [{"name":"a","score":10},{"name":"b","score":5},{"name":"c","score":7}]
    print(sort_dicts(items, "score"))
