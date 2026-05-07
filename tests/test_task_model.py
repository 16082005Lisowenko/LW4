import pytest
from src.models.task import Task, TaskStatus

def test_task_status_transition_valid():
    t = Task(title='Test')
    t.change_status(TaskStatus.IN_PROGRESS)
    assert t.status == TaskStatus.IN_PROGRESS

def test_task_status_transition_invalid():
    t = Task(title='Test')
    with pytest.raises(ValueError):
        t.change_status(TaskStatus.DONE)

def test_task_status_none_crash():
    t = Task(title='Test')
    with pytest.raises(ValueError, match='Status cannot be None'):
        t.change_status(None)
