from typing import Dict, List
from collections import namedtuple
from copy import deepcopy

Relation = namedtuple("Relation", "parent child")


def build_relation(input: str) -> Relation:
    tokens = input.split(' ')
    return Relation(tokens[1], tokens[7])


def build_step_map(relations: List[Relation]) -> Dict[str, List[str]]:
    steps: Dict[str, List[str]] = {}

    for relation in relations:
        if relation.child not in steps:
            steps[relation.child] = []
        if relation.parent not in steps:
            steps[relation.parent] = []
        steps[relation.child].append(relation.parent)

    return steps


Worker = namedtuple("Worker", "step seconds")


def remove_step_from_dict(steps: Dict[str, List[str]], step: str):
    for parent_list in steps.values():
        if step in parent_list:
            parent_list.remove(step)
    steps.pop(step)


def part_1(steps: Dict[str, List[str]]) -> List[str]:
    result: List[str] = []
    queue:  List[str] = []
    while len(steps.keys()) > 0:
        for step, blockers in steps.items():
            if len(blockers) == 0 and step not in queue:
                queue.append(step)
        queue = sorted(queue)
        next_step = queue.pop(0)
        result += next_step
        remove_step_from_dict(steps, next_step)
    return "".join(result)


def part_2(steps: Dict[str, List[str]], num_workers: int, base_time: int) -> int:
    result = 0
    workers: List[Worker] = []
    queue: List[str] = []
    while len(steps.keys()) > 0:
        for step, blockers in steps.items():
            if len(blockers) == 0 and step not in queue and step not in [worker.step for worker in workers]:
                queue.append(step)
        queue = sorted(queue)
        while len(workers) < num_workers and len(queue) > 0:
            next_step = queue.pop(0)
            workers.append(Worker(next_step, ord(next_step)-64+base_time))
        next_worker_to_finish = min(workers, key=lambda worker: worker.seconds)
        workers.remove(next_worker_to_finish)
        workers = [Worker(worker.step, worker.seconds - next_worker_to_finish.seconds) for worker in workers]
        result += next_worker_to_finish.seconds
        remove_step_from_dict(steps, next_worker_to_finish.step)
    return result


if __name__ == '__main__':
    inputs = open('./input.txt').read().split('\n')

    relations = [build_relation(input) for input in inputs]
    steps = build_step_map(relations)
    print(f'part 1: {part_1(deepcopy(steps))}')
    print(f'part 2: {part_2(deepcopy(steps), 5, 60)}')



