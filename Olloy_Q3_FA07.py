class colorz:
    RED = '\033[91m'
    LUVGREEN = '\033[92m'
    PURPLE = "\033[95m" 
    LUVRESET = "\033[0m"
    CYAN = 	"\033[96m"
    YELLOW = "\033[33m"


import numpy as np

names = ["Kyoko", "Xienn", "Brad "]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

print(colorz.PURPLE + "Daily Steps per Person" + colorz.LUVRESET)
print(colorz.LUVGREEN + "Name | Mon | Tue | Wed | Thu | Fri" + colorz.LUVRESET)
for i in range(len(names)):
    print(names[i],":", steps[i])  

print(colorz.RED + "Total Steps per Row (Name)" + colorz.LUVRESET)
totalStepsKyoko = steps[0].sum()
totalStepsXienn = steps[1].sum()
totalStepsBrad = steps[2].sum()

print("Kyoko:", totalStepsKyoko)
print("Xienn", totalStepsXienn)
print("Brad", totalStepsBrad)

print(colorz.YELLOW + "Average Steps per Row (Name)" + colorz.LUVRESET)
avgStepsKyoko = totalStepsKyoko / len(days)
avgStepsXienn = totalStepsXienn / len(days)
avgStepsBrad = totalStepsBrad / len(days)

print("Kyoko:", avgStepsKyoko)
print("Xienn:", avgStepsXienn)
print("Brad:", avgStepsBrad)

print(colorz.LUVGREEN + "Minimum Steps in the Entire Dataset" + colorz.LUVRESET)
minSteps = steps.min()
print("Minimum Steps:", minSteps)

print(colorz.CYAN + "Maximum Steps in the Entire Dataset" + colorz.LUVRESET)
maxSteps = steps.max()
print("Maximum Steps:", maxSteps)

print("Answer:")
print("Using arrays can help us analyze data more easily because the data is formatted "
"in a way that is already designed or ready for analysing. The compatibility of numpy with " \
"arrays also plays a lot into why placing data in arrays is very optimal for analysis. " \
"Numpy in the context of arrays offers built-in functions that replace very tedious ways of " \
"doing that specific action, like adding certain values using the sum funcion instead of individually " \
"accessing each value and adding them. Thus, using arrays to analyse data makes analysis easier.")
print( )
print("Overall, I think the the easiest part in summarizing the data is finding the minimum and maximum steps since it has" \
" the least lines to code, but if I really look at it in the big picture, everything was easy. This is all because of the " \
"built-in functions that numpy lets us use on arrays! Now, the difficult part about summarizing the data might be keeping " \
"track. There are many things you have to make variables of, and I think it was my own fault since I didn't use loops but " \
"nevertheless, I finished what I needed to do.")