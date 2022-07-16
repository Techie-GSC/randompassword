from cmd import PROMPT
import random

## characters to generate password from


def generate_random_password():

    #Clear old password.txt file
    f = open("passwords.txt", "w")
    f.write("")
    f.close()

    times = input(" How many passwords shall I generate for you, sir?")
    run = int(times)
    for run in range(run): 
        with open('words.txt') as f:
            words = f.read().split()
            word = random.choice(words)

        chars = list("!@#$%^&*()+={}[]<>;:")

        numbs = random.randrange(1,5)
        num_list = random.sample(range(1, 9), numbs)
        num = ''.join(str(e) for e in num_list)

        char = random.choice(chars)

        pas=""
        seq = word, num, char
        s = list(seq)
        y = random.sample(s, len(s))
        write = (pas.join(y))
        topas = write.join( "\n " )

        f = open("passwords.txt", "a")
        f.write(topas)
        f.close()  


## invoking the function
generate_random_password()