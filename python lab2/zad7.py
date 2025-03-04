from collections import Counter

def most_frequent_element(data: list) -> any:
    if not data:
        return None
    return Counter(data).most_common(1)[0][0]