import bullscows
import cowsay
import argparse 
import urllib.request
import random

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
    cows_types = cowsay.list_cows()
    print(cowsay.cowsay(message = prompt,
                        cow = random.choice(cows_types)))
    guess = input()
    guess = guess[:length]
    if valid is None:
        return guess

    while not guess in valid:
        print()
        print(cowsay.cowsay(message = f"Слово должно быть длины {length}, и из словаря. \n" + prompt,
                            cow = random.choice(cows_types)))
        guess = input()
        guess = guess[:length]
    return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    cows_types = cowsay.list_cows()
    print(cowsay.cowsay(message = format_string.format(bulls, cows), 
                        cow = random.choice(cows_types)))

bullscows.gameplay(ask=ask, inform=inform, words=fix_length_vocab)   