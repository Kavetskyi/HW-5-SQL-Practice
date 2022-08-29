class UserDB:
    users = [
        {"name": "test1", "email": "test1@test.com", "password": "password1"},
        {"name": "test2", "email": "test2@test.com", "password": "password2"}
    ]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user['email'] == email:
                return user
        return None

    def add(self, name, email, password_hash):
        # add check if user already exist
        for user in self.users:
            if user['email'] == email:
                return None
        user = {
            "name": name,
            "email": email,
            "password": password_hash
        }
        self.users.append(user)
        return user

    def update_by_email(self, name, email, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
        return None

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]
