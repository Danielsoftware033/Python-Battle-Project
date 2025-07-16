




class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"You have successfully added {friend.username} as a friend.")

    def friends_list(self):
        print("===================")
        for friend in self.friends:
            print(friend.username)

    def create_post(self):
        post = input("What's on your mind?: ")
        self.posts.append(post)
        print(f"{self.username}: {post}")


    def display_posts(self):
        print("My posts")
        print("===============")
        for post in self.posts:
            print(post)




cameron = User("Curds", "cameron@email.com", "ilovecheese123")
joey = User("RobotDoctor", 'joey@email.com', 'robodocjoey')
arnett = User("ajm911", "arnett@email.com", "callmebeepme")
# print(cameron.username)
# print(joey.username)
# print(arnett.username)
# arnett.friends.append(cameron)
# #WHY DO YOU HAVE TO DEF APPEND METHOD, AND NOT JUST USE IT DIRECTLY

# #adding users to joeys friends list
# joey.add_friend(cameron)
# joey.add_friend(arnett)
# print(joey.friends)

# #calling the friends_list method
# joey.friends_list()

# #creating a post
# arnett.create_post()
# arnett.display_posts()



def fakebook():
    users = [cameron, joey, arnett]

    current_user = ''
    print("Would you like to: ")
    print("1) Login")
    print("2) Create an account")
    answer = input(": ")
    if answer == "1":
        print("login")
    else:
        print("Create Account")
        print("===============")
        username = input("What is your username?: ")
        email = input("Email: ")
        password = input("Password: ")
        new_user = User(username, email, password)
        users.append(new_user)
        current_user = new_user
        print(f"Welcome to Fakebook {new_user.username}")

    while True:
        print("Things to do:" \
        "1. Add Friend" \
        "2. View my friend" \
        "3. Create a post" \
        "4. View my posts"
        "5. Logout")

        choice = input("What would you like to do? :")
        if choice == '1':
            num = 1
            print("Potential friends")
            print("===================")
            for user in users:
                if current_user.username != user.username:
                  print(f"{num}.) {user.username}")
                num += 1

            num = int(input("Select friend by number: "))
            current_user.add_friend(users[num-1])
        elif choice == "2":
            current_user.friends_list()
        elif choice == '3':
            current_user.create_post()
        elif choice == '4':
            current_user.display_posts()
        elif choice == '5':
            print("Thanks for Fakebookin it, Bye!")
            break



fakebook()


               