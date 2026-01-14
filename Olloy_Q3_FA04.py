import numpy as np

names = ["Kyoko", "Xienn", "Brad "]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

total_steps_list = {
    "Kyoko" : 0,
    "Xienn" : 0,
    "Brad " : 0 
}

print("Step Count Table")
print("Name | Mon | Tue | Wed | Thu | Fri")
for i in range(len(names)):
    print(names[i],":", steps[i])  

for i in range(len(names)):
    total_steps = steps[i].sum()
    total_steps_list[names[i]] = total_steps

high_total = max(total_steps_list.items(),key=lambda x: x[1])
low_total = min(total_steps_list.items(),key=lambda x: x[1])

difference = high_total[1] - low_total[1]

print("Highest Total Steps:", high_total[0], "with", int(high_total[1]), "steps!")
print("Lowest Total Steps:", low_total[0], "with", int(low_total[1]), "steps!")
print("Difference between the two highest and lowest totals:", int(difference), "steps.")