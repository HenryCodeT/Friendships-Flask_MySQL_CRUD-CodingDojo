from friendships_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_users_friendships(cls):
        # query = '''
        #         SELECT *  FROM users
        #         JOIN friendships ON users.id = friendships.user_id 
        #         JOIN users AS users2 ON users2.id = friendships.friend_id;
        #         '''
        query = '''
                SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name  FROM users
                JOIN friendships ON users.id = friendships.user_id 
                LEFT JOIN users AS users2 ON users2.id = friendships.friend_id;
                '''
        response_query = connectToMySQL('friendships_1').query_db(query)

        return response_query

    @classmethod
    def create_user(cls,data):
        query = '''
                INSERT INTO users (first_name,last_name)
                VALUES(%(first_name)s,%(last_name)s)
                '''
        response_query = connectToMySQL('friendships_1').query_db(query,data)
        return response_query
    
    @classmethod
    def get_all_users(cls):
        query = '''
                SELECT * FROM users
                '''
        response_query = connectToMySQL('friendships_1').query_db(query)
        users = []
        for user in response_query:
            users.append(cls(user))
        return users