import database


def main():
    db = database.Database()
    print(f"Loaded {len(db.data['users'])} users")

    username = input("Username: ")
    user = db.get_user(username)
    if user is None:
        print("User not found")
        return

    password = input("Password: ")
    if not db.login(username, password):
        print("Incorrect password")
        return

    print("Logged in successfully")
    print(f"Balance: {user['balance']}")
    print()

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("> ")

        if choice == "1":
            amount = int(input("Amount: "))
            user["balance"] += amount
        elif choice == "2":
            amount = int(input("Amount: "))
            if amount > user["balance"]:
                print("Insufficient balance")
                continue
            user["balance"] -= amount
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
