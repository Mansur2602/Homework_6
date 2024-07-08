import threading
import time

def create_file():
    time.sleep(1)
    with open(f"file_{time.time()}.txt", "w") as f:
        f.write("File created")

start = time.time()
threads = []
for i in range(100):
    thread = threading.Thread(target=create_file)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print(f"общее время: {end-start}")

