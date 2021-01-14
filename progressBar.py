---
#Project: To add a Progress Bar
#Author : Priya Mondal
---
#Module Used: tqdm

from tqdm import tqdm, trange
import time

for i in tqdm(range(5)):   #To make it more clean & instead of using iterable, you can use "trange(5)" to bake it.
    time.sleep(0.4)
