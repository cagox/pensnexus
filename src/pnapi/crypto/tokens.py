import os
from datetime import datetime, timedelta, timezone

import jwt

# TODO : Update this once config code is in place, then get this from the config file.
SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = "HS256"


def create_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)

    return jwt.encode(
        {
            "sub": str(user_id),
            "iat": now,
            "exp": now + timedelta(minutes=15),
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )