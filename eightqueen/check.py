from django.http import HttpResponse
import json

def index(request): 
    res = {"code":1,"msg":"","data":{"c_cnt":29,"o_cnt":0,"p_cnt":6,"pri_cnt":0}}
    if 'chessboard' in request.POST:
        print(request.POST['chessboard'])
    return HttpResponse(json.dumps(res))