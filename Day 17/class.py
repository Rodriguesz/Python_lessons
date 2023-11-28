class Users:
    #class constructor
    def __init__(self, user_id, username):
        #self.attributes = parameters
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
         
    
user_1 = Users("001", "Leonardo")
user_2 = Users("002", "Leonardo")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)