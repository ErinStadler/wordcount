"""Count words in file."""


# put your code here.

def make_word_count_dict(phrase):
    lines = open(phrase)
   
    word_count_dict = {}

    for line in lines:
        line = line.rstrip()
        word = line.split()

        for individual_words in word:
            word_count_dict[individual_words] = word_count_dict.get(individual_words, 0) + 1

    return word_count_dict
    
    # for line in lines:
    #     line = line.rstrip()
    #     word = line.split()

    #     for each_word in word:
    #         word = str(word)
    #         if each_word not in word_count_dict:
    #             word_count_dict[each_word] = 1
    #         else:
    #             word_count_dict[each_word] += 1
    # return word_count_dict

print(make_word_count_dict("twain.txt"))

# Read each line of text file one by one
# For each line, remove white space from each line and split line into individual str
# For each list of str, check if each word is in dict
# If it is, add to count; if repeated, +1