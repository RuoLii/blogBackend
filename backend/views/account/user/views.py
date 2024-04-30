from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # 该装饰器使此次请求忽略 csrf 校验


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

    return JsonResponse({
        "state": 200,
        "message": "register successfully!"
    })
