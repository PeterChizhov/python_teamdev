import argparse # command line parsing module
import cowsay


parser = argparse.ArgumentParser()
parser.add_argument('message',
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

args = parser.parse_args()
# -[bdgpstwy]

no_preset_flag = True
for preset in preset_names[::-1]:
    if args.__dict__[preset]:
        no_preset_flag = False
        break 

if no_preset_flag:
    preset = None

print(args.__dict__)

print(cowsay.cowsay(message = args.message, 
                    preset = preset,
                    eyes = args.eye_string[:2],
                    tongue = args.tongue_string[:2]))