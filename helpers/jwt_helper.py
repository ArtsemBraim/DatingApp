from authentication.models import CustomUser
from datetime import datetime, timedelta
from dating_app import settings
import jwt


class JWTHelper:
    JWT_ALGORITHM = 'HS256'
    JWT_UTF = 'utf-8'
    JWT_TOKEN_EXPIRY = getattr(settings, 'JWT_TOKEN_EXPIRY', 7)

    @staticmethod
    def encode_token(user):
        if user:
            data = {
                "exp": datetime.utcnow() + timedelta(days=JWTHelper.JWT_TOKEN_EXPIRY),
                "username": user.username,
            }
            token = jwt.encode(data, 'secret', algorithm=JWTHelper.JWT_ALGORITHM)
            return token
        raise CustomUser.DoesNotExist

    @staticmethod
    def is_token_valid(token):
        try:
            jwt.decode(token, 'secret', algorithms=JWTHelper.JWT_ALGORITHM)
            return True, "Valid"
        except jwt.ExpiredSignatureError:
            return False, "Token Expired"
        except jwt.InvalidTokenError:
            return False, "Token is Invalid"

    @staticmethod
    def decode_token(token):
        username_dict = jwt.decode(token, 'secret', algorithms=JWTHelper.JWT_ALGORITHM)
        return CustomUser.objects.filter(username=username_dict["username"]).first()
