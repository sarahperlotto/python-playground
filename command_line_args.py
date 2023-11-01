import sys
from distutils.core import setup

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

try:
    env = sys.argv[1]
except IndexError:
    env = 'dev'
print('Env: ', env)


try:
    idx = sys.argv.index('--env')
    sys.argv.pop(idx)
    env_arg = sys.argv.pop(idx)
except (ValueError, IndexError):
    env_arg = 'dev'
print('Env arg: ', env_arg)

# except ValueError
# if '--env' in sys.argv:
#     idx = sys.argv.index('--env')
#     sys.argv.pop(idx)
#     env_arg = sys.argv.pop(idx)
# print('Env arg: ', env_arg)
