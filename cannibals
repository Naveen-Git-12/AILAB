# Start
m_left, c_left = 3, 3
m_right, c_right = 0, 0
boat = "L"

# Safe moves sequence
moves = [(0,1),(0,2),(0,1),(2,0),(1,1),(0,2),(0,1),(2,0),(1,1),(0,1),(1,1)]

print("Missionaries and Cannibals Game:")

for step, move in enumerate(moves, start=1):
    m, c = move
    if boat == "L":
        m_left -= m
        c_left -= c
        m_right += m
        c_right += c
        boat = "R"
    else:
        m_left += m
        c_left += c
        m_right -= m
        c_right -= c
        boat = "L"
    
    print(f"Step {step}:")
    print("  Missionaries on left:", m_left)
    print("  Cannibals on left:", c_left)
    print("  Missionaries on right:", m_right)
    print("  Cannibals on right:", c_right)
    print("  Boat is on", "left" if boat=="L" else "right")
    print("---------------------------")
