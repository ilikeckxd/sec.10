"""
# 10-5 mutable default arguments
def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)
    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a2)



# 10-3 Argument Mutability

friends_last_seen = {
    'John': 5,
    'Everest': 0,
    'Saskia': 100
}


def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['John']))
see_friend(friends_last_seen, 'John')
print(id(friends_last_seen['John']))
print(id(friends_last_seen))



# 10-2 Mutability

friends_last_seen = {
    'John': 5,
    'Everest': 0,
    'Saskia': 100
}

print(id(friends_last_seen))
# 每次run都會不一樣


friends_last_seen = {
    'John': 5,
    'Everest': 0,
    'Saskia': 100
}

print(id(friends_last_seen))
friends_last_seen['John'] = 0
print(id(friends_last_seen))  # 跟前2行的會一樣 因為只是更改資料 不是創造新的Object
# =>dictionary is mutable.
# int, float, str, tuple => immutable

"""
