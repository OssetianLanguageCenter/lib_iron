import json
import string

non_oset_symbols = 'ьшщэюя'
# ж без дж
print("version 2.0")
def from_file_to_dict(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)
def load_bigrams(path=""):
    global dict_ose, dict_rus
    dict_ose = from_file_to_dict("bigrams/bigram_normal_ose.json")
    dict_rus = from_file_to_dict("bigrams/bigram_normal_rus.json")
    #print(len(dict_rus), len(dict_ose))

def is_ose_word(word):
    # добавим к каждому слову символ начала и конца слова
    if any([sym in non_oset_symbols or sym in string.punctuation for sym in word.lower()]):
        return (False, 0, 0)
    word = "%" + word + "%"

    sum_ose = 0
    sum_rus = 0
    for j in range(len(word)-1):
        bigramm = word[j:j+2]
        if bigramm in dict_ose:
            sum_ose += dict_ose[bigramm]
        if bigramm in dict_rus:
            sum_rus += dict_rus[bigramm]
    if sum_ose > sum_rus:
        return True, sum_ose, sum_rus
    else:
        return False, sum_ose, sum_rus

# удалить символ ударения
# æххуы́рст æххуырст
# удалить символ вариации окончания и само окончание
# мæсǀы́г мæс
def delete_symbol_stress(word):
    #print(len(word))
    symbol_stress = "́"
    word = word.replace(symbol_stress, "")
    #print(len(word))
    symbol_ending = "ǀ"
    pos = word.find(symbol_ending)
    if pos != -1:
        word = word[:pos]
    return word

if __name__ == "__main__":
    load_bigrams()
    print(is_ose_word("иристон"))
    print(delete_symbol_stress("мæсǀы́г"))
    print(is_ose_word(delete_symbol_stress("кæнын")))