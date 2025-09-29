import math

actions = ["Procrastinate", "Study", "Sleep"]
states  = ["Not Motivated", "Motivated", "Not Motivated"]

# Just fake small probabilities for fun
probs = [0.3, 0.6, 0.2]
log_score = sum(math.log(p) for p in probs)

print("Student did:", actions)
print("Hidden states:", states)
print("Log score:", round(log_score, 2))

if states[-1] == "Not Motivated":
    print("Decision: Give motivation! 💡")
else:
    print("Decision: Student is doing well ✅")
