import string
import random

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [] # TODO
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        pass

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        pass # TODO
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
