from random import shuffle

class SpymasterBoard():
    """
    This object represents the codename board.
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

        return print_string


class WordBoard():
    """
    This object represents the codename's word board.
    """
    def __init__(self):
        """
        The initializer of the codename word board which is the word tiles visable to everyone. 
        The board is a 5 by 5 board with 25 tiles.
        """
        self.tiles = []

        for _ in range(25):
            self.tiles.append("word")

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

        return print_string

test = SpymasterBoard()

print(test)

test = WordBoard()

print(test)