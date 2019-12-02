from typing import List

class ParseError(Exception):
	pass


def read_file_into_str_list(filename: str) -> List[str]:
	return [line.rstrip('\n') for line in open(filename)]

def read_file_into_int_list(filename: str) -> List[int]:
	return [int(line.rstrip('\n')) for line in open(filename)]

def read_line_into_int_list(filename: str) -> List[int]:
	return list(map(int, open(filename).read().split(','))