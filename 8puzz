# 8puzz
from collections import deque

# BFS to solve 8 puzzle
def solve(start, goal):
    q = deque([(start, [])])
    seen = {tuple(start)}
    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]
        i = state.index(0)   # blank tile position
        r, c = divmod(i, 3)  # row, col
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                ni = nr*3 + nc
                new = state[:]
                new[i], new[ni] = new[ni], new[i]
                if tuple(new) not in seen:
                    seen.add(tuple(new))
                    q.append((new, path+[state]))
    return None

# Display steps
def show(path):
    if not path:
        print("No solution")
        return
    for step, s in enumerate(path):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print("------")

# Example
start = [1,3,0,6,8,4,7,5,2]   # initial state
goal  = [1,2,3,4,5,6,7,8,0]   # goal state
solution = solve(start, goal)
show(solution)
