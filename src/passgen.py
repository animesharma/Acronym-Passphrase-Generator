import sys
import pickle
import secrets
import argparse

class AcronymPassphraseGenerator:
    """
    A class to generate a passphrase based on an acronym.
    """
    def __init__(self, acronym: str, min_word_len: int, separators: list, case: int, num_passphrases: int, word_dict: dict) -> None:
        """
        Initializes the AcronymPassphraseGenerator with the given acronym, minimum word length, separators, and word dictionary.

        Input parameters:
        - acronym: The acronym to use for generating the passphrase.
        - min_word_len: The minimum length of words to use in the passphrase.
        - separators: A list of separator characters to use between words in the passphrase.
        - case: The integer ID of the case to use for generating the passphrase. Use --help for more details
        - num_passphrases: The number of passphrases to generate from the given acronym.
        - word_dict: A dictionary of words to use for generating the passphrase, where the keys are the first letters of the words and the values are lists of words starting with that letter.
        """
        self.__acronym = acronym
        self.__min_word_len = min_word_len
        self.__separators = separators
        self.__case = case
        self.__num_passphrases = num_passphrases
        self.__word_dict = word_dict

    def __filter_short_words(self, word_list) -> list:
        """
        Filters a list of words by removing words with length less than the specified minimum word length.

        Input Paramters
        - word_list: A list of words to be filtered.

        Returns: A list containing only the words with length greater than or equal to the specified minimum word length.
        """
        return [word for word in word_list if len(word) >= self.__min_word_len]
    
    def __modify_case(self, word: str) -> str:
        """
        This method takes a word as input and modifies its case based on the value of self.__case

        Input paramters:
        - word: The input word to be modified.

        Returns: The input word with modified case.
        """
        if self.__case == 0:
            return word
        elif self.__case == 1:
            return word.capitalize()
        elif self.__case == 2:
            return "".join(char.upper() if secrets.choice([True, False]) else char.lower() for char in word)
        elif self.__case == 3:
            return "".join(char.upper() if index % 2 != 0 else char.lower() for index, char in enumerate(word))
            
    def generate_passphrase(self) -> list:
        """
        Generates passphrase(s) based on the given acronym, minimum word length, separators, and word dictionary.

        Returns: A list of generated passphrase(s).
        """
        for letter in set(self.__acronym):
            self.__word_dict[letter] = self.__filter_short_words(self.__word_dict[letter])
        
        passphrases = []
        for _ in range(self.__num_passphrases):
            passphrase = []
            for index, letter in enumerate(self.__acronym):
                word = secrets.choice(self.__word_dict[letter])
                word = self.__modify_case(word)
                passphrase.append(word)
                if index < len(self.__acronym) - 1:
                    passphrase.append(secrets.choice(self.__separators))
            passphrases.append("".join(passphrase))
 
        return passphrases
    
################################################################################

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
            help=f"Acronym from which passphrase is generated. \
                    Must be between 1 and 10 characters long."
        )
        self.__parser.add_argument(
            "--min_word_len",
            "-m",
            dest="min_word_len",
            type=int,
            default=1,
            help=f"Minimum length of words used in the passphrase. \
                    Must be an integer value between 1 and 8. \
                    Defaults to 1"
        )
        self.__parser.add_argument(
            "--separators",
            "-s",
            dest="separators",
            type=str,
            nargs="*",
            default=["-"],
            help=f"List of separators to separate words in the passphrase. \
                    Can specify one or more values. \
                    Each value can have one or multiple characters. \
                    Defaults to hyphen (-)"
        )
        self.__parser.add_argument(
            "--case",
            "-c",
            dest="case",
            default=0,
            type=int,
            help=f"Specifies the case style to use for the generated passphrase. \
                    Must be an integer value between 0 and 3. \
                    Supported options include: \
                    0 -> kebab-case (default), \
                    1 -> PascalCase, \
                    2 -> InTermitteNt CapItalIzaTIon, \
                    3 -> StIcKy CaPs"
        ) 
        self.__parser.add_argument(
            "--num_passphrases",
            "-n",
            dest="num_passphrases",
            type=int,
            default=1,
            help=f"The number of passphrases to be generated from the acronym. \
                    Must be an integer value between 1 and 20. \
                    Defaults to 1"
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
        if args.min_word_len and not (1 <= args.min_word_len <= 8):
            self.__error_handler(error_msg="Minimum word length must be between 1 and 8")
        if args.case and not (0 <= args.case <= 3):
            self.__error_handler(error_msg="Case Style must be between 0 and 3")
        if args.num_passphrases and not (1 <= args.num_passphrases <= 20):
            self.__error_handler("Number of passphrases must be an integer between 1 and 20")
        
    def get_args(self) -> argparse.Namespace:
        """
        Parses and validates the command line arguments and returns them as a Namespace object.

        Returns: The parsed and validated command line arguments.
        """
        args = self.__parser.parse_args()
        self.__validate_args(args)
        return args

################################################################################

def main() -> None:
    input_args = ParseArguments().get_args()

    with open("./data/word_dict.pkl", "rb") as f:
        word_dict = pickle.load(f)

    passgen = AcronymPassphraseGenerator(
        acronym = input_args.acronym.lower(),
        min_word_len = input_args.min_word_len,
        separators = input_args.separators,
        case = input_args.case,
        num_passphrases = input_args.num_passphrases,
        word_dict = word_dict
    )
    passphrases = passgen.generate_passphrase()
    for passphrase in passphrases:
        print(passphrase)

################################################################################

if __name__ == "__main__":
    main()
