import json

from django.http import HttpResponse
from django.shortcuts import render

from FirstApp.tool import utils


def index(request):
    return render(request, 'index.html')

# 扫描
def scan(request):
    return render(request, 'scan.html')

def scanList(request):
    data = request.POST.get('result', None)
    print(data)
    return render(request, 'scanList.html')

# 扫描列表
def scanCommit(request):
    print('收到资料:')
    print(request.method)
    if (request.method == 'POST'):
        name = request.POST.get('name', None)
        arr = utils.fileListFunc(name)
        result = json.dumps(arr,ensure_ascii=False)
    return HttpResponse(result)
    # return render(request, 'scanList.html')

if __name__ == '__main__':
    s = ['asdf',123,'aaa','bbb','我是中国人']
    # ["asdf", 123, "aaa", "bbb", "\u6211\u662f\u4e2d\u56fd\u4eba"]
    p = json.dumps(s)
    # ["asdf", 123, "aaa", "bbb", "我是中国人"]
    p = json.dumps(s, ensure_ascii= False) #ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了
    print(p)