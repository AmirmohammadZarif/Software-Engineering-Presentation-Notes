from multiprocessing import Process, Queue
import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_worker_status(workers_status):
    clear_screen()
    print("\n🚚 Package Delivery System 📦\n")
    print("─" * 50)
    
    for worker_id, status in workers_status.items():
        if status['active']:
            progress = "=" * status['progress'] + ">" + "." * (20 - status['progress'])
            package = status['package']
            print(f"Worker {worker_id}: [{progress}] Package {package}")
        else:
            print(f"Worker {worker_id}: [IDLE]")
    print("─" * 50)

def worker(task_queue, worker_id, status_queue):
    while not task_queue.empty():
        package_id = task_queue.get()
        
        # Simulate delivery with progress bar
        delivery_time = random.randint(2, 4)
        steps = 20
        for step in range(steps + 1):
            status_queue.put((worker_id, {
                'active': True,
                'package': package_id,
                'progress': step
            }))
            time.sleep(delivery_time / steps)
            
    status_queue.put((worker_id, {'active': False}))

if __name__ == '__main__':
    NUM_WORKERS = 4
    
    task_queue = Queue()
    status_queue = Queue()
    
    # Initialize packages
    for package_id in range(10):
        task_queue.put(package_id)
    
    # Initialize worker status
    workers_status = {i: {'active': False} for i in range(NUM_WORKERS)}
    
    # Start workers
    processes = []
    for worker_id in range(NUM_WORKERS):
        p = Process(target=worker, args=(task_queue, worker_id, status_queue))
        processes.append(p)
        p.start()
    
    # Update visualization
    while any(p.is_alive() for p in processes):
        try:
            worker_id, status = status_queue.get_nowait()
            workers_status[worker_id] = status
            print_worker_status(workers_status)
        except:
            time.sleep(0.1)
    
    clear_screen()
    print("\n🎉 All packages delivered! 🎉\n")