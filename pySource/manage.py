import os
from app import create_app
from flask_script import Manager, Shell, Server, Command
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

class init_db(Command):
    def run(self):
        from app import db
        with app.app_context():
            db.init_db()
manager.add_command("init-db", init_db())

def make_shell_context():
    return dict(app=app)#, db=db, User=User, Role=Role, Photo=Photo)
manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command("runserver", Server(host='127.0.0.1'))



if __name__ == '__main__':
    manager.run()
