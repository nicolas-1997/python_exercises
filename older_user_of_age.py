def older_user_of_age(user):  #Function that indicates if a user is of legal age
    if user.age > 18:
        print(user.name, "is of legal age because he has", user.age)
    else:
        print(user.name, "is not of legal age because he has", user.age)



class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name

def run():
    user1 = User(25, "Nicolas")
    user2 = User(15, "Noelia")

    result1 = older_user_of_age(user1)
    result2 = older_user_of_age(user2)

    


if __name__ == "__main__":
    run()

