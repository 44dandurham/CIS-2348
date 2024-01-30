def filter_and_sort_integers(int_list):
    return sorted([i for i in int_list if i >= 0])

user_input = input()

input_integers = list(map(int, user_input.split()))

sorted_non_negatives = filter_and_sort_integers(input_integers)

print(' '.join(map(str, sorted_non_negatives)), end=" ",)
