from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def login(self, **kwargs):
      if kwargs is not None:
        errors = { }
        if len(kwargs['password']) ==0:
          errors['password'] = "Please Enter a Password"
        if len(kwargs['username']) ==0:
          errors['username'] = "Please Enter a username"
        if len(errors)!=0:
          return (False, errors)
        else:
          user = self.filter (username = kwargs['username'])
          if not user:
            errors['user'] = "username/password combination not found"
            return (False, errors)
          else:
            if bcrypt.checkpw(kwargs['password'].encode('utf-8'), user[0].password.encode('utf-8')):
              return (True, user[0])
            else:
              errors['user'] = 'username/Password Combination Not Found'
              return (False, errors)
    def isValid(self, email, email_REGEX):
        if not email_REGEX. match (email):
           return False
        else:
           return True
# from __future__ import unicode_literals
# from django.db import models
# from django.contrib import messages
# import re
# import bcrypt

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# class UserManager(models.Manager):
#     def login(self, **kwargs):
#       if kwargs is not None:
#         errors = { }
#         if len(kwargs['password']) ==0:
#           errors['password'] = "Please Enter a Password"
#         if len(kwargs['email']) ==0:
#           errors['email'] = "Please Enter a Email"
#         if len(errors)!=0:
#           return (False, errors)
#         else:
#           user = self.filter (email = kwargs['email'])
#           if not user:
#             errors['user'] = "Email/password combination not found"
#             return (False, errors)
#           else:
#             if bcrypt.checkpw(kwargs['password'].encode('utf-8'), user[0].password.encode('utf-8')):
#               return (True, user[0])
#             else:
#               errors['user'] = 'Email/Password Combination Not Found'
#               return (False, errors)
#     def isValid(self, email, email_REGEX):
#         if not email_REGEX. match (email):
#            return False
#         else:
#            return True
    # def register (self, **kwargs):
    #   if kwargs is not None:
    #     errors = { }
    #     if len(kwargs['first_name']) <2:
    #       errors['first_name'] = "First name should have at least two characters"
    #     if len(kwargs['last_name']) <2:
    #       errors['last_name'] = "Last name should have at least two characters"
    #     if len(kwargs['email']) ==0:
    #       errors['email'] = "Email is required. "
    #     elif not EMAIL_REGEX.match(kwargs['email']):
    #       errors['email'] = "Please enter a valid email. "
    #     if len(kwargs['password']) <8:
    #       errors['password'] = "Password should have at least two characters"
    #     # if kwargs['password'] !=kwargs['confirm_password']:
    #       # errors['confirm_password'] = "password must match"
    #     if len(errors) is not 0:
    #       return (False, errors)
    #     else:
    #       hashed = bcrypt.hashpw(kwargs['password'].encode('utf-8'), bcrypt.gensalt())
    #       user = self.create(first_name = kwargs['first_name'], last_name = kwargs['last_name'], email = kwargs['email'], password = hashed)
    #       user.save()
    #       return (True, user)
    #   else:
    #     messages.add_message(request, messages.INFO, "Please Try Registration Again")
    #     return

class User (models.Model):
    name = models.CharField (max_length = 45)
    username = models.CharField (max_length = 45)
    # email = models.EmailField (max_length = 100)
    password = models.CharField (max_length = 200)
    date_hired = models.DateField (null = True)
    created_at = models.DateField (auto_now_add = True)
    updated_at = models.DateField (auto_now = True)
    objects = UserManager()




