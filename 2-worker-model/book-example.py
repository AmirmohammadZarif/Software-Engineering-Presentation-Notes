from multiprocessing import Process, Queue
import time
import random

def worker(task_queue, worker_id):
    while not task_queue.empty():
        package_id = task_queue.get()
        print(f"worker {worker_id} is delivering {package_id}")
        delivery_time = random.randint(2, 5)  
        time.sleep(delivery_time)
        print(f"worker {worker_id} delivered the package {package_id} in {delivery_time}")

if __name__ == '__main__':
    NUM_WORKERS = 4
    
    task_queue = Queue()
    for package_id in range(10): 
        task_queue.put(package_id)
    
    processes = []
    for worker_id in range(NUM_WORKERS):
        p = Process(target=worker, args=(task_queue, worker_id))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("All packages delivered")