import os
import os.path as osp
from cmds import register_cmd
from utils import *

def _build_root(project_root):
    create_file(project_root, 'manage.py')
    create_file(project_root, 'wsgi.py')
    create_file(project_root, 'requirements.txt')

def _build_config(project_root):
    rewrite_file(project_root, 'config/__init__.py')
    rewrite_file(project_root, 'config/default.py')

def _build_application(project_root):
    create_file(project_root, 'application/__init__.py')

@register_cmd
def cmd_new(args):
    if len(args) > 0:
        project_name = args[0]
        project_root = osp.join(os.getcwd(), project_name)
        mkdir_p(os.getcwd(), project_name)
    else:
        project_root = os.getcwd()
        project_name = osp.basename(project_root)
    _build_root(project_root) 
    _build_config(project_root)
    _build_application(project_root)
