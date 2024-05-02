from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # 该装饰器使此次请求忽略 csrf 校验
from django.contrib.auth.models import User
from django.contrib.auth import login
from backend.models.user.account.models import Member

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getinfo(request):
    user = request.user
    member = Member.objects.get(user=user)
    return Response({
        'message': '身份验证成功!',
        'username': user.username,
        'avatar': member.avatar,
        'description': member.description,
    })


@api_view(['POST', 'GET'])
def login(request):
    user = get_object_or_404(User, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response({
            "state": "failed",
            "message": "该用户未注册!"
        })
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "state": "success",
        "message": "调用 rest api 成功",
        "jwt_token": str(token),
    })


@csrf_exempt
def register(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    password_confirm = data.get('password_confirm')

    if not username or not password:
        return JsonResponse({
            "message": "用户名或密码不能为空！"
        })
    elif password != password_confirm:
        return JsonResponse({
            "message": "两次输入密码不一致！"
        })
    elif User.objects.filter(username=username).exists():
        return JsonResponse({
            "message": "此用户名已存在！"
        })

    #  存入数据库
    user = User(username=username)
    user.set_password(password)
    user.save()

    Member.objects.create(user=user, avater="", description=f"Hello, {username}!")
    login(request, user)  # 用该用户登录

    return JsonResponse({
        "state": 200,
        "message": "register successfully!"
    })
