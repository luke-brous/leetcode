class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # ------------------------------------------------------------
        # Approach:
        # We use 27 hash sets total (9 for rows, 9 for columns, 9 for 3x3 boxes).
        # As we iterate over each cell, we check whether the current value
        # has already been seen in its row, column, or box.
        # If it has, the Sudoku board is invalid.
        # If not, we record it in the corresponding sets.
        #
        # This ensures every number appears only once per row, column, and box.
        #
        # Time Complexity: O(81) → O(1) since the board size is fixed at 9x9.
        # Space Complexity: O(27 * 9) → O(1) for the sets (constant size).
        # ------------------------------------------------------------

        # Create 9 sets for rows, columns, and 3x3 boxes respectively.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate through all 81 cells in the board (flattened 9x9 grid).
        for i in range(81):
            col = i % 9         # column index (0–8)
            row = i // 9        # row index (0–8)

            # Determine which 3x3 box the cell belongs to.
            # Boxes are indexed from 0 to 8 (left-to-right, top-to-bottom).
            box_index = (row // 3) * 3 + (col // 3)

            # Skip empty cells (represented by ".")
            if board[row][col] == ".":
                continue

            val = board[row][col]  # The current number in the cell

            # If the number already exists in its row, column, or box,
            # then the board is invalid.
            if val in rows[row] or val in cols[col] or val in boxes[box_index]:
                return False

            # Otherwise, record the number in each corresponding set.
            rows[row].add(val)
            cols[col].add(val)
            boxes[box_index].add(val)

        # If no conflicts are found, the board is valid.
        return True
