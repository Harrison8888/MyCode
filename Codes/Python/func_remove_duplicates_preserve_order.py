# func_remove_duplicates_preserve_order.py
def func_remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(func_remove_duplicates_preserve_order([1, 2, 2, 3, 4, 4, 5]))
