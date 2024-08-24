class User:
    count = 0
    def add(self):
        self.count += 1
        return self.count

user = User()
print(user.add())
print(user.add())
print(user.add())
print(user.add())
print(user.add())
print(user.add())