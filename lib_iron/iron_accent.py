
strong_vowels = "ауеои"
weak_vowels = "ыæ"

# знак ударения плохо видно, но он там есть, в кавычках)
stress_mark = "́"
semivowel_y = "у"
vocal = ["гласная", "согласная"]

vowel = strong_vowels + weak_vowels

def is_y_consonant(word, ind=None):
    if ind is None:
        ind = word.find(semivowel_y)
    if ind != None:
        if word[ind] == semivowel_y:
            # как отдельное слово
            if word == semivowel_y: return False
            # удвоенное y
            i = word.find(semivowel_y + semivowel_y)
            if i != -1 and (ind == i or ind == i + 1): return True
            # если в начале слова, то перед гласной, у - согласный
            if ind == 0:
                return word[1] in strong_vowels + weak_vowels
            # если в конце слова, то после гласной, у - согласный
            if ind == -1 or ind == len(word) - 1:
                return word[-2] in strong_vowels + weak_vowels
            # после гласной
            if word[ind - 1] in strong_vowels + weak_vowels:
                return True
                # перед гласной
                # if word[ind + 1] in strong_vowels + weak_vowels: return True

            else:
            # после согласной
                return word[ind + 1] in strong_vowels + weak_vowels
    return None


def check_stress_mark(word):
    return stress_mark in word

def delete_stress_mark(word):
    for ind, letter in enumerate(word):
        if letter == stress_mark:
            return word[:ind] + word[ind + 1:]
    return word


# возвращает список кортежей (гласная буква, ее позиция)
def find_vowel(word):
    vowels = list()
    for ind, letter in enumerate(word):
        if letter in vowel:
            if letter == semivowel_y:
                if not is_y_consonant(word, ind=ind):
                    vowels.append((letter, ind))
            else:
                vowels.append((letter, ind))
    #print(vowels)
    return vowels

# на каком слоге стоит ударение и на какую (сильную или слабую) падает ударение
class Accent_syllable:
    def __init__(self, index_syllable, vowel, index_vowel, strong_vowels):
        self.index_syllable = index_syllable
        self.vowel = vowel
        self.index_vowel = index_vowel
        self.strong_vowels = strong_vowels

    def __str__(self):
        return f"index_syllable: {self.index_syllable}, vowel: {self.vowel}, index_vowel: {self.index_vowel}"
def get_index_syllable(word):
    if check_stress_mark(word):
        ind_stress = word.index(stress_mark)
        vowels = find_vowel(word)
        for ind, item in enumerate(vowels, 1):
            if item[1] + 1 == ind_stress:
                return Accent_syllable(ind, *item, item[0] in strong_vowels)
    return None



def add_accent(word, ind):
    return word[:ind + 1] + stress_mark + word[ind + 1:]
# если подан текст ставит ударение только в первом слове
# возвращает слово со знаком ударения и индекс символа (начаная с 0) на котором стоит ударение
def put_stress_mark(word):
    if word:
        word_source = word
        vowels = find_vowel(word.lower().split()[0])
        if vowels:
            # если одна гласная в слове, то ударение не ставим
            if len(vowels) == 1:
                return word_source, vowels[0][1]
            # ударение на первую сильную гласную
            if vowels[0][0] in strong_vowels:
                return add_accent(word_source, vowels[0][1]), vowels[0][1]
            # ударение на вторую гласную
            return add_accent(word_source, vowels[1][1]), vowels[1][1]
        else:
            # заимствование или предлог, т.е. не можем поставить знак ударения
            return (word_source, None)
    return None, None



if __name__ == '__main__':
    print(get_index_syllable("уа́зæгуат"))
    print(get_index_syllable("хуыца́убон"))
    # print(word:="уа́зæгуат", find_vowel(word), put_stress_mark(delete_stress_mark(word)))
    # print(word:="хуыца́убон", find_vowel(word), put_stress_mark(delete_stress_mark(word)) )

    # проверка ударения
    # print(put_stress_mark("фыр"))
    # # провека определения y - гласная или согласная
    # for test_word in ["хæрзæгъдаудзинад", "æххуырст", "урс", "да́мгъуат", "хъул", "къу́ту", "нæуу", "а́ууон", "фыр"]:
    #     test_word = delete_stress_mark(test_word.lower().strip())
    #     for ind_y in [ind for ind, b in enumerate(test_word) if b == semivowel_y]:
    #         print(test_word, ind_y + 1, vocal[is_y_consonant(test_word, ind_y)])

    #file_name = "stress_slovnik_rus_ose.csv"
    # file_name = "y_arter_vowel_front_дзл.txt"
    #file_name = "y_after_vowel.txt"

    # with open(file_name, "r", encoding="utf_8") as file:
    #     words_y = file.readlines()
    #     print(len(words_y))
    #     for test_word in words_y:
    #         test_word = delete_stress_mark(test_word.lower().strip())
    #         for ind_y in [ind for ind, b in enumerate(test_word) if b == semivowel_y]:
    #             print(test_word,  ind_y + 1, vocal[is_y_consonant(test_word, ind_y)])
    #             #is_y_consonant(test_word, ind_y)
    #
    #
