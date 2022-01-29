def quicksort(ls: list[int], pivot_index: int = None) -> list[int]:
    """
    quicksort list of integers, this is not on place sort, it does not alter the original list

    :param ls: list of integers to be sorted
    :param pivot_index: pivot index, if not supplied will be the middle index
    :return: list of sorted integers
    """
    if len(ls) < 2:
        return ls

    pivot_index = pivot_index or len(ls) // 2
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
    get the middle integer from list of integers

    Ex: 3 is the middle element of [3, 2, 1, 4, 5]

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
    This is an enhanced version of quicksort (in my opinion) because it guarantees O(nlogn) runtime
    """
    return quicksort(ls, get_middle(ls))


if __name__ == "__main__":
    unsorted_ls = [2, 1, 4, 3, 5]
    sorted_ls = quicksort_enhanced(unsorted_ls)
    print(sorted_ls)
