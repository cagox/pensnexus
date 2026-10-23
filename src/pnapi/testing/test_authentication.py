from ..config import settings
from ..models import User
from ..db.db import engine
from sqlalchemy.orm import Session

print("Testing authentication...")
input_email = input("Enter email to test: ").strip().lower()
input_password = input("Enter password to test: ").strip()


with Session(engine) as session:
    user = User.get_by_email(session, input_email)
    if user and user.verify_password(input_password):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

#TODO: Update this script or create a new one once TOTP code is in place.