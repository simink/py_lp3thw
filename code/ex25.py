def break_words(stuff):
    """ this funciton breaks up words """
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    """prints first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in full sentence and return words sorted"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sort words then print first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# use the following to check - help(ex25)
# those """ are documentation comments