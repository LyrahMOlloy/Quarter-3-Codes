import numpy as np

names = ["Kyoko", "Xienn", "Brad "]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

for i in range(len(names)):
    total_steps = steps[i].sum()
    avg_steps = steps[i].mean()
    min_steps = steps[i].min()
    max_steps = steps[i].max()

    print(names[i], "- Total Steps:", int(total_steps), "|", "Average:", int(avg_steps), "|", "Min:", int(min_steps), "|", "Max:", int(max_steps))