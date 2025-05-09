
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
print(users)


def add_user(new_user):
    users.append(new_user)
    print(f"User added: {new_user}")


def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def update_user(user_id, updated_data):
    for user in users:
        if user["id"] == user_id:
            user.update(updated_data)
            print(f"User updated: {user}")
            return
    print(f"User with ID {user_id} not found.")


def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User with ID {user_id} deleted.")


add_user({"id": 3, "name": "Appi", "email": "appi@newuser.com"})
print("accessed_user",get_user_by_id(2))
update_user(1, {"email": "alice_new@example.com"})
delete_user(2)
print(users)
