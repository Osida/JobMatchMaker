# Manages user interactions and role selection

def get_user_role_choice(roles):
    # Existing function to get user role choice
    ...


def get_user_input(prompt, input_type=str):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        try:
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input type. Expected {input_type.__name__}.")
