# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from nomapp.models import MedicalReport
from django.core.mail import send_mail
from nomapp.models import MedicalReport

@receiver(post_save, sender=MedicalReport)
def notify_doctor(sender, instance, created, **kwargs):
    if created:
        subject = 'New Medical Report'
        message = f'Hello {instance.doctor.username},\n\nYou have a new medical report to review.'
        from_email = 'samaraouadi7@gmail.com'  # Update with your email
        to_email = [instance.doctor.email]

        send_mail(subject, message, from_email, to_email)
