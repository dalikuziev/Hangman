import random as r
from emoji import stages, logo

print(logo)
word = []
number = int(input("Nechta so'zdan iborat so'z o'yinini o'ynamoqchisiz: "))

while number < 2:
  if number < 0:
    number = int(input("musbat son kiriting: "))
  else:
    number = int(input("kamida 2ta so'z bo'lishi kerak shuning uchun qayta kiriting: "))
i = 1
for n in range(number):
  user_word = input(f"{i}-so'z: ").lower()
  while len(user_word) < 2:
    user_word = input(f"{i}-so'z: ").lower()
  word.append(user_word)
  i += 1
word_pc = r.choice(word)

def display(user_letters, word_pc):
  display_letters = ""
  for letter in word_pc:
    if letter in user_letters:
      display_letters += letter + " "
    else:
      display_letters += "- "
  return display_letters

def play():
  word_letters = set(word_pc)
  user_letters = ""
  print(f"{len(word_pc)} harfdan iborat so'zni topolasizmi")
  j = 0
  while word_letters and j < 7:
    print(display(user_letters, word_pc))
    letter = input("Harf kiriting: ").lower()
    while len(letter) != 1:
      print("Iltimos bitta harf kiriting!")
      letter = input("Harf kiriting: ").lower()
    if letter in user_letters:
      print(f"{letter} bu harfni oldin kiritgansiz")
      continue
    elif letter in word_pc:
      print(f"Topdingiz {letter} harfi so'zni ichida bor")
      word_letters.remove(letter)
    else:
      print(stages[j])
      j += 1
    user_letters += letter
  if word_letters:
    print(f"Siz yutkazdingiz, bu {word_pc} so'zi edi")
  else:
    print(f"Tabriklaymiz {word_pc} so'zini {len(user_letters)}ta urinishda topdingiz")

play()
