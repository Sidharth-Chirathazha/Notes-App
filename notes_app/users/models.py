import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, user_email, user_name, password=None):
        if not user_email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError('Users must have a username')

        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_email, user_name, password=None):
        user = self.create_user(
            user_email,
            password=password,
            user_name=user_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=150, unique=True)
    user_email = models.EmailField(unique=True)
    last_update = models.DateTimeField(auto_now=True)
    create_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_email