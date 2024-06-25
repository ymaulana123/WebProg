from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from about.models import AccountUser


@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    if created:
        # Check if student number or email already exists
        student_number_exists = AccountUser.objects.filter(account_user_student_number=instance.account_user_student_number).exists()
        email_exists = User.objects.filter(username=instance.account_user_student_number).exists()

        if student_number_exists or email_exists:
            # If the student number or email exists, handle the case as needed
            # For instance, you might want to raise a validation error
            return HttpResponse('Data already exists')
        else:
            # Create User and AccountUser if they do not exist
            user = User.objects.create(username=instance.account_user_student_number, email=instance.email)
            instance.account_user_related_user = user
            instance.save()
    else:
        # If not created, simply return, no further action needed
        return

# Note: Ensure that the redirect or HttpResponse logic is handled within the view, 
# not within the signal handler. Signal handlers should not directly handle HTTP responses.
