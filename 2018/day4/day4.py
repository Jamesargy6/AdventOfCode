from typing import Optional, List, Dict
from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse
from enum import Enum
from collections import defaultdict


class Action(Enum):
    ASLEEP: str = 'ASLEEP'
    AWAKE: str = 'AWAKE'
    CHANGE: str = 'CHANGE'


@dataclass
class Log:
    timestamp: datetime
    action: Action
    guard_id: Optional[str]


@dataclass
class Guard:
    guard_id: str
    minutes_map: Dict[int, int]
    minutes_spent_asleep: int = 0


def parse_log(input: str) -> Log:
    l_bracket = input.find('[')
    r_bracket = input.find(']')
    date = parse(input[l_bracket+1:r_bracket])

    action_dict = {
        'falls': Action.ASLEEP,
        'wakes': Action.AWAKE,
        'Guard': Action.CHANGE

    }

    action_tokens = input[r_bracket+2:].split(' ')
    action = action_dict[action_tokens[0]]
    id: str = None
    if action == Action.CHANGE:
        id = action_tokens[1]

    return Log(date, action, id)


def get_sorted_logs(input: str) -> List[Log]:
    input_lines = input.split('\n')
    logs = [parse_log(line) for line in input_lines]
    return sorted(logs, key=lambda log: log.timestamp)


def get_minutes(start: datetime, stop: datetime) -> List[int]:
    delta = (stop - start).seconds//60
    return [minute for minute in range(start.minute, start.minute+delta)]


def get_minutes_asleep_by_guard(logs: List[Log]) -> Dict[str, Guard]:
    guard_map:  Dict[str, Guard] = {}
    current_guard_id: str
    sleep_timestamp: datetime
    for log in logs:
        if log.action == Action.CHANGE:
            current_guard_id = log.guard_id
            if current_guard_id not in guard_map:
                guard_map[current_guard_id] = Guard(current_guard_id, defaultdict(int))
        elif log.action == Action.ASLEEP:
            sleep_timestamp = log.timestamp
        elif log.action == Action.AWAKE:
            minutes_asleep = get_minutes(sleep_timestamp, log.timestamp)
            for minute in minutes_asleep:
                guard_map[current_guard_id].minutes_map[minute] += 1
            guard_map[current_guard_id].minutes_spent_asleep += len(minutes_asleep)
    return guard_map


def part_1(guard_map: Dict[str, Guard]):
    sorted_guard_ids = sorted(guard_map, key=(lambda key: guard_map[key].minutes_spent_asleep), reverse=True)
    sleepiest_guard = guard_map[sorted_guard_ids[0]]
    sorted_minutes = sorted(sleepiest_guard.minutes_map, key=(lambda key: sleepiest_guard.minutes_map[key]),
                            reverse=True)
    sleepiest_minute = sorted_minutes[0]
    print(sleepiest_guard.guard_id, sleepiest_minute)

def part_2(guard_map: Dict[str, Guard]):
    sleepiest_minute: int
    sleepiest_guard_id: str
    max_value: int = 0
    for id, guard in guard_map.items():
        for minute in guard.minutes_map:
            value = guard.minutes_map[minute]
            if value > max_value:
                max_value = value
                sleepiest_minute = minute
                sleepiest_guard_id = id
    print(sleepiest_guard_id, sleepiest_minute)



if __name__ == '__main__':
    input = open('./input.txt').read()
    sorted_logs = get_sorted_logs(input)
    guard_map = get_minutes_asleep_by_guard(sorted_logs)
    part_1(guard_map)
    part_2(guard_map)

