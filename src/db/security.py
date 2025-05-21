import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
#         minutes=ACCESS_TOKEN_EXPIRE_MINUTES
#     )
#     to_encode.update({"exp": expire})
#     encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
