def calculate_frequencies_case_sensitive(word_list):
    count_dict = {}
    
    for word in word_list:
        count_dict[word] = count_dict.get(word, 0) + 1
    
    return count_dict

user_input = input() 

user_words = user_input.split()

frequencies = calculate_frequencies_case_sensitive(user_words)

for word in user_words:
       print(f"{word} {frequencies[word]}")
