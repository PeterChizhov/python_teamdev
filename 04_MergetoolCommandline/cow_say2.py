import cmd
import shlex
import cowsay
import argparse

# list_cows, make_bubble, cowsay и cowthink
parser = argparse.ArgumentParser()
parser.add_argument('message', nargs='?', default = '',
                    help='message you want cow to say')
parser.add_argument('-e', dest='eye_string', default='OO', type=str,
                    help='select the appearance of the cow\'s eyes')
parser.add_argument('-T', dest='tongue_string', default='  ', type=str,
                    help='select the appearance of the cow\'s tongue') 
parser.add_argument('-f', dest='cow', default='default', type=str,
                    help='set cowfile')                      

class cmdLine(cmd.Cmd):
    intro = 'Hello!'
    prompt = '>>>> '
    
    def do_cowsay(self, args):
        '''
        prints cow, you can choose message, cow, eyes, tongue:
        message : positional argument
        -f cowname
        -e eye_string
        -T tongue_string    
        '''
        # print(message, cowname, eye_string, tongue_string)
        print(args)
        print(shlex.split(args))
        # print(parser.parse_args(args.split()))
        params = parser.parse_args(shlex.split(args))
        print(cowsay.cowsay(message = params.message, 
                            cow = params.cow,
                            eyes = params.eye_string[:2],
                            tongue = params.tongue_string[:2]))


    def do_exit(self, arg):
        'exit cmd'  
        return 1    


if __name__ == '__main__':
    cmdLine().cmdloop()