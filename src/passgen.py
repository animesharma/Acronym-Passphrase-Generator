import sys
import json
import secrets
from argparse import ArgumentParser, Namespace

class AcronymPassphraseGenerator:
    """
    
    """
    def __init__(self, acronym: str, min_word_len: int, separators: list, word_list: list) -> None:
        """
        
        """
        self.__acronym = acronym
        self.__min_word_len = min_word_len
        self.__separators = separators
        self.__word_list = word_list

    def __filter_short_words(self) -> list:
        """
        Filters a list of words by removing words with length less than the specified minimum word length.

        Returns: A new list containing only the words with length greater than or equal to the specified minimum word length.
        """
        return [word for word in self.__word_list if len(word) >= self.__min_word_len]
    
    def __generate_alphabetical_dict(self) -> dict:
        """
        Generates a dictionary where the keys are the first letters of the words in the input list and the values are lists of words starting with that letter.

        Returns: A dictionary where the keys are the first letters of the words in the input list and the values are lists of words starting with that letter.
        """
        alphabetical_dict = {}
        for word in self.__word_list:
            initial = word[0]
            alphabetical_dict[initial] = alphabetical_dict.get(initial, []) + [word]
        return alphabetical_dict

    def __get_inital_word_map(self) -> dict:
        """
        
        """
        if self.__min_word_len:
            self.__word_list = self.__filter_short_words()
        word_dict = self.__generate_alphabetical_dict()
        return word_dict

    def generate_passphrase(self) -> str:
        """
        
        """
        passphrase = ""
        initial_word_map = self.__get_inital_word_map()
        for index, letter in enumerate(self.__acronym):
            passphrase += secrets.choice(initial_word_map[letter])
            if index < len(self.__acronym) - 1:
                passphrase += secrets.choice(self.__separators)
        return passphrase

class ParseArguments:
    """
    
    """
    def __init__(self) -> None:
        """
        
        """
        self.__parser = ArgumentParser(
            prog="Acronym Passphrase Generator",
            description="Python program to generate a secure passphrase from a user desired acronym.",
        )

    def __define_args(self) -> None:
        """
        
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
        
        """
        print(f"Error: {error_msg}. Use --help for more information")
        sys.exit(1)

    def __validate_args(self, args) -> None:
        """
        
        """
        if not 1 < len(args.acronym) <= 10:
            self.__error_handler(error_msg="Acronym must be between 1 and 10 characters long")
        if not args.acronym.isalpha():
            self.__error_handler(error_msg="Acronyms must use the English alphabet only")
        
    def get_args(self) -> Namespace:
        """
        
        """
        self.__define_args()
        args = self.__parser.parse_args()
        self.__validate_args(args)
        return args

if __name__ == "__main__":
    input_args = ParseArguments().get_args()

    with open("./data/word_list.json", "r") as f:
        word_list = json.load(f)

    passgen = AcronymPassphraseGenerator(
        acronym = input_args.acronym.lower(),
        min_word_len = input_args.min_word_len,
        separators = input_args.separators,
        word_list = word_list
    )
    passphrase = passgen.generate_passphrase()
    print(passphrase)
