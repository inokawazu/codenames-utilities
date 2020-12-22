class Board():
    """
    This object represents the codename board.
    """
    def __init__(self, red = 9 , blue = 8, gray = 7 , black = 1 ):
        """
        The initializer of the codename board. It constructs the word_view which 
        is visible to all players and the spymaster_view. The board is a 5 by 5 board with 25 tiles.
        """
        self.spymaster_view = []

        for _ in range(red):
            self.spymaster_view.append("red")

        for _ in range(blue):
            self.spymaster_view.append("blue")

        for _ in range(gray):
            self.spymaster_view.append("gray")

        for _ in range(black):
            self.spymaster_view.append("black")