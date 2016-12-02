import os
import re

__all__ = [
    'mkdir_p',
    'render_template',
    'rewrite_file',
    'create_file',
    'to_snake',
]

def mkdir_p(root, path):
    paths = path.split('/')
    for i in range(len(paths)):
        dst_path = os.path.join(root, *paths[:i + 1])
        if os.path.isdir(dst_path):
            continue
        if os.path.exists(dst_path):
            raise ValueError('{0} exists but not a directory'.format(dst_path))
        os.mkdir(dst_path)
    return os.path.join(root, path)
    
def render_template(template_path, **kwargs):
    src_dir = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(src_dir, 'templates', template_path) + '.tpl'
    with open(template_path) as inf:
        template_str = inf.read()
        output = template_str.format(**kwargs)
        return output

def _write_file(project_root, template_path, dst_path, rewrite_if_exists, **kwargs):
    if dst_path is None:
        dst_path = template_path
    mkdir_p(project_root, os.path.dirname(dst_path))
    dst_abs_path = os.path.join(project_root, dst_path)
    if os.path.exists(dst_abs_path) and not rewrite_if_exists:
        print('{0} exists. Skip it'.format(dst_abs_path))
        return
    with open(dst_abs_path, 'w') as outf:
        outf.write(render_template(template_path, **kwargs))
        print('render {1} into {0}'.format(dst_abs_path, template_path))
    
def rewrite_file(project_root, template_path, dst_path=None, **kwargs):
    _write_file(project_root, template_path, dst_path, True, **kwargs)

def create_file(project_root, template_path, dst_path=None, **kwargs):
    _write_file(project_root, template_path, dst_path, False, **kwargs)

def to_snake(camel_name):
    return '_'.join([x.lower() for x in re.findall(r'[A-Z][a-z0-9]*', camel_name)])
