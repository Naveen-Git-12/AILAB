import random
word = input("Word to find: ").upper()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# initial random guess
guess = "".join(random.choice(abc) for _ in word)

step = 0
while True:
    print("Step", step, ":", guess)
    if guess == word:
        print("Found 🎉 ->", word)
        break
    
    new = list(guess)  # convert to list for easy updates
    for i in range(len(word)):
        if guess[i] != word[i]:  # only change wrong characters
            new[i] = random.choice(abc)
    guess = "".join(new)
    
    step += 1
