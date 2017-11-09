from django.http import JsonResponse

def dfs(l, r, c, index, n, board, res):
    # 判断如果下标已经到了n，即已经摆够n颗皇后了
    if (index == n):
        res.append(board)
        return 1
    # 初始化ans为0
    ans = 0
    for i in range(n):
        # 从0到n-1试摆，如果在与斜左边冲突，斜右边，或者竖直方向冲突（冲突是指被其他皇后吃到）
        tmp = 1 << i
        if (tmp&l) or (tmp&r) or (tmp&c):
            # 则跳过
            continue
        # 不冲突就继续向下一行摆放
        board[index][i] = True
        ans += dfs((tmp | l) << 1, (tmp | r) >> 1, tmp | c, index + 1, n, board, res)
        # 回溯，把棋盘还原
        board[index][i] = False
    return ans

# 求总皇后的个数，对第一行进行特殊处理，只需要摆置棋子在左半部分即可
def totalNQueens(n, board, res, middle):
    sum = 0
    for i in range(int(n/2)):
        tmp = 1 << i
        sum += dfs(tmp << 1, tmp >> 1, tmp, 1, n, board, res)
    # 数量翻倍，由于对称的关系
    sum = 2*sum
    # 如果传进来的size是奇数，则需要额外把第一行中间摆上棋子进行dfs继续求解
    if n%2 != 0:
        tmp = 1 << int(n/2 + 1)
        sum += dfs(tmp << 1, tmp >> 1, tmp, 1, n, board, middle)
    return sum

# 接受http的get请求，得到请求的规模，设置规模，利用dfs就行求解
def index(request): 
    # 设置left数组用来保存左半边求得的结果，middle是第一行棋子置于最中间的结果
    left = []
    middle = []
    if 'size' in request.GET:
        size = int(request.GET['size'])
        # 初始化棋盘，全设置为false
        board = [[False for j in range(size)] for i in range(size)]
        num = totalNQueens(size, board, left, middle)
        # 将结果以json的形式放回客户端，将求得的结果直接传给客户端，客户端自己进行对称修复
        # 可以减少传输的流量，加快传输的速度
        result = {
            'size': size,
            'solutionNum': num,
            'type': 'halfResult',
            'solutions': {
                'left': left,
                'middle': middle
            }
        }
    return JsonResponse(result)