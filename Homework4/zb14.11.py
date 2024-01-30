def selection_sort_descend_trace(data_list):
   
    for current_position in range(len(data_list) - 1):
        largest_index = current_position

       
        for next_index in range(current_position + 1, len(data_list)):
            if data_list[next_index] > data_list[largest_index]:
                largest_index = next_index

      
        data_list[current_position], data_list[largest_index] = data_list[largest_index], data_list[current_position]

        
        print(' '.join(map(str, data_list)),'')



if __name__ == "__main__":
    
    numbers = [int(x) for x in input().split()]

    selection_sort_descend_trace(numbers)

