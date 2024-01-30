num_calls = 0

def partition(user_ids, low, high):
    pivot = user_ids[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while user_ids[i] < pivot:
            i += 1
        j -= 1
        while user_ids[j] > pivot:
            j -= 1
        if i >= j:
            return j
        user_ids[i], user_ids[j] = user_ids[j], user_ids[i]

def quicksort(user_ids, low, high):
    global num_calls
    num_calls += 1
    if low < high:
        pivot_index = partition(user_ids, low, high)
        quicksort(user_ids, low, pivot_index)
        quicksort(user_ids, pivot_index + 1, high)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

   
    print(num_calls)

    for user_id in user_ids:
        print(user_id)
