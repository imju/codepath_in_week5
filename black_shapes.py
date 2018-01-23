class Solution:
    # @param A : list of strings
    # @return an integer

    def black(self, A):


        visited = [ [0 for x in range(len(A[0]))] for y in range(len(A))]

        width = len(A[0])
        height = len(A)
        x_list = []
        t_count = 0
        for i in range(len(A)): #by row
            for j in range(len(A[i])): #by col and cell
                '''
                if i > 1 :
                    print 'i:j-'+str(i)+':'+str(j)
                    print 'visited:'+str(visited)
                '''
                if visited[i][j]:
                    continue
                visited[i][j] = 1
                if A[i][j]== 'X' :
                    #print 'i:j-'+str(i)+':'+str(j)
                    x_list.append((i,j))
                else:
                    continue
                if len(x_list)>0:
                    t_count += 1
                while len(x_list)>0:
                    #print 'x_list:'+str(x_list)
                    (a,b)=x_list.pop()
                    #check up, left, right, down
                    #up
                    if a - 1 >= 0:
                        if visited[a-1][b] == 0:
                            visited[a-1][b] = 1
                            if A[a-1][b]=='X':
                                x_list.append((a-1,b))
                    #down
                    if a + 1 < height:
                        if visited[a+1][b] == 0:
                            visited[a+1][b] = 1
                            if A[a+1][b]=='X':
                                x_list.append((a+1,b))
                    #left
                    if b - 1 >= 0:
                        if visited[a][b-1] == 0:
                            visited[a][b-1]=1
                            if A[a][b-1]=='X':
                                x_list.append((a,b-1))

                    #right
                    if b + 1 < width:
                        if visited[a][b+1] == 0:
                            visited[a][b+1]=1
                            if A[a][b+1]=='X':
                                x_list.append((a,b+1))

        return t_count
