from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    first = {'qtd_linhas': 1}
    second = {'qtd_linhas': 2}
    third = {'qtd_linhas': 3}

    queue.enqueue(first)
    queue.enqueue(third)
    queue.enqueue(second)

    assert len(queue) == 3

    assert queue.search(2) == second
    assert queue.search(0) == first

    assert queue.dequeue() == first

    with pytest.raises(IndexError):
        queue.search(4)
