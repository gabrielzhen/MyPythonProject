import json
def get_user_name():
    try:
        with open('username.json') as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_name():
    username=input('Enter you user name!')
    with open('username.json','w') as f_obj:
        json.dump(username,f_obj)
    return username

def guess_user():
    username=get_user_name()
    if username:
        print('welcome'+str(username))
    else:
        username=get_new_name()
        print('we will remember you'+username)

guess_user()