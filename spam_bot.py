import random, pyautogui, time

class Spam:
    def __init__(self, file, MAXIMUM_SENTENCE_LENGTH):
        self.file = file
        self.MAXIMUM_SENTENCE_LENGTH = MAXIMUM_SENTENCE_LENGTH

    def to_list(self):
        f = open(self.file, "r")
        words_list = []
        for word in f:
            words_list.append(word.strip())
        f.close()
        return words_list

    def get_length(self):
        return len(self.to_list())

    def make_sentence(self):
        sentence = ""
        sentence_length = random.randint(0, self.MAXIMUM_SENTENCE_LENGTH)
        for i in range(sentence_length):
            current_word = self.to_list()[random.randint(1, self.get_length())]
            sentence += current_word + " "
            # print(sentence)

        return (sentence.strip()) + "."

    def type_spam(self, sentence):
        pyautogui.write(sentence, interval=0)
        pyautogui.press("enter")
        return None

if __name__ == "__main__":
    s = Spam("words_alpha.txt", 20)
    # print(s.make_sentence())
    time.sleep(2)
    for i in range(60):
        s.type_spam(s.make_sentence())