from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Users,Clients
import json
import random
import string
from pathlib import Path
@csrf_exempt
def login(request):
    if request.session.get('user_fio'):
        return HttpResponseRedirect('/board')
    else:
        return render(request, 'app/login.html')

def logout(request):
    if request.session['user_fio']:
        del request.session['user_fio']
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(PurePath())

def token(request):
    data = {}
    if request.method == 'POST':

        try:
            post_ = json.loads(request.body.decode('utf8'))
            log = Users.objects.filter(login=post_['login'], password=post_['password'])
            if log:
                if dict(log.values()[0])['token']:
                    data['id'] = dict(log.values()[0])['id']
                    data['token'] = dict(log.values()[0])['token']
                    request.session['user_fio'] = dict(log.values()[0])['FIO']
                else:
                    token_ = ''.join(random.choices(string.ascii_letters + string.digits, k=60))
                    Users.objects.filter(login=post_['login']).update(token=token_)
                    log = Users.objects.filter(login=post_['login'])
                    data['id'] = dict(log.values()[0])['id']
                    data['token'] = dict(log.values()[0])['token']
                    request.session['user_fio'] = dict(log.values()[0])['FIO']
            else:
                return HttpResponse(False)

        except Exception as e:
            return HttpResponse(e)

    return HttpResponse(json.dumps(data))


def board(request):
    data={}
    if request.method == 'GET' and request.session.get('user_fio'):
        data = Clients.objects.filter(FIO_representative=request.session['user_fio']).values()
#       test = {}
        data = list(data)
        compare = {'account_number':'Номер счета','familiya':'Фамилия','imya':'Имя','otchestvo':'Отчество','birthday':'Дата рождения','INN':'ИНН','FIO_representative':'Отвественный','status':'Статус'}
        for k,v in compare.items():
           for i,d in enumerate(data):
               data[i][v] = data[i][k]
               del data[i][k]

    if request.method == 'POST' and request.session.get('user_fio'):
        if request.body:
            try:
                post = dict(json.loads(request.body.decode('utf8')))
                Clients.objects.filter(id=post['id']).update(status=post['status'])
                return HttpResponse({'res':'status changed'})
            except Exception as e:
                return HttpResponse("Возникла непредвиденная ошибка "  + str(e) + " \nОбратитесь к администратору")

    if not request.session.get('user_fio'):
        return HttpResponseRedirect('/')

    return render(request, 'app/board.html',{"data":data})