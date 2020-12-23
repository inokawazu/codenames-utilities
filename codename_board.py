from random import shuffle, sample
import csv

WORDS = []

WORD_FILE_NAME = "most-common-nouns-english.csv"


with open(WORD_FILE_NAME, 'r') as word_file:
    word_file_reader = csv.reader(word_file)
    for line in word_file_reader:
        WORDS.append(line[0])


MAX_WORD_LENGTH = max(list(map(len, WORDS)))

class SpymasterBoard():
    """
    This object represents the codename spymasters' board.
    """
    def __init__(self, red = 9 , blue = 8, gray = 7 , black = 1 ):
        """
        The initializer of the codename spymaster board. The board is a 5 by 5 board with 25 tiles.
        """
        self.tiles = []

        for _ in range(red):
            self.tiles.append("red")

        for _ in range(blue):
            self.tiles.append("blue")

        for _ in range(gray):
            self.tiles.append("gray")

        for _ in range(black):
            self.tiles.append("black")

        shuffle(self.tiles)

    def __str__(self):
        """
        Returns the string form of the spymaster board.
        """
        print_string = ""

        for index, tile in enumerate(self.tiles):
            print_string += tile

            if (index + 1) % 5 == 0 and index > 0:
                print_string += "\n"
            elif index < 25 - 1:
                print_string += "\t"

        return print_string.expandtabs(MAX_WORD_LENGTH+3)


class WordBoard():
    """
    This object represents the codename's word board.
    """
    def __init__(self):
        """
        The initializer of the codename word board which is the word tiles visable to everyone. 
        The board is a 5 by 5 board with 25 tiles.
        """

        self.tiles = sample(WORDS, 25)

        shuffle(self.tiles)

    def __str__(self):
        """
        Returns the string form of the word board.
        """
        print_string = ""

        for index, tile in enumerate(self.tiles):
            print_string += tile

            if (index + 1) % 5 == 0 and index > 0:
                print_string += "\n"
            elif index < 25 - 1:
                print_string += "\t"

        return print_string.expandtabs(MAX_WORD_LENGTH+3)