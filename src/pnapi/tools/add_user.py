from ..models.user import User
from ..models.profile import Profile
from sqlalchemy.orm import Session
from ..db.db import engine

def create_user_with_profile(session: Session):
   # Gather the information:
   print("We will ask you some questions.")
   email = input("Email: ").strip().lower()
   password = input("Password: ").strip()
   is_admin_input = input("Is this user an admin? (y/n): ").strip().lower()
   is_admin = is_admin_input == 'y'
   print("is_admin: ", is_admin)
   input("Press Enter to continue...")
   display_name = input("Default Display Name: ").strip()
   brief_bio = input("Brief Bio (optional): ").strip() or None

   # First we will create the user.
   new_user = User.create(email=email, password=password, is_admin=is_admin)
   new_user = new_user.commit_to_db(session)

   if not new_user.id:
       print("Failed to create user. Please check the input and try again.")
       return
   
   # Now we will create the profile.
   new_profile = Profile.create(user_id=new_user.id, display_name=display_name, bio=brief_bio)
   new_profile = new_profile.commit_to_db(session)

   if not new_profile.id:
       print("Failed to create profile. Please check the input and try again.")
       return


if __name__ == "__main__":
    with Session(engine) as session:
        create_user_with_profile(session)

