# Tech

Using postgresql, Python, and React

# Setup Steps on Ubuntu 26.04


# SQL Server
1. sudo apt install postgresql
2. sudo vim /etc/postgresql/18/main/pg_hba.conf
- Find the first entry that says local all postgress peer
- Temporarily change peer to trust
3. psql -U postgress
- Once logged into postgress
    \password
- Assign a password you will remember. Then exit postgress.
- Go back to pg_hba.conf and set that line back to peer.
4. psql -U postgress
5. CREATE USER ficsiteuser WITH PASSWORD 'your_password';    # use info from config.json
6. CREATE DATABASE ficsite OWNER ficsiteuser;
7. exit
8. psql -U ficsiteuser ficsite
9. CREATE EXTENSION IF NOT EXISTS citext;

# Redis Server
10. sudo apt install redis
11. TBD (I still need to make sure I know how to set up and configure redis)
  
# SQLAlchemy
12. set up venv and activate
13. sudo apt install libpq-dev
- On Production Machine: pip install -r requirements.txt 
- But, the following is what I did on the local machine.
14. pip install psycopg2
15. pip install alembic
16. pip install "fastapi[standard]"
17. python -Im pip install argon2-cffi # For password hashing
18. pip install uuid6 # I will use this for generating keys to facilitate eventual database replication

# Useful Commands
## Generate and encrypt the HMAC session key directly:
python3 -c "import secrets; print(secrets.token_urlsafe(32), end='')" | sudo systemd-creds encrypt --with-key=host - session_secret.cred

## Generate and encrypt the password pepper:
python3 -c "import secrets; print(secrets.token_urlsafe(32), end='')" | sudo systemd-creds encrypt --with-key=host - password_pepper.cred


## Run the dev server with the right variables
CONFIG_PATH="$HOME/workspace/github/cagox/pensnexus/docs/ficsiteconf.json" \
SESSION_SECRET="$(systemd-creds decrypt "$HOME/temp/session_secret.cred" -)" \
PASSWORD_PEPPER="$(systemd-creds decrypt "$HOME/temp/password_pepper.cred" -)" \
DB_PASSWORD="$(systemd-creds decrypt "$HOME/temp/db_password.cred" -)" \
exec uvicorn main:app --reload

# Run Alembic
## To initialize or update schema
CONFIG_PATH="$HOME/workspace/github/cagox/pensnexus/docs/ficsiteconf.json" \
SESSION_SECRET="$(sudo systemd-creds decrypt "$HOME/temp/session_secret.cred" -)" \
PEPPER="$(sudo systemd-creds decrypt "$HOME/temp/password_pepper.cred" -)" \
DB_PASSWORD="$(sudo systemd-creds decrypt "$HOME/temp/db_password.cred" -)" \
alembic revision --autogenerate -m "initial schema"

Change the message after -m when making changes.

## To apply the update
CONFIG_PATH="$HOME/workspace/github/cagox/pensnexus/docs/ficsiteconf.json" \
SESSION_SECRET="$(sudo systemd-creds decrypt "$HOME/temp/session_secret.cred" -)" \
PEPPER="$(sudo systemd-creds decrypt "$HOME/temp/password_pepper.cred" -)" \
DB_PASSWORD="$(sudo systemd-creds decrypt "$HOME/temp/db_password.cred" -)" \
alembic upgrade head




alembic upgrade head


CONFIG_PATH="$HOME/workspace/github/cagox/pensnexus/docs/ficsiteconf.json" \
SESSION_SECRET="$(sudo systemd-creds decrypt "$HOME/temp/session_secret.cred" -)" \
PEPPER="$(sudo systemd-creds decrypt "$HOME/temp/password_pepper.cred" -)" \
DB_PASSWORD="$(sudo systemd-creds decrypt "$HOME/temp/db_password.cred" -)" \
alembic revision --autogenerate -m "adding is_admin to user"