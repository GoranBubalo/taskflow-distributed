# exceptions.py

class TaskFlowError(Exception):
    """Base exception for all TaskFlow errors"""
    pass

# Task-related errors
class TaskError(TaskFlowError):
    """Base exception for task-related errors"""
    pass

class TaskCreationError(TaskError):
    """Raised when a task cannot be created due to validation or database constraints"""
    pass

class TaskNotFoundError(TaskError):
    """Raised when a requested task does not exist"""
    pass

class TaskUpdateError(TaskError):
    """Raised when an error occurs while updating a task"""
    pass

class InvalidTaskDataError(TaskError):
    """Raised when task data violates validation rules"""
    pass

# Worker-related errors
class WorkerError(TaskFlowError):
    """Base exception for worker-related errors"""
    pass

class WorkerRegistrationError(WorkerError):
    """Raised when a worker fails to register with the system"""
    pass

class WorkerProcessingError(WorkerError):
    """Raised when a worker encounters an error while processing a task"""
    pass

# Queue-related errors
class QueueError(TaskFlowError):
    """Base exception for queue-related errors"""
    pass

class QueueConnectionError(QueueError):
    """Raised when there is a failure connecting to the task queue"""
    pass

class QueueTimeoutError(QueueError):
    """Raised when a task times out in the queue"""
    pass

# API-related errors
class APIError(TaskFlowError):
    """Base exception for API-related errors"""
    pass

class UnauthorizedError(APIError):
    """Raised when a user is not authorized to perform an action"""
    pass

class InvalidRequestError(APIError):
    """Raised when an API request is invalid or malformed"""
    pass

class DependencyError(TaskFlowError):
    """Raised when a required dependency is missing or misconfigured"""
    pass
