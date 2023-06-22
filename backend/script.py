import random
import string

from enum import Enum
from utils import get_words

ALPHABET = string.ascii_lowercase
ALL_WORDS = get_words()
MAX_GUESSES = 10


class Game:
    def __init__(self) -> None:
        self._letter = self._pick_letter()  # which letter to exclude for this run
        self._words_to_show = []  # which words to pick from
        self._shown_words = []
        self._won = False  # has the user guessed the word correctly?
        self._guesses = []  # letters that the user has guessed

    def run(self):
        # set initial words to draw from
        self._words_to_show = self._select_words()
        print("Which letter is not used in these words?")

        while not self._won and len(self._guesses) < MAX_GUESSES:
            # pick a word for the user to base guess on and remove from list
            this_word = random.choice(self._words_to_show)
            self._shown_words.append(this_word)
            self._words_to_show = [w for w in self._words_to_show if w != this_word]

            # show word to the user
            print(this_word.upper())

            # get user input and evaluate
            this_guess = input("Which letter was removed from the alphabet?")

            if this_guess.lower() not in ALPHABET:
                print("Limit guesses to single ASCII letters! Try again.")
                continue

            if any([this_guess.lower() in w for w in self._shown_words]):
                print("That letter was used in one of the shown words! Try again.")
                continue
            if this_guess in self._guesses:
                print(f"You have guessed {this_guess} before! Try again.")
                continue

            self._guesses.append(this_guess)
            if this_guess.upper() == self._letter.upper():
                self._end_game("won")
            else:
                print(f"{len(self._guesses)}/{MAX_GUESSES} tries used")

        # after ten tries
        if len(self._guesses) >= MAX_GUESSES:
            self._end_game("lost")

    def _end_game(self, result: str) -> None:
        if result == "won":
            self._won = True
            print(
                f"Congratulations, you won the game after {len(self._guesses)} tries!"
            )
        else:
            print(
                f"You didn't manage to guess the letter after {len(self._guesses)} tries."
            )

        print(f"The missing letter was {self._letter.upper()}.")

    def _pick_letter(self) -> str:
        """Which letter to exclude from the alphabet for a specific run.

        Returns:
            str: excluded letter
        """
        return random.choice(ALPHABET)

    def _select_words(self) -> list[str]:
        """Select words that can be shown for a specific round.

        Returns:
            list[str]: list of possible words
        """
        return [w for w in ALL_WORDS if self._letter not in w]


if __name__ == "__main__":
    game = Game()
    game.run()
