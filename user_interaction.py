# INVALID_INPUT_MESSAGE = 'Invalid input. Please enter a number.'
# MAX_INPUT_ATTEMPTS = 3
#
# def get_int_input(prompt):
#     while True:
#         user_input = input(prompt)
#         try:
#             return int(user_input)
#         except ValueError:
#             print(INVALID_INPUT_MESSAGE)
#
# def prompt_user_for_role(roles):
#     for attempt in range(MAX_INPUT_ATTEMPTS):
#         for index, role in enumerate(roles, start=1):
#             print(f'{index}. {role}')
#         choice = input('Select a role by entering the number: ')
#         try:
#             choice = int(choice)
#             if 1 <= choice <= len(roles):
#                 return list(roles.keys())[choice - 1]
#             print('Invalid selection. Please choose a valid role number.')
#         except ValueError:
#             print(INVALID_INPUT_MESSAGE)
#         if attempt == MAX_INPUT_ATTEMPTS - 1:
#             print('Maximum number of attempts reached. Exiting program.')
#             exit(1)
#
# def prompt_user_for_input(prompt, input_type=str):
#     while True:
#         user_input = input(prompt)
#         if user_input:  # Guard clause for non-empty input
#             try:
#                 return input_type(user_input)
#             except ValueError:
#                 print(f'Invalid input type. Expected {input_type.__name__}.')
#         print('Input cannot be empty. Please try again.')
