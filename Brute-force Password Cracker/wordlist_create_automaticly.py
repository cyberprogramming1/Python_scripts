import random
import string

def generate_wordlist(num_words, word_length):
    wordlist = []
    letters = string.ascii_lowercase  
    
    for _ in range(num_words):
        word = ''.join(random.choice(letters) for _ in range(word_length))
        wordlist.append(word)
    
    return wordlist

# Parameters
num_words = 500  
word_length = 10 


random_wordlist = generate_wordlist(num_words, word_length)

# Save wordlist to a file
with open('random_wordlist.txt', 'w') as f:
    for word in random_wordlist:
        f.write(word + '\n')

print(f"Wordlist with {num_words} words generated and saved to 'random_wordlist.txt'")
