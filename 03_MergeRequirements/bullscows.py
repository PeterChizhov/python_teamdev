import random

def bullscows(guess: str, secret: str) -> (int, int):
    bulls_count = 0
    cows_count = 0
    for ch1, ch2 in zip(guess, secret):
        if ch1==ch2:
            bulls_count+=1
    
    guess_set = set(guess)
    for ch in guess_set:
        if ch in secret:
            cows_count+=1

    return bulls_count, cows_count        

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    print("Try to guess secret word")
    guess = ''
    number_of_tries = 0
    while (guess != secret):
        guess = ask("Введите слово: ", words)
        number_of_tries += 1
        bulls_count, cows_count = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls_count, cows_count)

    print(f'Well done! Total number of guesses: {number_of_tries}')    
    return number_of_tries

if __name__ == '__main__':
    import argparse 
    import urllib.request

    parser = argparse.ArgumentParser()
    parser.add_argument('vocab_ref', nargs='+', default = '',
                        help='first - file or url containing vocabluary, second - length of word (optional)')
    
    args = parser.parse_args()
    vocabulary = []
    length = 5

    if len(args.vocab_ref) > 1:
        length = int(args.vocab_ref[1])
    
    if args.vocab_ref[0].startswith('http'):
        with urllib.request.urlopen(args.vocab_ref[0]) as response:
            html = response.read()
        vocabulary = html.decode("utf8")
    else:
        with open(args.vocab_ref[0]) as f:
            vocabulary = f.read()
    
    vocabulary = vocabulary.split()
    fix_length_vocab = list(filter(lambda s: len(s) == length, vocabulary))

    def ask(prompt: str, valid: list[str] = None) -> str:
        guess = input(prompt)
        guess = guess[:length]
        if valid is None:
            return guess

        while not guess in valid:
            print(f"Слово должно быть длины {length}, и из словаря")
            guess = input(prompt)
            guess = guess[:length]
        return guess

    def inform(format_string: str, bulls: int, cows: int) -> None:
        print(format_string.format(bulls, cows))
    
    gameplay(ask=ask, inform=inform, words=fix_length_vocab)       



