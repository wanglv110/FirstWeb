from django.shortcuts import render

from FirstApp.tool import utils


def index(request):
    return render(request, 'index.html')

def scan(request):
    return render(request, 'scan.html')

def scanCommit(request):
    print('收到资料:')
    print(request.method)
    if (request.method == 'POST'):
        name = request.POST.get('name', None)
        arr = utils.fileListFunc(name)
        print(arr)
    return scan(request)