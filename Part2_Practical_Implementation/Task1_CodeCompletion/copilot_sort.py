# copilot_sort.py
# Example AI/Copilot-style implementation: more defensive to missing keys.
def sort_dicts(data, key):
    """
    Sort a list of dictionaries by the given key.
    Uses .get() to handle missing keys and returns original list on error.
    """
    try:
        return sorted(data, key=lambda x: x.get(key, None))
    except Exception as e:
        print("Sorting error:", e)
        return data

# Example usage
if __name__ == "__main__":
    items = [{"name":"a","score":10},{"name":"b"},{"name":"c","score":7}]
    print(sort_dicts(items, "score"))
