import collections


def part1(states):
    new_states = []
    for x in range(0, 80):
        for state in states:
            new_state_value = (state - 1) if state - 1 > 0 else (state - 1) % 7
            new_states.append(new_state_value)
            if state == 0:
                new_states.append(8)
        states = new_states
        new_states = []
    return len(states)


def part2(states):
    states_as_dict = collections.Counter(states)
    for day in range(0, 256):
        new_states = collections.Counter({8: states_as_dict[0], 6: states_as_dict[0]})
        new_states.update({k - 1: v for k, v in states_as_dict.items() if k > 0})
        states_as_dict = new_states

    return sum(states_as_dict.values())


if __name__ == "__main__":
    input_states = open("input.txt", "r").read().split(",")
    states_as_int = list(map(int, input_states))
    print(part1(states_as_int))
    print(part2(states_as_int))
