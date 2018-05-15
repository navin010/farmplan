from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, gatekeeper_id, business_name, password=None):
        if not email:
            raise ValueError('User must provide email')

        if not gatekeeper_id:
            raise ValueError('User must provide gatekeeper id')

        if not business_name:
            raise ValueError('User must provide business name')

        user = self.model(
            email=self.normalize_email(email),
            gatekeeper_id=gatekeeper_id,
            business_name=business_name,
        )

        user.set_password(password)     #hashes password to prevent being stored as text
        user.save(using=self._db)
        return user

    def create_superuser(self, email, gatekeeper_id, business_name, password):

        user = self.create_user(
            email,
            password=password,
            gatekeeper_id=gatekeeper_id,
            business_name=business_name,
        )

        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class FarmUser(AbstractBaseUser):
    email = models.EmailField(max_length=100, default='', unique=True)
    gatekeeper_id = models.CharField(max_length=10, unique=True)
    business_name = models.CharField(max_length=100, default='', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'        #username field and password required by default

    REQUIRED_FIELDS = ['gatekeeper_id','business_name'] #used when executing command like python manage.py createsuperuser

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# Separate out non mandatory fields into profile class as too many fields/changes User class can cause issues in future
class Profile(models.Model):
    user = models.OneToOneField(FarmUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    town = models.CharField(max_length=50, default='')
    county = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=30, default='')
    post_code = models.CharField(max_length=10, default='')

