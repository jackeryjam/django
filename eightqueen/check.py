from django.http import JsonResponse
import json

# 由于客户端传来的棋盘上面皇后数量没有限制，必须在普通位运算的基础上加个row进行判断
# 不像运行八皇后的时候，聪明的我们已经知道每一行顶多只能有一个皇后
def bitCalc(chessBoard):
    flag = True
    n = len(chessBoard)
    r = 0
    l = 0
    c = 0
    for i in range(len(chessBoard)):
        if flag == False:
            break
        row = 0
        for j in range(len(chessBoard[i])):
            if chessBoard[i][j] == False:
                continue
            tmp = 1 << j
            if (tmp&l) or (tmp&r) or (tmp&c) or (tmp&row):
                flag = False
                break
            else:
                l = (l|tmp)
                r = (r|tmp)
                c = (c|tmp)
                row = (1<<n) - 1
        l = l << 1
        r = r >> 1
    return flag

# 接受客户端传过来的棋盘，对棋盘继续位运算的检验
def index(request): 
    result = {
        'isLegal':False
    }
    if 'chessBoard' in request.POST:
        chessBoard = json.loads(request.POST['chessBoard'])
        result['isLegal'] = bitCalc(chessBoard)
    return JsonResponse(result)