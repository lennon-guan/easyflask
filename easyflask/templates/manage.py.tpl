# coding: utf-8

import sys
from flask.ext.script import Manager
from application import create_app
from config import load_config

app = create_app()
manager = Manager(app)

@manager.command
def run():
    config = load_config()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

@manager.command
def create_tables():
    from application import db
    from application.models import all_models
    from peewee import create_model_tables
    create_model_tables(all_models, fail_silently=True)

@manager.command
def drop_tables():
    from application import db
    from application.models import all_models
    from peewee import drop_model_tables
    drop_model_tables(all_models, fail_silently=True)

@manager.command
def add_model(model_name):
    import application.models as m
    model_cls = getattr(m, model_name)
    fields = {{}}
    for field in model_cls._meta.sorted_fields:
        tips = '\t{{0}}: '.format(field.name)
        if sys.version_info[0] == 2:
            val = raw_input(tips)
        else:
            val = input(tips)
        fields[field.name] = field.coerce(val)
    model = model_cls(**fields)
    model.save()

if __name__ == "__main__":
    manager.run()

