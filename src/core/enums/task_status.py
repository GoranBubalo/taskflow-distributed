from enum import Enum as pyEnum

class TaskStatus(pyEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"