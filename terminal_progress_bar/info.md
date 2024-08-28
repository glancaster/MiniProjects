# Terminal Progress Bar

# Description
Using some looping business logic, a progress bar will appear in the terminal.


Tags: Python
Libraries: tqdm

# Code Review

[1] from tqdm import tqdm
    from time import sleep

[2] n_elements = 10
    list_elements = range(0,n_elements+1)

[3] for element in tqdm(list_elements, desc = "Looping over elements"):
        sleep(1)

    print("Done")

1. Import necessary libaries but the main focus is tqdm. The `from tqdm import tqdm` is importing the
tqdm module from the tqdm library. Also, this avoids writing tqdm.tqdm in your code.
2. Placeholder list for the module to loop over.
3. While this list is looping, a progress bar will appear in the Terminal.

# Resources
[tqdm](https://tqdm.github.io/)
