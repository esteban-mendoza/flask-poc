from weakref import ref

from flask.views import MethodView
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

from db import db
from middleware.blocklist import BLOCKLIST
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", __name__, description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(409, message="A user with that username already exists.")
        except Exception as e:
            abort(500, message=f"An error occurred while registering the user: {e}")

        return {"message": "User registered successfully."}, 201


@blp.route("/login")
class UserLogin(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")


@blp.route("/refresh")
class TokenRefresh(MethodView):

    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        access_token = create_access_token(identity=user_id, fresh=False)
        return {"access_token": access_token}, 200


@blp.route("/logout")
class UserLogout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "User logged out."}, 200


@blp.route("/user/<int:user_id>")
class User(MethodView):

    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted."}, 200
