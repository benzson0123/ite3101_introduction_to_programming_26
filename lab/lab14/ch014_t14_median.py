def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_lst[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2.0
