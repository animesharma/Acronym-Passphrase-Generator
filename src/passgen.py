import sys
import pickle
import secrets

import argparse

class AcronymPassphraseGenerator:
    """
    A class to generate a passphrase based on an acronym.
    """
    def __init__(self, acronym: str, min_word_len: int, separators: list, word_dict: dict) -> None:
        """
        Initializes the AcronymPassphraseGenerator with the given acronym, minimum word length, separators, and word dictionary.

        Input parameters:
        - acronym: The acronym to use for generating the passphrase.
        - min_word_len: The minimum length of words to use in the passphrase.
        - separators: A list of separator characters to use between words in the passphrase.
        - word_dict: A dictionary of words to use for generating the passphrase, where the keys are the first letters of the words and the values are lists of words starting with that letter.
        """
        self.__acronym = acronym
        self.__min_word_len = min_word_len
        self.__separators = separators
        self.__word_dict = word_dict

    def __filter_short_words(self, word_list) -> list:
        """
        Filters a list of words by removing words with length less than the specified minimum word length.

        Input Paramters
        - word_list: A list of words to be filtered.

        Returns: A list containing only the words with length greater than or equal to the specified minimum word length.
        """
        return [word for word in word_list if len(word) >= self.__min_word_len]
    
    def generate_passphrase(self) -> str:
        """
        Generates a passphrase based on the given acronym, minimum word length, separators, and word dictionary.

        Returns: The generated passphrase.
        """
        if self.__min_word_len:
            for letter in set(self.__acronym):
                self.__word_dict[letter] = self.__filter_short_words(self.__word_dict[letter])
        
        passphrase = []
        
        for index, letter in enumerate(self.__acronym):
            passphrase.append(secrets.choice(self.__word_dict[letter]))
            if index < len(self.__acronym) - 1:
                passphrase.append(secrets.choice(self.__separators))
        
        return "".join(passphrase)

class ParseArguments:
    """
    A class to parse command line arguments for the Acronym Passphrase Generator program.
    """
    def __init__(self) -> None:
        """
        Initializes the ParseArguments object with an ArgumentParser.
        """
        self.__parser = argparse.ArgumentParser(
            prog="Acronym Passphrase Generator",
            description="Python program to generate a secure passphrase from a user desired acronym.",
        )
        self.__define_args()

    def __define_args(self) -> None:
        """
        Defines the command line arguments for the Acronym Passphrase Generator program.
        """
        self.__parser.add_argument(
            "--acronym",
            "-a",
            dest="acronym",
            type=str,
            required=True,
            help="Acronym from which passphrase is generated."
        )
        self.__parser.add_argument(
            "--min_word_len",
            "-m",
            dest="min_word_len",
            type=int,
            help="Minimum length of words used in the passphrase."
        )
        self.__parser.add_argument(
            "--separators",
            "-s",
            dest="separators",
            type=str,
            nargs="*",
            default=["-"],
            help="List of separators to separate words in the passphrase. Defaults to hyphen (-)"
        )

    def __error_handler(self, error_msg: str) -> None:
        """
        Prints an error message to the console and exits the program.
        
        Input parameters:
        - error_msg: The error message to print.
        """
        print(f"Error: {error_msg}. Use --help for more information")
        sys.exit(1)

    def __validate_args(self, args: argparse.Namespace) -> None:
        """
        Validates the command line arguments and raises an error if any argument is invalid.
        
        Input parameters:
        - args: The parsed command line arguments.
        """
        if not 1 < len(args.acronym) <= 10:
            self.__error_handler(error_msg="Acronym must be between 1 and 10 characters long")
        if not args.acronym.isalpha():
            self.__error_handler(error_msg="Acronyms must use the English alphabet only")
        
    def get_args(self) -> argparse.Namespace:
        """
        Parses and validates the command line arguments and returns them as a Namespace object.

        Returns: The parsed and validated command line arguments.
        """
        args = self.__parser.parse_args()
        self.__validate_args(args)
        return args


if __name__ == "__main__":
    input_args = ParseArguments().get_args()

    with open("./data/word_dict.pkl", "rb") as f:
        word_dict = pickle.load(f)

    passgen = AcronymPassphraseGenerator(
        acronym = input_args.acronym.lower(),
        min_word_len = input_args.min_word_len,
        separators = input_args.separators,
        word_dict = word_dict
    )
    passphrase = passgen.generate_passphrase()
    print(passphrase)
