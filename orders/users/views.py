# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
#
# from .forms import SignupForm
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.core.mail import EmailMessage
# from django.contrib.auth import get_user_model
#
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import CreateModelMixin
# from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
UserModel = get_user_model()

from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import UserSerializer
from .signals import new_user_registered
from .models import ConfirmEmailToken


class RegisterAccount(APIView):
    """
    Для регистрации покупателей
    """
    # Регистрация методом POST
    def post(self, request, *args, **kwargs):
        print(f'request class is: {type(request.data)}')
        # проверяем обязательные аргументы
        if {'first_name', 'middle_name', 'last_name', 'email', 'password', 'password2', 'company', 'position'}.issubset(request.data):
            print(f'All data are in request.data')
            # errors = {}

            # проверяем совпадение паролей
            if request.data['password'] != request.data['password2']:
                print(f'password != password2')
                return JsonResponse({'Status': False, 'Errors': {'password': ['Пароли не совпадают']}})
            print(f'password == password2 ==> True')
            # проверяем пароль на сложность
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                password_error_array = []
                # noinspection PyTypeChecker
                for item in password_error:
                    password_error_array.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': password_error_array}})
            else:
                # print('проверяем данные для уникальности имени пользователя')
                # # проверяем данные для уникальности имени пользователя
                # request.data._mutable = True
                # request.data.update({})
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    # сохраняем пользователя
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    new_user_registered.send(sender=self.__class__,
                                             user=user,
                                             # user_id=user.id,
                                             # user_full_name=user.get_full_name,
                                             request=request)
                    return JsonResponse({'Status': True, 'Message': 'Проверьте вашу почту.'})
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class ConfirmAccount(APIView):
    """
    Класс для подтверждения почтового адреса
    """
    # Регистрация методом POST
    def post(self, request, *args, **kwargs):

        # проверяем обязательные аргументы
        if {'email', 'token'}.issubset(request.data):

            token = ConfirmEmailToken.objects.filter(user__email=request.data['email'],
                                                     key=request.data['token']).first()
            if token:
                token.user.is_active = True
                token.user.save()
                token.delete()
                return JsonResponse({'Status': True, 'Message': 'Поздравляем. Регистрация прошла успешно!'})
            else:
                return JsonResponse({'Status': False, 'Errors': 'Неправильно указан токен или email'})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

















# === Archived records ===

# class CreateUserView(CreateModelMixin, GenericViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserCreateSerializer


# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = UserModel.objects.all()



# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Активания вашего аккаунта в самом лучшем интернет магазине.'
#             message = render_to_string('registration/activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(subject=subject, body=message, to=[to_email, ])
#             email.send()
#             return HttpResponse('Мы почти закончили. Пожалуйста проверьте сообщение на почте!')
#     else:
#         form = SignupForm()
#     return render(request, 'registration/signup.html', {'form': form})
#
# from rest_framework import status
# from rest_framework.decorators import api_view
#
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = UserModel.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Спасибо, аккаунт подтвержден. Теперь вы можете перейти в созданию первого заказа.')
#     else:
#         return HttpResponse('Activation link is invalid!')
#
#
# # Код ниже просто для закрепления материала из Туториала DRF
# from .serializers import UserSerializer
# from rest_framework import viewsets

# class UserViewSet(viewsets.ModelViewSet):
#     print(f'Create new object of UserViewSet class!')
#     queryset = UserModel.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

