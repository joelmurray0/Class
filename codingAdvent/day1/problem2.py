NUMBER_WORDS = {
     "one": 1,
     "two": 2,
     "three": 3,
     "four": 4,
     "five": 5,
     "six": 6,
     "seven": 7,
     "eight": 8,
     "nine": 9,
     "zero": 0,
}

def find_index(stringy, number_words, nums="0123456789"):
     index1 = None
     index2 = None
     worded_numbers = list(number_words.keys())
     
     word_dict = {}
     word_indexes = []
     for i in range(len(number_words)):
          if worded_numbers[i] in stringy:
               index = int(str(stringy.index(worded_numbers[i]))[0])
               word_dict[index] = list(number_words.keys())[i]
               word_indexes.append(index)

     num_dict = {}
     num_indexes = []

     for j in range(len(stringy)):
          if stringy[j] in nums:
               index1 = j
               num_indexes.append(index1)
               num_dict[index1] = int(stringy[j])

     elig_word = True
     elig_num = True
     if word_indexes == []:
          elig_word = False
          max_word_index = -1
          min_word_index = len(stringy)
     if num_indexes == []:
          elig_num = False
          max_num_index = -1
          min_num_index = len(stringy)

     if elig_word:
          max_word_index = max(word_indexes)
          min_word_index = min(word_indexes)
     if elig_num:
          max_num_index = max(num_indexes)
          min_num_index = min(num_indexes)

     if max_word_index > max_num_index:
          last_num = NUMBER_WORDS[word_dict[max_word_index]]
     elif max_word_index == max_num_index:
          last_num = 0
     else:
          last_num = num_dict[max_num_index]
     
     if min_word_index < min_num_index:
          first_num = NUMBER_WORDS[word_dict[min_word_index]]
     elif min_word_index == min_num_index:
          first_num = 0
     else:
          first_num = num_dict[min_num_index]

     num = first_num * 10 + last_num

     return num

strrr = "asksdjone123"


sum = 0
# The text file was removed - the code works though!
with open("codingAdvent\day1\ListOfNums.txt", "r")as file:
     inputs = file.readlines()
     
for i in inputs:
     sum += find_index(i, NUMBER_WORDS)
print(sum)


