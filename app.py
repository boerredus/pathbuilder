import sys
import os

program = sys.argv[1]
args = ' '.join(sys.argv[2:])

os.system('{} "{}"'.format(program, args))
