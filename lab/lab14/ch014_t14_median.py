def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        # If 