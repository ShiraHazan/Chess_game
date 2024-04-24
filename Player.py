class Player:
    def __init__(self, name, color):
        self.name = name  # player's name
        self.color = color  # The color of the player's playing pieces
        self.pieces = []  # List to store player's pieces
    
    def add_piece(self, piece):
        """Add a piece to the player's collection"""
        self.pieces.append(piece)

    def remove_piece(self, piece):
        """Remove a captured piece from the player's collection"""
        if piece in self.pieces:
            self.pieces.remove(piece)
    
    def get_piece_by_type(self, piece_type):
        """Get a specific type of piece from the player's collection"""
        return [piece for piece in self.pieces if piece.type == piece_type]
    
    def get_piece_by_position(self, position):
        """Get a piece at a specific position"""
        return [piece for piece in self.pieces if piece.position == position]
    