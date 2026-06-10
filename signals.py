import time 
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import Student

@receiver(post_save, sender=Student)
def student_saved(sender, instance, **kwargs):

    ##question 1
    print("Signal Started")
    time.sleep(5)
    print("Signal Completed")

    #question 2
    print("signal Thread ID:", threading.get_ident())

    #question 3
    print("Inside Signal")
    print("In Atomic Block:", connection.in_atomic_block)

    raise Exception("Signal Exception for Transection Test")
