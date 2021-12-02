actions = open("input.txt", "r").read().splitlines()

actionsToValues = list(map(lambda x: x.split(" "), actions))
position = [0, 0]

for actionToValue in actionsToValues:
    if actionToValue[0] == 'forward':
        position[0] += int(actionToValue[1])
    if actionToValue[0] == 'down':
        position[1] += int(actionToValue[1])
    if actionToValue[0] == 'up':
        position[1] -= int(actionToValue[1])

print(position[0] * position[1])

positionAndAim = [0, 0, 0]
for actionToValue in actionsToValues:
    if actionToValue[0] == 'forward':
        positionAndAim[0] += int(actionToValue[1])
        positionAndAim[1] += int(actionToValue[1])* positionAndAim[2]
    if actionToValue[0] == 'down':
        positionAndAim[2] += int(actionToValue[1])
    if actionToValue[0] == 'up':
        positionAndAim[2] -= int(actionToValue[1])

print(positionAndAim[0] * positionAndAim[1])
