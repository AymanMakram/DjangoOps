from celery import shared_task

@shared_task
def send_test_email():
    return "Task executed successfully"
