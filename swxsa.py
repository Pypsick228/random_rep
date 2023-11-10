from speech import speech
import random
import time
levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}
def play_game(level):
    words = levels[level]
    score = 0
    for i in range(len(words)):
        random_word = random.choice(words)
        print("Произнесите слово {random_word}")
        recog_word = speech()
        print(recog_word)
        if random_word == recog_word:
            print("Правильный ответ!")
            score = score + 1
        else:
            print("Вы ответили неправильно! Ответ был {random_word}")
        time.sleep(2)
    print(f"Игра завершена! Ваш счёт: {score}/{len(words)}")
selected_level = input("Выберите уровень сложности.(Easy, medium, hard)").lower()
play_game(selected_level)