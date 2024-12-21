from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_progress(active_tasks):
    clear_screen()
    print("\n" + "=" * 50)
    print("Thread Pool Visualization")
    print("=" * 50)
    
    for thread_name, task_info in sorted(active_tasks.items()):
        progress = int((time.time() - task_info['start']) * 20) 
        bar = '█' * min(progress, 20) + '▒' * (20 - min(progress, 20))
        print(f"\n{thread_name}:")
        print(f"Task {task_info['task_id']:2d} [{bar}] {time.time() - task_info['start']:.1f}s")
    
    print("\n" + "=" * 50)

def task(n, active_tasks):
    thread_name = threading.current_thread().name
    start_time = time.time()
    
    active_tasks[thread_name] = {
        'task_id': n,
        'start': start_time
    }
    
    for _ in range(10):
        display_progress(active_tasks)
        time.sleep(0.1)
    
    active_tasks.pop(thread_name, None)
    display_progress(active_tasks)

active_tasks = {}

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(task, i, active_tasks) for i in range(10)]
    for future in futures:
        future.result()

print("\nAll tasks completed!")