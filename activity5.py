from sympy import true


def more_than_20(file):
    open_file=open(file)
    ret_list= []
    for i in open_file:
        x=i.strip()
        if len(x)> 20:
                ret_list.append(x)
    return ret_list

print(more_than_20('CROSSWD.txt'))

def has_no_e(word):
    for i in word:
          if i == "e":
            return False
    return True

def uses_only(word, letters):
    for i in word:
        if i not in letters:
            return False
    return True

def all_uses_only(file, letters):
    valid_words = []
    with open(file, 'r') as words_file:
        for line in words_file:
            word = line.strip()
            if uses_only(word, letters):
                valid_words.append(word)
    return valid_words
