from django.http import JsonResponse
import copy

def dfs(l, r, c, index, n, board, res):
    if (index == n):
        tmp = copy.deepcopy(board)
        res.append(tmp)
        print (tmp)
        return 1
    ans = 0
    for i in range(n):
        tmp = 1 << i
        if (tmp&l) or (tmp&r) or (tmp&c):
            continue
        board[index][i] = True
        ans += dfs((tmp | l) << 1, (tmp | r) >> 1, tmp | c, index + 1, n, board, res)
        board[index][i] = False
    return ans

def totalNQueens(n, board, res, middle):
    sum = 0
    for i in range(int(n/2)):
        tmp = 1 << i
        board[0][i] = True
        sum += dfs(tmp << 1, tmp >> 1, tmp, 1, n, board, res)
        board[0][i] = False
    sum = 2*sum
    if n%2 != 0:
        i = int(n/2 + 1)
        tmp = 1 << i
        board[0][i] = True
        sum += dfs(tmp << 1, tmp >> 1, tmp, 1, n, board, middle)
        board[0][i] = False
    print (res)
    return sum

def index(request): 
    left = []
    middle = []
    board = []
    if 'size' in request.GET:
        size = int(request.GET['size'])
        board = [[False for j in range(size)] for i in range(size)]
        num = totalNQueens(size, board, left, middle)
        result = {
            'size': size,
            'solutionNum': num,
            'solutions': {
                'left': left,
                'middle': middle
            }
        }
    return JsonResponse(result)