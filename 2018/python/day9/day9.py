import sys


class Marble:
    def __init__(self, value: int):
        self.value = value
        self.previous: Marble = self
        self.next: Marble = self


def play_game(input_players: int, input_last_marble_score: int) -> int:
    current_marble = Marble(0)
    
    players = [0 for _ in range(input_players)]
    current_player = 0

    for marble_value in range(1, input_last_marble_score+1):
        if marble_value % 23 == 0:
            for x in range(7):
                current_marble = current_marble.previous
            players[current_player] += current_marble.value
            current_marble = current_marble.next
            current_marble.previous.previous.next = current_marble
            current_marble.previous = current_marble.previous.previous
            players[current_player] += marble_value

        else:
            new_marble = Marble(marble_value)
            adj_marble = current_marble.next
            new_marble.next = adj_marble.next
            new_marble.next.previous = new_marble
            new_marble.previous = adj_marble
            adj_marble.next = new_marble
            current_marble = new_marble

        current_player = (current_player+1) % input_players
    return max(players)


if __name__ == '__main__':

    input_players, input_last_marble_score = int(sys.argv[1]), int(sys.argv[2])

    result = play_game(input_players, input_last_marble_score)
    print(result)