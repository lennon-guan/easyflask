import os
from cmds import register_cmd
from utils import *

@register_cmd
def cmd_blueprint(args):
    project_root = os.getcwd()
    bp_name = args[0]
    bp_url = args[1] if len(args) > 1 else '/' + bp_name
    bp_dir = os.path.join(project_root, 'application', 'blueprints', bp_name)
    if os.path.exists(bp_dir):
        print('blueprint dir {0} is exists'.format(bp_name))
        return 0
    if not os.path.exists(os.path.join(project_root, 'application', 'blueprints')):
        mkdir_p(project_root, 'application/blueprints')
        with open(os.path.join(project_root, 'application', 'blueprints', '__init__.py'), 'w') as outf:
            outf.write('\n')
    create_file(
        project_root,
        'application/blueprint/__init__.py',
        'application/blueprints/{0}/__init__.py'.format(bp_name),
        name=bp_name,
    )
    create_file(
        project_root,
        'application/blueprint/controllers/__init__.py',
        'application/blueprints/{0}/controllers/__init__.py'.format(bp_name),
    )
    code_lines = open(os.path.join(project_root, 'application', '__init__.py')).readlines()
    begin_idx = code_lines.index('    # BEGIN IMPORT BLUEPRINTS\n') + 1
    end_idx = code_lines.index('    # END IMPORT BLUEPRINTS\n')
    if end_idx - begin_idx < 2:
        new_lines = [
            '    import application.blueprints.{}\n'.format(bp_name),
            '    app.register_blueprint(blueprints.{0}.blueprint, url_prefix=\'{1}\')\n'.format(bp_name, bp_url),
        ]
    else:
        new_lines = code_lines[begin_idx: end_idx] + [
            '    import application.blueprints.{}\n'.format(bp_name),
            '    app.register_blueprint(blueprints.{0}.blueprint, url_prefix=\'{1}\')\n'.format(bp_name, bp_url),
        ]
    with open(os.path.join(project_root, 'application', '__init__.py'), 'w') as outf:
        outf.write(''.join(code_lines[:begin_idx] + new_lines + code_lines[end_idx:]))
