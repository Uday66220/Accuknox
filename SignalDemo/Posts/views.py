from django.shortcuts import render
import threading
from django.db import transaction
from .models import MyModel, LogEntry
import time

def test_signal_view(request):
    #print("Starting view logic...")
    start_time = time.time()

    # Creating an instance of MyModel which triggers the signal
    obj = MyModel.objects.create(name="Test Object")
    
    # End time after model save (and signal)
    end_time = time.time()

    #print(f"View logic complete in {end_time - start_time} seconds.")
    
    #print(f"Caller thread ID: {threading.get_ident()}")

    return render(request,"index.html")



def test_signal_transaction_view(request):
    try:
        with transaction.atomic():
            print("Starting transaction and saving MyModel...")
            obj = MyModel.objects.create(name="Test Object")  # This triggers the signal
            print("Raising an exception to trigger rollback.")
            raise Exception("Simulated exception to cause rollback.")
    except Exception as e:
        print(f"Transaction rolled back: {e}")

    # Check if log entry was created despite the rollback
    log_count = LogEntry.objects.count()
    print(f"Number of log entries: {log_count}")
    
    return render(request, 'index.html')

