import os
from cmds import register_cmd
from utils import *

@register_cmd
def cmd_controller(args):
    project_root = os.getcwd()
    bp_name = args[0]
    if not os.path.exists(os.path.join(project_root, 'application', 'blueprints', bp_name)):
        import cmd_blueprint
        cmd_blueprint.cmd_blueprint([bp_name])
    ct_names = args[1].split(',')
    for ct_name in ct_names:
        ct_dir = os.path.join(project_root, 'application', bp_name, 'controllers')
        ct_path = os.path.join(ct_dir, ct_name + '.py')
        if os.path.exists(ct_path):
            print('controller {0}.{1} is exists'.format(bp_name, ct_name))
            continue
        create_file(
            project_root,
            'application/blueprint/controllers/blank.py',
            'application/blueprints/{0}/controllers/{1}.py'.format(bp_name, ct_name),
        )
        code_lines = open(os.path.join(project_root, 'application', 'blueprints',
                        bp_name, 'controllers', '__init__.py')).readlines()
        begin_idx = code_lines.index('# BEGIN IMPORT FILES\n') + 1
        end_idx = code_lines.index('# END IMPORT FILES\n')
        new_lines = code_lines[begin_idx: end_idx] + [
            '\n',
            'import application.blueprints.{0}.controllers.{1}\n'.format(bp_name, ct_name),
        ]
        with open(os.path.join(project_root, 'application', 'blueprints',
                                bp_name, 'controllers', '__init__.py'), 'w') as outf:
            outf.write(''.join(code_lines[:begin_idx] + new_lines + code_lines[end_idx:]))

