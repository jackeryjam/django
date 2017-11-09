from django.http import JsonResponse
import json

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

def index(request): 
    result = {
        'isLegal':False
    }
    if 'chessBoard' in request.POST:
        chessBoard = json.loads(request.POST['chessBoard'])
        result['isLegal'] = bitCalc(chessBoard)
    return JsonResponse(result)