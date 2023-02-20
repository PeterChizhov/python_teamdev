import argparse # command line parsing module
import cowsay
import sys


parser = argparse.ArgumentParser()
parser.add_argument('message', nargs='?', default = '',
                    help='message you want cow to say')

preset_names = ['b', 'd', 'g', 'p', 's', 't', 'w', 'y']
preset_helps = ['initiates Borg mode',
                 'causes the cow to appear dead',
                 'invokes greedy mode',
                 'causes a state of paranoia to come over the cow',
                 'makes the cow appear thoroughly stoned',
                 'yields a tired cow',
                 'is somewhat the opposite of -t, and initiates wired mode',
                 'brings on the cow\'s youthful appearance']

for name, help in zip(preset_names, preset_helps):
    parser.add_argument('-' + name,
                        help=help,
                        action='store_true'
                        )
# adding eye and tongue
parser.add_argument('-e', dest='eye_string', default='OO', type=str,
                    help='select the appearance of the cow\'s eyes')
parser.add_argument('-T', dest='tongue_string', default='  ', type=str,
                    help='select the appearance of the cow\'s tongue')   
# add -l
parser.add_argument('-l', action= 'store_true',
                    help='To list all cowfiles on the current COWPATH')                                      

parser.add_argument('-W', dest='width', default=40, type=int,
                    help='choose width of text in symbols')
# disable wrapping (-n)
parser.add_argument('-n', action='store_true',
                    help='disables text wrapping')                     
# -f cowfile
parser.add_argument('-f', dest='cowfile', default='default', type=str,
                    help='set cowfile')
args = parser.parse_args()

if args.l:
    print(*cowsay.list_cows())
else:
    # -[bdgpstwy]
    no_preset_flag = True
    for preset in preset_names[::-1]:
        if args.__dict__[preset]:
            no_preset_flag = False
            break 

    if no_preset_flag:
        preset = None
        
    if '/' in args.cowfile:
        cow_name = 'default'
        cowfile = args.cowfile
    else:
        cow_name = args.cowfile
        cowfile = None 
        
    # stdin if positional message is default
    if not args.message:
        lines = []
        for line in sys.stdin:
            lines.append(line.strip())
        message = '\n'.join(lines)
    else:
        message = args.message    

    print(cowsay.cowsay(message = message, 
                    cow = cow_name,
                    preset = preset,
                    eyes = args.eye_string[:2],
                    tongue = args.tongue_string[:2],
                    width = args.width,
                    wrap_text = not args.n,
                    cowfile=cowfile))