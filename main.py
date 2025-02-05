from datetime import datetime
import random
filename = 'dokidoki.txt'

with open(filename, 'a') as f:
    now = datetime.now()
    f.write(f'Today is {now.strftime("%Y-%m-%d")}\n')
    l1 = ["David", "Lucy", "Rebecca", "Maine", "Jackie", "Dorio"]
    f.write(f'This one is for you '+l1[random.randint(0,5)]+'\n')