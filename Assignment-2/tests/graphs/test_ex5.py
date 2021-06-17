import pytest
from graphs.ex5 import CourseSchedule


def test_can_finish():
    schedule = CourseSchedule(2, [[1,0]])
    assert schedule.can_finish() == True

def test_can_not_finish():
    schedule = CourseSchedule(2, [[1,0], [0,1]])
    assert schedule.can_finish() == False