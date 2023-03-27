import time

start_time = time.time()

# Using list() function
a = list()
for i in range(1000000):
    a.append(i)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Using list(): {elapsed_time} seconds")

start_time = time.time()

# Using empty list syntax
a = []
for i in range(1000000):
    a.append(i)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Using empty list syntax: {elapsed_time} seconds")
