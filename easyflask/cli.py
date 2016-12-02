# coding: utf-8

from __future__ import print_function
import sys
import cmd_new
import cmd_blueprint
import cmd_controller
import cmd_model
import cmds

def main(args=None, options=None):
    if not args:
        args = sys.argv[1:]
    if not args:
        print('Usage: easyflask <command>...')
        print('Available commands:')
        for cmd in cmds.cmd_map.keys():
            print('\t{0}'.format(cmd))
        return 1
    cmd, args = args[0], args[1:]
    if cmd not in cmds.cmd_map:
        print('No this command {0}'.format(cmd))
        print('Available commands:')
        for cmd in cmds.cmd_map.keys():
            print('\t{0}'.format(cmd))
        return 1
    return cmds.cmd_map[cmd](args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)

