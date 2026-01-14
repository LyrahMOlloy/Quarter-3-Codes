import numpy as np

names = ["Kyoko", "Xienn", "Brad "]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

total_steps_list = {
    "Monday" : 0,
    "Tuesday" : 0,
    "Wednesday" : 0,
    "Thursday" : 0,
    "Friday" : 0
}


print("Step Count Table")
print("Days   | Total Steps")
for i in range(len(days)):
    total_steps = steps[:,i].sum()
    total_steps_list[days[i]] = total_steps
    print(days[i],":", total_steps)

high_total = max(total_steps_list.items(),key=lambda x: x[1])

print(high_total[0], "is the most active day with", int(high_total[1]), "steps!")