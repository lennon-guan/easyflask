#coding: utf-8

from flask import Flask
from playhouse.flask_utils import FlaskDB
from werkzeug.contrib.fixers import ProxyFix
from config import load_config


def create_app():
    config = load_config()
    app = Flask(__name__)
    app.config.from_object(config)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    _init_db(app)
    _init_templates(app)
    _init_blueprints(app)
    _init_admin(app)

    return app

db = FlaskDB()

def _init_db(app):
    db_conf = app.config.get('DATABASE', None)
    if db_conf is None:
        return
    db.init_app(app)
    def _close_db(exc):
        if not db.is_closed():
            db.close()
    # adding get_or_none method into peewee
    def _select_get_or_none(self):
        try:
            return self.get()
        except peewee.DoesNotExist as e:
            return None
    def _model_get_or_none(cls, *query, **kwargs):
        try:
            return cls.get(*query, **kwargs)
        except peewee.DoesNotExist as e:
            return None
    import peewee
    peewee.SelectQuery.get_or_none = _select_get_or_none
    peewee.Model.get_or_none = classmethod(_model_get_or_none)
    if 'DATABASE_LOG_LEVEL' in app.config:
        peewee.logger.setLevel(app.config['DATABASE_LOG_LEVEL'])

def _init_templates(app):
    pass


def _init_blueprints(app):
    # this function is generated by easyflask. do NOT modify it
    # BEGIN IMPORT BLUEPRINTS
    pass
    # END IMPORT BLUEPRINTS

def _init_admin(app):
    # import flask_admin
    # from application.models import *
    # from application.admin.xxx_modelview import XXXModelView
    # admin_app = flask_admin.Admin(app, name='Your Admin Name')
    # admin_app.add_view(XXXModelView(XXXModel, name='XXX'))
    pass
