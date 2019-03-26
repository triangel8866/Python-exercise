n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = ""
  for numbers in lists:
    for item in numbers:
      results += item
return results

print flatten(n)

result = []
type(result)


from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
    print ("Turn", turn + 1)
    if turn  == 3:
        print "Game Over"
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or \
        guess_col not in range(5):
            print ("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print( "You guessed that one already." )
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print ("Game Over")




def digit_sum(n):
    sum = 0
    right = n
    left = n
    while left > 0:
        right = left%10
        left = left//10
        sum = sum + right
    return sum


def factorial(x):
  x = int(x)
  factor = 1
  for i in range(x):
    factor = factor*(i+1)
  return factor


def factorial(x):
    total = 1
    while x>0:
        total = total*x
        x-=1
    return total


def is_prime(x):
    if x < 2:
        return False
    for n in range(2, x-1):
        if x % n == 0:
            return False
        return True

#for loop
def reverse(text):
    y = ""
    length = len(text)
    for i in range(length):
        x = length -1 - i
        t = text[x]
        y = y + t
    return y
reverse('Python!')


#while loop
def reverse(text):
    y = ""
    l = len(text)
    while l > 0:
        x = l - 1
        y = y + text[x]
        l -= 1
    return y

def anti_vowel(text):
    initial = ""
    for i in text:
        for c in "aeiouAEIOU":
            if i == c:
                i = ""
            else:
                i = i
        initial = initial + i
    return initial

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
score["a"]

def scrabble_score(word):
    word = str(word)
    word = word.lower()
    scores = 0
    for i in word:
        t = score[i]
        scores += t
    return scores

def censor(text,word):
    final = ""
    length = len(word)
    for word in text:

#This is the end of code
