from email.headerregistry import Group
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    AbstractUser,
    PermissionsMixin,
    Group,
    Permission,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.contrib.auth import get_user_model



class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and return a regular user with an email, username, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with an email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)
# nomapp/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _




class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_groups',
        related_query_name='group',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_user_permissions',
        related_query_name='user_permission',
    )

    def is_patient(self):
        # Your logic to determine if the user is a patient
        # Replace the following line with your actual logic
        return hasattr(self, 'patient')

    def is_medic(self):
        # Your logic to determine if the user is a medic
        # Replace the following line with your actual logic
        return hasattr(self, 'medic')

    def __str__(self):
        return self.email

class MedicalReport(models.Model):
    
    def some_method(self):
        from nomapp.models import CustomUser  # Import CustomUser here
        # rest of the method
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='medical_reports')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='generated_reports')
    report_date = models.DateField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    comments = models.TextField(blank=True, null=True)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Medical Report for {self.patient.username} on {self.report_date}"


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Medic(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20)
    clinic_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class DoctorAvailability(models.Model):
    doctor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    monday_morning = models.BooleanField(default=False)
    monday_afternoon = models.BooleanField(default=False)
    specialty = models.CharField(max_length=255)  # Ajoutez le champ de spécialité
    clinic_address = models.CharField(max_length=255)  # Ajoutez le champ d'adresse de la clinique
    doctor_photo = models.ImageField(upload_to='doctor_photos/')  # Ajoutez le champ de photo du médecin

    def __str__(self):
        return f"Availability for {self.doctor.username}"



    