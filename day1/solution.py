from tqdm import tqdm

def get_next_point(pointing_to: int, instruction: str) -> int:
    if instruction[0] == 'L':
        move = int(instruction.lstrip('L'))
        crossing_zero_count = move // 100
        move = move % 100
        if pointing_to - move < 0:
            if pointing_to != 0:
                crossing_zero_count += 1 
            pointing_to = 100 - (move - pointing_to)
        else:
            pointing_to -= move
    else:
        move = int(instruction.lstrip('R'))
        crossing_zero_count = move // 100
        move = move % 100
        if pointing_to + move > 100:
            if pointing_to != 0:
                crossing_zero_count += 1 
            pointing_to = pointing_to + move - 100
        else:
            pointing_to += move
            pointing_to %= 100
    assert pointing_to <= 99 and pointing_to >=0
    if pointing_to == 0:
        return pointing_to, crossing_zero_count + 1
    else:
        return pointing_to, crossing_zero_count

with open('input.txt', 'r') as f:
    instructions = [line.strip() for line in f if line.strip()]


pointing_to = 50
count = 0
for instruction in tqdm(instructions, desc="Processing instructions"):
    pointing_to,crossing_zero_count = get_next_point(pointing_to=pointing_to, instruction=instruction)
    count += crossing_zero_count

print(count)