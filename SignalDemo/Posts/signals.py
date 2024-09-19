# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, LogEntry
import threading

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received: Starting processing...")
    time.sleep(5)  # Simulating a time-consuming task
    print("Signal processing complete.")
    print(f"Signal handler thread ID: {threading.get_ident()}")


@receiver(post_save, sender=MyModel)
def log_model_save(sender, instance, **kwargs):
    print("Signal triggered: Creating log entry.")
    # This creates a log entry when the model is saved
    LogEntry.objects.create(message=f"MyModel {instance.name} was saved.")
