from src.backend.piece import Rook, Square

moves = [
    ('White rook vertical movement',
        ['A2 A4','A7 A5','A1 A3'],
        [Rook(is_white=True, location=(0,2))]),
    ('Black rook vertical movement',
        ['A2 A4','A7 A5','A1 A3', 'H7 H5', 'C2 C3', 'H8 H6'],
        [Rook(is_white=True, location=(0,2)),
        Rook(is_white=False, location=(7,5))]),
    ('White rook horizontal movement',
        ['A2 A4','A7 A5','A1 A3', 'H7 H5', 'A3 G3', 'H8 H6', 'C2 C3','H6 F6'],
        [Rook(is_white=True, location=(6,2)]),
    ('Black rook horizontal movement',
        ['A2 A4','A7 A5','A1 A3', 'H7 H5', 'A3 G3', 'H8 H6', 'C2 C3','H6 F6'],
        [Rook(is_white=True, location=(6,2),
        Rook(is_white=False, location=(5, 5))]),
    ('White rook Captures Pawn',
        ['A2 A4','B7 B5','A1 A3', 'H7 H5', 'A3 B3', 'H8 H6', 'B3 B5'],
        [Rook(is_white=True, location=(6,2))]),
    ('Black rook Captures Pawn',
        ['A2 A4','A7 A5','A1 A3', 'A8 A6', 'A3 G3', 'A6 B6', 'C2 C3','B6 B2'],
        [Rook(is_white=True, location=(6,2)),
        Rook(is_white=False, location=(1,1))]),
    ('White rook moving over white pawn (invalid Move)',
        ['A1 A4'],
        [Rook(is_white=True, location=(0,0))]),
    ('Black rook moving over black pawn (invalid move)',
        ['A2 A4', 'A8 A5'],
        [Rook(is_white=False, location=(0,7))]),
    ('Diagonal white rook move (invalid move)',
        ['A2 A4','A7 A5','A1 A3', 'A8 A6', 'A3 D6'],
        [Rook(is_white=True, location=(6,2)),
        Rook(is_white=False, location=(1,1))]),
     
]