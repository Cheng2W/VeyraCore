from app.celery_app import celery_app


@celery_app.task
def example_task(x: int, y: int) -> int:
    """Example Celery task."""
    return x + y
