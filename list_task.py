def average(lst):
    return sum(lst) / (len(lst))


def averages_row(mat):
    return list(map(average, mat))


def find_min_pos(mat):
    min_i = None
    min_j = None
    min_val = None
    for i, row in enumerate(mat):
        for j, elem in enumerate(row):
            if (min_val is None) or (elem < min_val):
                min_i = i
                min_j = j
                min_val = row[j]
    return (min_i, min_j)


def unique(lst):
    set_uniq = set(lst)
    lst_uniq = []
    for i, elem in enumerate(lst):
        if elem in set_uniq:
            set_uniq.remove(elem)
            lst_uniq.append(elem)
    return lst_uniq
