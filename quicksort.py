# Example of quicksort algorithm

# REF: Grokking algorithm, loc: 1634

def quicksort(ls: list[int]) -> list[int]:
    """
    Quicksort list of integers using the middle index element as the pivot.
    This is not in-place sort, it does not alter the original list.

    :param ls: list of integers to be sorted
    :return: list of sorted integers
    """
    if len(ls) < 2:
        return ls

    pivot_index = len(ls) // 2
    pivot = ls[pivot_index]

    left: list[int] = []
    right: list[int] = []

    for i, val in enumerate(ls):
        if i == pivot_index:
            continue
        if val > pivot:
            right.append(val)
        else:
            left.append(val)

    return quicksort(left) + [pivot] + quicksort(right)


def get_middle(ls: list[int]) -> int:
    """
    get the middle integer from list of integers.
    Eg: 3 is the middle element of [3, 2, 1, 4, 5]

    :param ls: list of integers
    :return: middle_index
    """

    average = sum(ls) / len(ls)
    middle_index = 0
    for i, val in enumerate(ls):
        if val == ls[middle_index]:
            continue
        if abs(val - average) < abs(ls[middle_index] - average):
            middle_index = i

    return middle_index


def quicksort_enhanced(ls: list[int]):
    """
    This is an enhanced version of quicksort (in my opinion) because it guarantees O(nlogn) runtime as it always
    uses the middle element (not the middle index) as the pivot

    In practice, quicksort is about twice faster or even more!!
    """

    if len(ls) < 2:
        return ls

    pivot_index = get_middle(ls)
    pivot = ls[pivot_index]

    left: list[int] = []
    right: list[int] = []

    for i, val in enumerate(ls):
        if i == pivot_index:
            continue
        if val > pivot:
            right.append(val)
        else:
            left.append(val)

    return quicksort_enhanced(left) + [pivot] + quicksort_enhanced(right)


if __name__ == "__main__":
    unsorted_ls = [2, 1, 4, 3, 5]
    sorted_ls = quicksort_enhanced(unsorted_ls)
    print(sorted_ls)
