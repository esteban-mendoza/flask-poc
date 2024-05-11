from flask import jsonify
from flask_jwt_extended import JWTManager

from middleware.blocklist import BLOCKLIST


class JWTManager(JWTManager):

    def __init__(self, app=None):
        super().__init__(app)

        self.token_in_blocklist_loader(self.check_if_token_in_blocklist)
        self.revoked_token_loader(self.revoked_token_callback)
        self.expired_token_loader(self.expired_token_callback)
        self.invalid_token_loader(self.invalid_token_callback)
        self.unauthorized_loader(self.missing_token_callback)
        self.needs_fresh_token_loader(self.token_not_fresh_callback)

    def token_not_fresh_callback(self, jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "Fresh token required",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    def check_if_token_in_blocklist(self, jwt_header, jwt_payload):
        """
        This method is called to check if a token is blacklisted. It should
        return True if the token has been blacklisted, and False otherwise.
        """
        return jwt_payload["jti"] in BLOCKLIST

    def revoked_token_callback(self, jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token has been revoked", "error": "token_revoked"}
            ),
            401,
        )

    def expired_token_callback(self, jwt_header, jwt_payload):
        return (
            jsonify({"description": "The token has expired", "error": "token_expired"}),
            401,
        )

    def invalid_token_callback(self, error):
        return (
            jsonify(
                {
                    "description": "Signature verification failed",
                    "error": "invalid_token",
                }
            ),
            401,
        )

    def missing_token_callback(self, error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token",
                    "error": "authorization_required",
                }
            ),
            401,
        )
