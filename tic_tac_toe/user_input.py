class UserInput:
    def input_validator(self):
        while True:
            user_entry = input("Please enter a number, 1-9.\n\n")
            try:
                return int(user_entry) - 1
            except ValueError:
                print("\nI'm sorry, I don't understand that.")
