from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from .constants import ROLE_CHOICES

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, default="")
    first_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    roll = models.CharField(max_length=10, blank=True, null=True, default="")
    register_id = models.CharField(max_length=10, blank=True, null=True, default="")
    bio = models.TextField(blank=True, default="")
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    phone_number = models.CharField(max_length=15, blank=True, null=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
