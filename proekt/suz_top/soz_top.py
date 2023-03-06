import random 

from uzb_suzlar import suzlar

def uzb_suzlar():
    word = random.choice(suzlar)
    while "-" in word or " " in word;p[[;p]]:
        word = random.choice(suzlar)
    return word.upper()


def Display(user_letters, word):
    display_word = ""
    for latter in word:
        if latter in user_letters:
            display_word += latter
        else:
            display_word += "-"
    return display_word

def Play():
    word = get_word()
    word_latters = set(word)
    user_letters = ""
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")
    while word_latters:
        print(Display(user_letters, word))
        if user_letters:
            print(f"SHu vaqtgacha kiritgan xarflaringiz: {user_letters}")
            letter = input("Xarf kiriting: ").upper()
        if letter in user_letters:
            print("Bu xarfni avval kiritgansiz.")
            continue
        elif letter in word:
            word_latters.remove(letter)
            print(f"{letter} xarfi to'g'ri.")
        else:
            print("Bunday xarf yo'q")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz")
