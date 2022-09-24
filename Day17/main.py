class User:
    def __init__(self, name, followers, following):
        self.__name = name
        self.__followers = followers
        self.__following = following

    def get_name(self):
        return self.__name

    def get_followers(self):
        return self.__followers

    def get_following(self):
        return self.__following

    def set_followers(self, followers):
        self.__followers = followers

    def set_following(self, following):
        self.__following = following

    def follow_another_user(self, user):
        self.set_following(self.get_following() + 1)
        user.set_followers(user.get_followers() + 1)


user1 = User("Marin", 10, 1)
user2 = User("Ante", 100, 50)
user1.follow_another_user(user2)
print(user1.get_following(), user2.get_followers())

