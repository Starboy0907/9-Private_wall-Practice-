from ..config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    db = "private_wall"
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.sent_by_id = data['sent_by_id']
        self.sent_to_id = data['sent_to_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.messages = []

    @classmethod
    def save(cls, data):
        query = "SELECT * from messages;"
        return connectToMySQL('private_wall')

    @classmethod
    def destroy(cls,data):
        query = "DELETE from messages WHERE message_id = %(id)s;"
        return connectToMySQL('private_wall').query_db(query)

