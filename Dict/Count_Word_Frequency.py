words = ['apple','orange','banana','apple','orange','orange']

def word_frequency(words):
    word_frequerncy_dict = {}
    for word in words:
        word_frequerncy_dict[word] = word_frequerncy_dict.get(word,0)+1

    return(word_frequerncy_dict)

print(word_frequency(words))