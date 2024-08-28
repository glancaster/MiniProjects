# from python-mini-projects @ Mitesh

from tqdm import tqdm
from time import sleep

n_elements = 10
list_elements = range(0,n_elements+1)

for element in tqdm(list_elements, desc = "Looping over elements"):
    sleep(1)
print("Done")
