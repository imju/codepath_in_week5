class Solution:

    def capture(self, board, i, j, visited):
        width = len(board[0])
        height = len(board)
        if i<0 or j<0 or i>=height or j>=width:
            return False

        #print 'board:'+str(board[i][j])+' for i:'+str(i)+' j:'+str(j)

        if visited[i][j]:
            if board[i][j] == 'X':
                print 'board:'+str(board[i][j])+' for i:'+str(i)+' j:'+str(j)+'visited: return True'
                return True
            elif board[i][j] == 'O':
                print 'board:'+str(board[i][j])+' for i:'+str(i)+' j:'+str(j)+'visited: return False'
                return False



        visited[i][j]=1
        if board[i][j] == 'O' or board[i][j]=='#':
            print 'board:'+str(board[i][j])+'Recursive:'+':i:'+str(i)+':j:'+str(j)
            board[i][j]='#'

            if self.capture(board, i+1, j, visited) and \
               self.capture(board, i, j+1, visited) and \
               self.capture(board, i-1, j, visited) and \
               self.capture(board, i, j-1, visited) :
                   print ' O to X>>'+'board:'+str(board[i][j])+' for i:'+str(i)+' j:'+str(j)
                   board[i][j]='X'
                   return True
            else:
                board[i][j]='O'
        #print 'Return True'
        return True

    def flood_fill(self, board, i, j, prev, new):
        height = len(board)
        width = len(board[0])
        if i<0 or j<0 or i >= height or j >= width:
            return
        if board[i][j] != prev:
            return
        board[i][j] = new

        self.flood_fill(board, i+1, j, prev, new)
        self.flood_fill(board, i, j+1, prev, new)
        self.flood_fill(board, i-1, j, prev, new)
        self.flood_fill(board, i, j-1, prev, new)


    # @param A : list of list of chars
    def solve(self, A):

        if len(A) == 0 :
            return A
        if len(A[0]) == 0:
            return A

        if len(A[0]) == 1:
            return A

        import collections
        if not isinstance(A[0], collections.Sequence):
            return A
        height = len(A)
        width = len(A[0])

        for i in range(height):
            if A[i][0]=='O':
                self.flood_fill(A, i,0, 'O', '#')

        for i in range(height):
            if A[i][width-1]=='O':
                self.flood_fill(A, i, width-1, 'O', '#')

        for i in range(width):
            if A[0][i]=='O':
                self.flood_fill(A, 0, i, 'O', '#')

        for i in range(width):
            if A[height-1][i]=='O':
                self.flood_fill(A, height-1, i, 'O', '#')
        for i in range(height):
            for j in range(width):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == '#':
                    A[i][j] = 'O'

        return A

            
