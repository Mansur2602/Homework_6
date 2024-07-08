import time
import random
from multiprocessing import Pool

def create_file_with_random_number(file_name):
    with open(file_name, 'w') as file:
        random_number = random.randint(1, 1000)
        file.write(str(random_number))
        time.sleep(1)

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


pool = Pool()


file_names = [f"file_{i}.txt" for i in range(1000)]
pool.map(create_file_with_random_number, file_names)


execution_time = measure_time(create_file_with_random_number, "test.txt")
print(f"Общее время: {execution_time} секунд")
