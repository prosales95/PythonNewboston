from operator import itemgetter
from operator import attrgetter


class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ":" + str(self.user_id)


users = [
    User('dsfs', 412),
    User('sdf', 234),
    User('gjhgh', 34),
    User('asf', 6542),
    User('fghbn', 1432),
    User('xvcx', 4133452),
]

for user in users:
    print(user)

print("----------")

for user in sorted(users, key=attrgetter('name')):
    print(user)
print("----------------")

for user in sorted(users, key=attrgetter( 'user_id')):
    print(user)

users = [
    {'fname': 'asdad', 'lname': 'sdfgvgsdf'},
    {'fname': 'fwef', 'lname': 'xcvxvc'},
    {'fname': 'dsf', 'lname': 'xcvvcx'},
    {'fname': 'dfsf', 'lname': 'xcvxv'},
    {'fname': 'dfssf', 'lname': 'ewrr'},
    {'fname': 'xbcvbx', 'lname': 'vcbvcb'},
    {'fname': 'xcvxcv', 'lname': 'cvxbbd'},
    {'fname': 'khzjg', 'lname': 'fdgdsg'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
