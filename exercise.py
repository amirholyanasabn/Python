text_input = input('Please enter your text : ')
text_list = text_input.split(' ')
count_of_word = len(text_list)
text_list.sort(key=len,reverse=False)
big_word = text_list[-1]
big_word_len = len(big_word)
print('{} words are in the sentence and the biggest word is {} and its length is {}'.format(count_of_word,big_word,big_word_len))