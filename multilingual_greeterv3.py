from typing import Dict

from random import randint

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: 'English',
    2: 'Spanish',
    3: 'Portuguese'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?',
    2: '¿Cómo te llamas?',
    3: 'Qual o seu nome?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: ['Hello', 'Yo', 'Howdy'],
    2: ['Hola', 'Sí', '¡Oye!'],
    3: ['Olá', 'Oi', 'Prazer']
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for (k, v) in lang_options.items():
        print(str(k) + ': ' + str(v))


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    return int(input())


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options.get(lang_choice)


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    return str(input(name_prompt))


def greet(name: str, greetings_options: Dict[int, list], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(rand_greeting(greetings_options, lang_choice) + ' ' + name)


def admin_choice():
    user_input = input('Press 1 to add a language \nPress 2 to update Greetings.')
    if user_input == '1':
        add_support()
    elif user_input == '2':
        update_greetings()
    else:
        print('Not a valid Choice.')


def is_admin(user_input='0'):
    # user_input = input('Press 1 for Admin Mode \nPress anything else for normal mode.')
    if user_input == '1':
        return True
    else:
        return False


def add_support():
    update_dict(lang_dict, len(lang_dict) + 1, input('Enter new Langauge: '))
    update_dict(name_prompt_dict, len(name_prompt_dict) + 1, input('Enter the name ask: '))
    update_dict(greetings_dict, len(greetings_dict) + 1, input('Enter the greeting: '))


def update_greetings(chosen_dict, lang_choice: int, new_value: str):
    update_dict(greetings_dict, len(greetings_dict) + 1, input('Add a greeting: '))


def update_dict(chosen_dict, lang_choice: int, new_value: str):
    """
    Takes a chosen dict, a key value, and a string, and updates that dicts key value to the string
    :param chosen_dict: The Dict
    :param lang_choice: Key value
    :param new_value: The String
    :return:
    """
    dict_update = chosen_dict[lang_choice] = ''
    if type(dict_update) is not list:
        chosen_dict[lang_choice] = new_value
    else:
        dict_update.append(new_value)


def rand_greeting(chosen_dict, lang_choice):
    the_list = chosen_dict[lang_choice]
    random_value = randint(0, len(the_list) - 1)
    return chosen_dict[lang_choice][random_value]


def update_greetings():
    print_language_options(lang_dict)
    update_dict(greetings_dict, language_input(), input('Update Greeting to: '))


if __name__ == '__main__':
    if is_admin(input('Press 1 for Admin Mode \nPress anything else for user mode.')):
        admin_choice()
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)

#
# Create a program called *multilingual_greeter_v3.py*
#
# Extend the functionality from exercise 2 to meet the following requirements:
# * Each key in the greetings dictionary is associated with a list rather than a string.
# * Each list should contain at least 3 greetings per language.
# * The greet function will select a random item from the list when invoked.
# * Ensure appropriate support for these new features while in admin mode.
# * As always, be sure to include appropriate test coverage.
