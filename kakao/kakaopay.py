
import json
from json import JSONDecodeError
import requests
import urllib
from django.db.models import F
from django.http import (HttpResponse, JsonResponse,
                         HttpResponseBadRequest, HttpResponseRedirect)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from django.views import View
from order.models import Order, Payment
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
# from payment.models import PaymentModel
# menus={'아메리카노':'아메리카노', '2': '카페라떼','23':'초코쉐이크'}
headers = {
    'Authorization': "KakaoAK 71af8dbb8f935a60b315cede1dec6368",
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
}

pay_url = 'https://kapi.kakao.com/v1/payment/ready'
check_url = 'https://kapi.kakao.com/v1/payment/approve'

@csrf_exempt
@permission_classes([IsAuthenticated])
def Pay(request):
    try:
        user = request.GET.get('user')
        userM = User.objects.get(username=user)
        realorder = Order.objects.filter(creator=userM)
        thisorder = realorder.filter(status='a').order_by('id').last()

    except User.DoesNotExist:
        return HttpResponseRedirect('http://10.16.147.173:3000/')
    idx=[]
    idx = thisorder.order.split(",")
    total_cost = thisorder.price
    item = thisorder.order
    approval_url = 'http://10.16.147.173:8000/check?user=' + user
    cancel_url = 'http://10.16.147.173:8000/cancel?user=' + user
    fail_url = 'http://10.16.147.173:8000/fail?user=' + user

    # Body
    body = {
        'cid': 'TC0ONETIME',
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'item_name': item,
        'quantity': 1,
        'total_amount': total_cost,
        'vat_amount': total_cost// 10,
        'tax_free_amount': 0,
        'approval_url': approval_url,
        'fail_url': fail_url,
        'cancel_url': cancel_url
    }

    # Get response
    res = requests.post(url=pay_url, headers=headers, data=body)
    req_data = json.loads(res.text)
    try:
        tid = req_data['tid']
        redirection_url = req_data['next_redirect_mobile_url']
    except KeyError as err:
        return JsonResponse(req_data)

    thisorder.tid = tid
    thisorder.save(update_fields=["tid"])
    # return JsonResponse(posts_serialized, safe=False)
    return JsonResponse({'url': redirection_url})


# csrf, POST만
def Check(request):
    user = request.GET.get('user')
    userM = User.objects.get(username=user)
    realorder = Order.objects.filter(creator=userM)
    thisorder = realorder.filter(status='a').order_by('id').last()
    total_cost = thisorder.price
    tid = thisorder.tid
    pg_token = request.GET['pg_token']
    body = {
        'cid': 'TC0ONETIME',
        'tid': tid,
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'pg_token': pg_token,
        'total_amount': total_cost
    }

    res = requests.post(url=check_url, headers=headers, data=body)
    approve_data = json.loads(res.text)
    thisorder.status = 'c'
    thisorder.save(update_fields=["status"])
    return JsonResponse(approve_data)


def Cancel(request):

    user = request.GET.get('user')
    userM = User.objects.get(username=user)
    realorder = Order.objects.filter(creator=userM)
    thisorder = realorder.filter(status='a').order_by('id').last()
    thisorder.delete()
    redirection_url =  'http://10.16.147.173:3000/menu/'
    return HttpResponseRedirect(redirection_url)

def Fail(request):
    user = request.GET.get('user')
    userM = User.objects.get(username=user)
    realorder = Order.objects.filter(creator=userM)
    thisorder = realorder.filter(status='a').order_by('id').last()
    thisorder.delete()
    redirection_url =  'http://10.16.147.173:3000/menu/'
    return HttpResponseRedirect(redirection_url)
