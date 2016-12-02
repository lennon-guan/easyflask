import os
from cmds import register_cmd
from utils import *

@register_cmd
def cmd_model(args):
    project_root = os.getcwd()
    model_names = args[0].split(',')
    if len(args) > 1:
        base_name = args[1]
        if not base_name.endswith('Model'):
            raise ValueError('base model name must ends with "Model"')
        if base_name == 'db.Model':
            import_base = 'from application import db'
        else:
            import_base = 'from .{0} import {1}'.format(
                    to_snake(base_name), base_name)
    else:
        base_name = 'db.Model'
        import_base = 'from application import db'
    for model_name in model_names:
        if not model_name.endswith('Model'):
            raise ValueError('model name must ends with "Model"')
        if not model_name[0].isupper():
            model_name = model_name[0].upper() + model_name[1:]
        model_filename = to_snake(model_name)
        if os.path.exists(os.path.join(project_root, 'application', 'models', model_filename + '.py')):
            print('model {0} is exists'.format(model_name))
            continue
        create_file(
            project_root,
            'application/models/__init__.py',
        )
        create_file(
            project_root,
            'application/models/model.py',
            'application/models/{0}.py'.format(model_filename),
            base_name=base_name,
            model_name=model_name,
            import_base=import_base,
            table=model_filename[:-6],
        )

    code_lines = open(os.path.join(project_root, 'application', 'models', '__init__.py')).readlines()
    begin_idx = code_lines.index('# BEGIN IMPORT FILES\n') + 1
    end_idx = code_lines.index('# END IMPORT FILES\n')
    new_lines = code_lines[begin_idx: end_idx] + [
        'from .{0} import {1}\n'.format(to_snake(model_name), model_name) for model_name in model_names
    ]
    code_lines = code_lines[:begin_idx] + new_lines + code_lines[end_idx:]

    begin_idx = code_lines.index('# BEGIN ALL_MODELS\n') + 1
    end_idx = code_lines.index('# END ALL_MODELS\n')
    new_lines = code_lines[begin_idx: end_idx] + [
        '    {0},\n'.format(model_name) for model_name in model_names
    ]
    code_lines = code_lines[:begin_idx] + new_lines + code_lines[end_idx:]

    with open(os.path.join(project_root, 'application', 'models', '__init__.py'), 'w') as outf:
        outf.write(''.join(code_lines))
