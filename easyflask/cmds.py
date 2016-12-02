from functools import wraps

cmd_map = {}

def register_cmd(cmd_func):
    if not cmd_func.__name__.startswith('cmd_'):
        raise NameError('cmd func name must starts with "cmd_"')
    cmd_map[cmd_func.__name__[4:]] = cmd_func
    return cmd_func

