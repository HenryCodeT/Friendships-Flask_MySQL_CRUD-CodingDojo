from flask import Flask, redirect, render_template, request, session
from friendships_app import app
from friendships_app.models.model_user import User
from friendships_app.models.model_friend import Friend

@app.route("/")
def index(): 
    return redirect("/friendships")

@app.route("/friendships")
def friendship():
    
    response_query_users_friendships = User.get_users_friendships()
    response_query_users = User.get_all_users()
    return render_template("index.html",users_friends=response_query_users_friendships,users=response_query_users)

@app.route("/create-user",methods = ['POST'])
def create_user_post():
    data = {
        'first_name':request.form['name'],
        'last_name':request.form['lastname']
    }
    response_query=User.create_user(data)
    return redirect("/")

@app.route("/create-friendships",methods = ['POST'])
def create_friendships():
    friendships=Friend.get_friendships()
    
    def validate_data_before_post(data):
        stage=True
        if data['friend_id'] == data['user_id']:
            stage=False
            return stage  
        for friendship in friendships:
            if friendship.user_id==data['user_id'] and friendship.friend_id==data['friend_id']:
                stage=False
                break
            elif friendship.user_id==data['friend_id'] and friendship.friend_id==data['user_id']:
                stage=False
                break
        return  stage
    data = {
        'friend_id':request.form.get('friend_id',type=int),
        'user_id':request.form.get('user_id',type=int)
    }
    validation= validate_data_before_post(data)
    if validation == True:
        result=Friend.create_friendships(data)
        print(result,"se creo una nueva amistad")
    else:
        print("No se creo una nueva amistad")
    return redirect("/")

