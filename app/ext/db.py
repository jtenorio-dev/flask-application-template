from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from sqlalchemy import text

__all__ = ['db', 'migrate', 'ma', 'init', 'bcrypt']

convention = {
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
migrate = Migrate(render_as_batch=True)

def init(app):
    db.init_app(app)
    migrate.init_app(app, db)

    context = app.app_context()
    context.push()
    engine = db.engine
    if engine.dialect.name == 'sqlite':
        db.session.execute(text('PRAGMA foreign_keys=ON'))
        db.session.commit()
    context.pop()

    import app.models as _