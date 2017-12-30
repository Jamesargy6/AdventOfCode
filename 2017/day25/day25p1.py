tape = [0]*5001
cursor = 2500
state = "A"

def executeState(tapeVal, cursorMove, nextState):
	global tape, cursor, state
	tape[cursor] = tapeVal
	cursor += cursorMove
	state = nextState

for x in range(12368930):
	if state == "A":
		if tape[cursor] == 0:
			executeState(1, 1, "B")
		else:
			executeState(0, 1, "C")
		continue
	
	elif state == "B":
		if tape[cursor] == 0:
			executeState(0, -1, "A")
		else:
			executeState(0, 1, "D")
		
		continue

	elif state == "C":
		if tape[cursor] == 0:
			executeState(1, 1, "D")
		else:
			executeState(1, 1, "A")
		
		continue

	elif state == "D":
		if tape[cursor] == 0:
			executeState(1, -1, "E")
		else:
			executeState(0, -1, "D")
		
		continue

	elif state == "E":
		if tape[cursor] == 0:
			executeState(1, 1, "F")
		else:
			executeState(1, -1, "B")
		
		continue

	elif state == "F":
		if tape[cursor] == 0:
			executeState(1, 1, "A")
		else:
			executeState(1, 1, "E")
		
		continue

print(tape.count(1))
