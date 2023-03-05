import cmd
import shlex
import cowsay
import argparse
import pyreadline3
import sys

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

        params = parser.parse_args(shlex.split(args))
        print(cowsay.cowsay(message = params.message, 
                            cow = params.cow,
                            eyes = params.eye_string[:2],
                            tongue = params.tongue_string[:2]))
   
    def complete_cowsay(self, pfx, line, beg, end):
        cows_lst = cowsay.list_cows()
        eye_lst = ['00', 'oo', 'XX']
        tongue_lst = ['U ', '__', '\/']
        key_lst = ['-f', '-T', '-e']
        # tmp_lst = []
        tmp_lst = key_lst
        if line[beg-3:beg].strip() == '-f': 
            tmp_lst = cows_lst
        elif line[beg-3:beg].strip() == '-T': 
            tmp_lst = tongue_lst
        elif line[beg-3:beg].strip() == '-e':
            tmp_lst = eye_lst         
        return [s for s in tmp_lst if s.startswith(pfx)]   
                   
    def do_list_cows(self, arg):
        'list availible cows'
        print(*cowsay.list_cows())                        


    def do_exit(self, arg):
        'exit cmd'  
        return 1    


if __name__ == '__main__':
    cmdLine().cmdloop()