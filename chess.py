from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy pěšáka. Zohledňuje jeho barvu.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        if self.color == 'white':
            forward = (row + 1, col)
        else:  # color == 'black'
            forward = (row - 1, col)
        
        # Přidá tah pouze pokud je na šachovnici
        if self.is_position_on_board(forward):
            moves.append(forward)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        Střelec se pohybuje diagonálně libovolný počet polí.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Všechny čtyři diagonální směry
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for d_row, d_col in directions:
            for step in range(1, 8):  # Střelec může jít maximálně 7 polí
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break  # Pokud se dostane mimo šachovnici, zastavíme tento směr

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        Věž se pohybuje horizontálně nebo vertikálně libovolný počet polí.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Všechny čtyři směry: horizontální a vertikální
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for d_row, d_col in directions:
            for step in range(1, 8):  # Věž může jít maximálně 7 polí
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break  # Pokud se dostane mimo šachovnici, zastavíme tento směr

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.
        Dáma kombinuje pohyby střelce a věže.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Kombinace všech směru věže a střelce
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Věž - horizontální a vertikální směry
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Střelec - diagonální směry
        ]

        for d_row, d_col in directions:
            for step in range(1, 8):  # Dáma může jít maximálně 7 polí v každém směru
                new_position = (row + step * d_row, col + step * d_col)
                if self.is_position_on_board(new_position):
                    moves.append(new_position)
                else:
                    break  # Pokud se dostane mimo šachovnici, zastavíme tento směr

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        Král se pohybuje o jedno pole v libovolném směru.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Všechny směry krále (kombinace střelce a věže, ale pouze jedno pole)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Vertikální a horizontální
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Diagonální
        ]

        for d_row, d_col in directions:
            new_position = (row + d_row, col + d_col)
            if self.is_position_on_board(new_position):
                moves.append(new_position)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Test Knight
    knight = Knight("black", (1, 2))
    print(knight)
    print("Possible moves:", knight.possible_moves())

    # Test Pawn
    pawn = Pawn("white", (2, 2))
    print(pawn)
    print("Possible moves:", pawn.possible_moves())

    # Test Bishop
    bishop = Bishop("white", (4, 4))
    print(bishop)
    print("Possible moves:", bishop.possible_moves())

    # Test Rook
    rook = Rook("black", (1, 1))
    print(rook)
    print("Possible moves:", rook.possible_moves())

    # Test Queen
    queen = Queen("white", (4, 4))
    print(queen)
    print("Possible moves:", queen.possible_moves())

    # Test King
    king = King("black", (4, 4))
    print(king)
    print("Possible moves:", king.possible_moves())
