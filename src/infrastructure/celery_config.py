from celery import Celery

celery_app = Celery(
    "taskflow",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

# Celery configuration
celery_app.conf.task_routes = {"tasks.*": {"queue": "default"}}
celery_app.conf.update(task_serializer="json", result_serializer="json")
