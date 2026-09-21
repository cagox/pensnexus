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
  
# SQLAlchemy
10. set up venv and activate
11. sudo apt install libpq-dev
- On Production Machine: pip install -r requirements.txt 
- But, the following is what I did on the local machine.
12. pip install psycopg2
13. pip install alembic
14. pip install "fastapi[standard]"
15. python -Im pip install argon2-cffi # For password hashing
16. 



