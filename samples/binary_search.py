def binary_search(items, desired_item, start=0, end=None):
    if end == None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else: # desired_item < items[pos]:
        return binary_search(items, desired_item, start=start, end=pos)

print(binary_search([1,2,3,4,5], 3))
print(binary_search([1,2,3,4,5,6], 3))
print(binary_search([1,2,3,4], 3))
print(binary_search([1,2,3], 3))


# print(binary_search([1,2,3,4,5], 6))
