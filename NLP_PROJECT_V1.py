import string
import re
 
selectiveness = 10
my_text = """
"""

# removes punctuation in a given string

def check_upper(word):
    for letter in word:
        if letter.isupper():
            return True
    else:
        return False
    
def remove_punctuation(input_string):
    punctuation_chars = string.punctuation + "()" + '"'
    translator = str.maketrans("", "", punctuation_chars)
    result_string = input_string.translate(translator)
    return result_string


# removes punctuation from text
text_without_punc = remove_punctuation(my_text)

# splits the text into words
split_text = my_text.split()

# checks if a word in the text is in the word list


def check_existing(word, word_list):
    x = 0
    if len(word_list) == 0:
        return True
    else:
        for existing_word in word_list:
            if word != existing_word[0]:
                x += 1
            if word == existing_word:
                x = x
    if x < len(word_list):
        return False

    if x == len(word_list):
        return True


# creates a list of words
word_list = []

for i in split_text:
    if check_existing(i, word_list):
        word_item = []
        word_item.append(remove_punctuation(i))
        word_item.append(0)
        word_list.append(word_item)
        
    if not check_existing(i, word_list):
        for existing_word in word_list:
            if i == existing_word[0]:
                existing_word[1] += 1
        

# sorts word list by word frequency
frequences = []
most_common_freq = []
most_common_words = []

for word_object in word_list:
    global freq
    freq = word_object[1]

    frequences.append(freq)
for i in range(3):
    max_freq = max(frequences)
    most_common_freq.append(max_freq)
    frequences.remove(max_freq)

for w in word_list:
    for frequency in most_common_freq:
        if w[1] == frequency:
            most_common_words.append(w[0])

print(most_common_words)

scentences_without_punc = []
scentences = re.split('[.?!]', my_text)

# gets rid of all punctuation in the scentences
for scentence in scentences: 
    scentence_without_punc = remove_punctuation(scentence)
    scentences_without_punc.append(scentence_without_punc)

# ranks the scentence
def scentence_rank(scentence):
    rank = 0
    scen_no_punc = remove_punctuation(scentence)
    split_scentence = scen_no_punc.split()
    
    for scen_word in split_scentence:
        for word in most_common_words:
            if scen_word.lower() == word.lower():
                rank += 1
            if check_upper(scen_word):
                rank -= 1
            
    
    #print(split_scentence)

    return rank


scentence_rankings = []
top_three_rankings = []

for scentence in scentences_without_punc:
    rank = scentence_rank(scentence)
    scentence_rankings.append(rank)

for i in range(selectiveness):
    top_ranking = min(scentence_rankings)
    top_three_rankings.append(top_ranking)
    scentence_rankings.remove(top_ranking)
x = 0
for scentence in scentences_without_punc:
    scen_rank = scentence_rank(scentence)
    if scen_rank in top_three_rankings:
        print("")
        print(scentence)
        x += 1
        
print(x)