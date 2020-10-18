from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()

with app.app_context():
    username = input("Enter name: ")

    if User.query.filter(User.username == username).count():
        print("User with this name is already exists")
        sys.exit(0)

    password1 = getpass("Enter password: ")
    password2 = getpass("Repeat password: ")

    if not password1 == password2:
        print("Passwords are not the same")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print("User has been created id = {}".format(new_user.id))