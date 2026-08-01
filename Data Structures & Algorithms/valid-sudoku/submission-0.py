class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        myset = set()        
        sets = defaultdict(set)
        squares = defaultdict(set)

        for i,row in enumerate(board):
            myset.clear()

            for j,cell in enumerate(row):
                if cell != "." :
                    if cell in myset:
                        return False
                    myset.add(cell)

                    if cell in sets[j]:
                        return False
                    sets[j].add(cell)

                    if cell in squares[(i//3,j//3)]:
                        return False
                    squares[(i//3,j//3)].add(cell)

        return True
                