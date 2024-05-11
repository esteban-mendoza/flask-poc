"""
This file contains the blocklist of the application. It will be used to check
whether a token is blacklisted or not. Here, we are using an in-memory set
to store the tokens. In a production application, you would use a more
persistent storage like Redis or a database to store the blocklist.
"""

BLOCKLIST = set()
