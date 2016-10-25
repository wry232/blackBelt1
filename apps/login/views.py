# from django.shortcuts import render, redirect, HttpResponse
# from django.utils.dateparse import parse_date
# from .models import User
# import re
# from django.contrib import messages
# # import bcrypt
# import bcrypt
# from django.core.urlresolvers import reverse
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile (r'^(.*?[a-zA-Z]){2,}.*$')
# PASSWORD_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
# def index(request):
#     return render (request, 'login/index.html')
# def logout(request):
#     request.session.clear()
#     return redirect(reverse('login:index'))
# def login(request):
#     if request.method =='POST':
#         result = User.objects.login(email = request.POST['email'], password = request.POST['password'])
#         if result[0]:
#             request.session['user_id'] = result[1].id
#             request.session['name'] = result[1].name
#             return redirect(reverse('black:appointments'))
#         else:
#             for error in result[1]:
#                 messages.add_message(request, messages.INFO, result[1][error])
#             return redirect(reverse('login:index'))
#     else:
#         messages.add_message(request, messages.INFO, 'Please Try Again')
#         return redirect(reverse('black:appointments'))

from django.shortcuts import render, redirect, HttpResponse
from django.utils.dateparse import parse_date
from .models import User
import re
from django.contrib import messages
# import bcrypt
import bcrypt
from django.core.urlresolvers import reverse
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile (r'^(.*?[a-zA-Z]){2,}.*$')
PASSWORD_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
def index(request):
    return render (request, 'login/index.html')
def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))
def login(request):
    if request.method =='POST':
        result = User.objects.login(username= request.POST['username'], password = request.POST['password'])
        if result[0]:
            request.session['user_id'] = result[1].id
            request.session['name'] = result[1].name
            request.session['username'] = result[1].username


            return redirect(reverse('Bapp:dashboard'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('login:index'))
    else:
        messages.add_message(request, messages.INFO, 'Please Try Again')
        return redirect(reverse('Bapp:dashboard'))
# def register(request):
#     name = request.POST['name']
#     # last_name = request.POST['last_name']
#     birthday = parse_date (request.POST['birthday'])
#     email = request.POST['email']
#     password  = request.POST['password']
#     confirm_password  = request.POST['confirm_password']
#     if (User.objects.isValid (name, NAME_REGEX) == False):
#         messages.error(request, 'Name is not valid. ')
#         return redirect('/')

#     elif (User.objects.isValid (email, EMAIL_REGEX) == False):
#         messages.error(request, 'Email is not valid. ')
#         return redirect('/')
#     elif (User.objects.isValid (password, PASSWORD_REGEX) == False):
#         messages.error(request, 'Password is not valid. ')
#         return redirect('/')
#     elif (confirm_password != password):
#         messages.error(request, 'Password is not consistant. ')
#         return redirect('/')

#     else:
#         password = password.encode()
#         hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#         user = User.objects.create (name = name, email = email, password = hashed, birthday = birthday)
def register(request):
    name = request.POST['name']
    username = request.POST['username']
    # email = request.POST['email']
    datehired = parse_date(request.POST['datehired'])
    password  = request.POST['password']
    confirm_password  = request.POST['confirm_password']
    if (User.objects.isValid (name, NAME_REGEX) == False):
        messages.error(request, 'First name is not valid. ')
        return redirect('/')
    elif (User.objects.isValid (username, NAME_REGEX) == False):
        messages.error(request, 'Last name is not valid. ')
        return redirect('/')
    # elif (User.objects.isValid (email, EMAIL_REGEX) == False):
    #     messages.error(request, 'Email is not valid. ')
    #     return redirect('/')
    elif (User.objects.isValid (password, PASSWORD_REGEX) == False):
        messages.error(request, 'Password is not valid. ')
        return redirect('/')

    elif (confirm_password != password):
        messages.error(request, 'Password is not consistant. ')
        return redirect('/')
    else:
        password = password.encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User.objects.create (name = name, username = username, password = hashed, date_hired = datehired)
        # context = {
        # 'first_name' : first_name
        # }
        # request.session['user_id'] = user.id
        # print "******", user.id
        # request.session['object'] = User.objects.filter (email = email)
        # return render (request, 'login/success.html')
        return redirect(reverse('login:index'))
# def success(request):
#     return render (request, 'login/success.html')

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile (r'^(.*?[a-zA-Z]){2,}.*$')
# PASSWORD_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

# def index(request):
#     context = {
#     'users': User.objects.all()
#     }
#     return render(request, 'login/index.html', context)
# def register(request):
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     email = request.POST['email']
#     password  = request.POST['password']
#     confirm_password  = request.POST['confirm_password']
#     if (User.objects.isValid (first_name, NAME_REGEX) == False):
#         messages.error(request, 'First name is not valid. ')
#         return redirect('/')
#     elif (User.objects.isValid (last_name, NAME_REGEX) == False):
#         messages.error(request, 'Last name is not valid. ')
#         return redirect('/')
#     elif (User.objects.isValid (email, EMAIL_REGEX) == False):
#         messages.error(request, 'Email is not valid. ')
#         return redirect('/')
#     elif (User.objects.isValid (password, PASSWORD_REGEX) == False):
#         messages.error(request, 'Password is not valid. ')
#         return redirect('/')
#     elif (confirm_password != password):
#         messages.error(request, 'Password is not consistant. ')
#         return redirect('/')
#     else:
#         password = password.encode()
#         hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#         User.objects.create (first_name = first_name, last_name = last_name, email = email, password = hashed, confirm_password =hashed)
#         context = {
#         'first_name' : first_name
#         }
#         # request.session['object'] = User.objects.filter (email = email)
#         return render (request, 'login/success.html', context)
# def login(request):
#     email = request.POST['email']
#     password  = request.POST['password']
#     password = password.encode()
#     # context = {
#     #     'first_name' : User.objects.get (email = email).first_name
#     #     }
#     obj = User.objects.get (email = email)
#     context = {
#         'first_name' : obj. first_name
#         }
#     # ps_hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#     ps_hashed = obj.password
#     ps_hashed = ps_hashed.encode()
#     if bcrypt.hashpw(password, ps_hashed):
#         return render (request, 'login/success.html', context)
#     else:
#         messages.same_password(request, 'email or password wrong, check and enter again. ')
#         return redirect('/')





# Create your views here.
