from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from apps.department.models import Department


class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, department, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            department = department,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name="Super", last_name="User", department=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            department=department
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True     
