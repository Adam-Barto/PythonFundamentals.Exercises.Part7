from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeterv2


class MultilingualGreeterV2Test(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_language_options(self, stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        expected = "Please choose a language: \n" \
                   "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n"

        multilingual_greeterv2.print_language_options(languages)
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('builtins.input', return_value="1")
    def test_language_input(self, user_input):
        actual = multilingual_greeterv2.language_input()
        self.assertEqual(1, actual)

    def test_language_choice_is_valid(self):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        test_cases = [
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (10, False),
            ('PIG LATIN', False)
        ]

        for key, expected in test_cases:
            with self.subTest(f"{key}, {expected}"):
                self.assertEqual(expected, multilingual_greeterv2.language_choice_is_valid(languages, key))

    def test_get_name_input(self):
        name_prompt_dict = {
            1: 'What is your name?',
            2: '¿Cómo te llamas?',
            3: 'Qual é o seu nome?'
        }

        for key, expected in name_prompt_dict.items():
            with self.subTest(f"{key} -> {expected}"):
                self.assertEqual(expected, multilingual_greeterv2.get_name_input(name_prompt_dict, key))

    @patch('builtins.input', return_value="Harry Potter")
    def test_name_input(self, user_input):
        self.assertEqual("Harry Potter", multilingual_greeterv2.name_input("What is your name?"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }

        multilingual_greeterv2.greet("Winston Wolfe", greetings_dict, 1)
        self.assertEqual("Hello Winston Wolfe\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test2_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        multilingual_greeterv2.greet("Vincent Vega", greetings_dict, 2)
        self.assertEqual("Hola Vincent Vega\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test3_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        multilingual_greeterv2.greet("Jules Winnfield", greetings_dict, 3)
        self.assertEqual("Olá Jules Winnfield\n", stdout_mock.getvalue())

    def test_admin_choice(self):
        self.fail()

    def test_is_admin_True(self):
        expected = True
        actual = multilingual_greeterv2.is_admin('1')
        self.assertEqual(expected, actual)

    def test_is_admin_False(self):
        expected = False
        actual = multilingual_greeterv2.is_admin(0)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_dict(self, stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }
        expected = "Please choose a language: \n" \
                   "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n" \
                   "4: French\n"

        multilingual_greeterv2.update_dict(languages, 4, 'French')
        multilingual_greeterv2.print_language_options(languages)
        self.assertEqual(expected, stdout_mock.getvalue())



    def test_update_greetings(self):
        self.fail()
