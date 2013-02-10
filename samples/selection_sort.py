def selection_sort(items):
    """Sorts a list of items into ascending order using the
       selection sort algoright.
       """
    for step in range(len(items)):
        # Find the location of the smallest element in
        # items[step:].
        location_of_smallest = step
        for location in range(step, len(items)):
            # determine location of smallest
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        # Exchange items[step] with items[location_of_smallest]
        temporary_item = items[step]
        items[step] = items[location_of_smallest]
        items[location_of_smallest] = temporary_item
    return items


if __name__ == "__main__":
    print(selection_sort([5, 4, 3, 2, 1]))
    print(selection_sort([3, 2, 3, 1, 5]))
    print(selection_sort([]))
    print(selection_sort([1]))
    print(selection_sort([2, 1]))
    print(selection_sort([1, 2]))
    print(selection_sort([3, 3]))
