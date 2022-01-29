from friendships_app.config.mysqlconnection import connectToMySQL

class Friend:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.friend_id=data['friend_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_friendships(cls):
        query = '''
                SELECT * FROM friendships
                '''
        response_query_friendships=connectToMySQL('friendships_1').query_db(query)
        friendships = []
        for friendship in response_query_friendships:
            friendships.append(cls(friendship))
        return friendships
    
    @classmethod
    def create_friendships(cls,data):
        query = '''
                INSERT INTO friendships (user_id,friend_id)
                VALUES (%(user_id)s,%(friend_id)s)
                '''
        response_query_create_friendships=connectToMySQL('friendships_1').query_db(query,data)
        return response_query_create_friendships