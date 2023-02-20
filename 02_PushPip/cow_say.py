import argparse # command line parsing module
import cowsay


parser = argparse.ArgumentParser()
parser.add_argument('message', help = 'message you want cow to say')
args = parser.parse_args()


print(cowsay.cowsay(args.message))