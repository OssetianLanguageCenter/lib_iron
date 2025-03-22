import string
CYRILIC = "ӔАВЕКМНОРСТХаеорсуӕ"
LATIN   = "ÆABEKMHOPCTXaeopcyæ"
RIGHT_SYMBOL_AE = "æ"

alpha = list()


def word_code_symbols(word):
    return word + " " + "|".join(map(lambda x: str(ord(x)), word))

try:
    file = open("lib_iron/alpha.txt", "r", encoding="utf-8")
    alpha = file.read().split('\n')
    file.close()
    #print(alpha)
except:
    print("нет файла с алфавитом alpha.txt")


# передаем слово и dеfine  - не понимаю что это))) может хотела алфавит согласно которому сортируем?     
class dict_word:
    def __init__(self, word, remove_word_with_bad_symbols=True):
        self.word = word.strip()
        # проверить что все буквы слова из алфавита
        error_sym = ""
        for i in range(len(word)):
            sym = word.lower()[i]
            if sym not in alpha:
                # встретилась латинская буква - заменить на аналог кирилический
                #print(word_code_symbols(word))
                if sym in LATIN:
                    self.word = word[:i] + CYRILIC[LATIN.index(word[i])] + word[i+1:]
                    #print(word_code_symbols(self.word))
                else:
                    error_sym += sym+":"+str(ord(sym)) + " "
        if error_sym:
            # удалить слово с неверными символами
            if remove_word_with_bad_symbols:
                self.word = ''
                print(f"в слове {word} символы {error_sym} отсутствуют в словаре")

    def __str__(self):
        return self.word  #+ "\n" + self.define
    def __eq__(self, other):
        return self.word == other.word
    def __ne__(self, other):
        return self.word != other.word
    def __lt__(self, other):
        try:
            for i in range(min(len(self.word), len(other.word))):
                if alpha.index(self.word[i].lower()) < alpha.index(other.word[i].lower()):
                    return True
                elif alpha.index(self.word[i].lower()) > alpha.index(other.word[i].lower()):
                    return False
            if len(self.word) < len(other.word):
                return True
            return False
        except:
            print(f"{i} |{self.word} &le& {other.word}|")
            #print(self.word[i],alpha.index(self.word[i].lower()))
            #print(other.word[i], alpha.index(other.word[i].lower()))
            #print(i, alpha.find(self.word[i].lower()))
            #print(i, alpha.find(other.word[i].lower()))
    
    def __le__(self, other):
        return self.word < other.word or self.word == other.word
    def __gt__(self, other):
        try:
            for i in range(min(len(self.word), len(other.word))):

                if alpha.index(self.word[i].lower()) > alpha.index(other.word[i].lower()):
                    return True
                elif alpha.index(self.word[i].lower()) < alpha.index(other.word[i].lower()):
                    return False
            if len(self.word) > len(other.word):
                return True
            return False
        except:
            print(f"|{self.word}&le&{other.word}|")
            
    
    def __ge__(self, other):
            return self.word > other.word or self.word == other.word

    def list(self):
        list_letters = []
        i = 0
        while i < len(self.word):
            try_letter = self.word[i:i + 2]
            if try_letter.lower() in alpha:
                list_letters.append(try_letter)
                i += 2
            else:
                list_letters.append(self.word[i])
                i += 1
        return list_letters
    def __repr__(self):
        return self.word


