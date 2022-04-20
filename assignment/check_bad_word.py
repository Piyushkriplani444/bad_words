def split_text(text):
       words = text.split(' ')
       return words
        

def get_bad_words(path):
       with open(path) as f:
              lines = f.readlines()
       return lines


def replace_bad_word(word):
       size = len(word)
       replaced_word = "$"*size
       return replaced_word


def check_bad_word(text, path):
        result = ''
        bad_bool = False
        words = split_text(text)
        bad_set = get_bad_words(path)
        for word in words:
              if word in bad_set:
                     word = replace_bad_word(word)
                     bad_bool = True

              result += word

        return result, bad_bool