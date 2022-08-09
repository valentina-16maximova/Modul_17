def lst_sort(lst):
    return sorted(lst)
def lst_find_num(lst, num):
    for i in range(len(lst) - 1):
        if num > lst[i] and num <= lst[i + 1]:
            return i + 1
    return -1
def f():
    seq = list(map(int, input('Input sequence: ').split()))
    num = int(input('Input number: '))
    seq_sorted = lst_sort(seq)
    position = lst_find_num(seq_sorted, num)
    print('Sequence', *seq)
    print('Number', num)
    print('Sequence Sorted', *seq_sorted)
    print('Position in sorted sequence', *seq_sorted,
          'for number', num,
          'is', position)

