import os
import random

solved = [
    item for item in os.listdir('.') if os.path.isdir(item) and not item.startswith('.')
]

is_revise = random.random() < 0.3

if is_revise:
    problem = random.choice(solved)
    print(f"Rewise {problem}")
else:
    solved_ids = {int(folder.split('-')[0]) for folder in solved}
    unsolved = list(set(range(1, 1001)) - solved_ids)
    problem = random.choice(unsolved)
    print(f"Solve {problem}")
