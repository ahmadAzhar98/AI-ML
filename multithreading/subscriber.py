import redis
import time
import multiprocessing
import json
from datetime import datetime

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def execute_math_operation(task_data, time_limit=5):
    start_time = time.time()
    try:
        print(f"Processing task {task_data['id']}: {task_data['type']}({task_data['a']}, {task_data['b']})")
        
        # Perform the requested operation
        if task_data['type'] == 'add':
            result = task_data['a'] + task_data['b']
            operation_str = f"{task_data['a']} + {task_data['b']}"
        elif task_data['type'] == 'multiply':
            result = task_data['a'] * task_data['b']
            operation_str = f"{task_data['a']} * {task_data['b']}"
        elif task_data['type'] == 'divide':
            if task_data['b'] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = task_data['a'] / task_data['b']
            operation_str = f"{task_data['a']} / {task_data['b']}"
        else:
            raise ValueError(f"Unknown operation: {task_data['type']}")
        
        # Simulate variable processing time (1-3 seconds)
        processing_time = min(3, max(1, task_data['id'] % 3 + 1))
        time.sleep(processing_time)
        
        # Check if we've exceeded time limit
        if time.time() - start_time > time_limit:
            raise TimeoutError(f"Task {task_data['id']} exceeded time limit")
            
        print(f"Task {task_data['id']} result: {operation_str} = {result} (took {time.time()-start_time:.2f}s)")
        return True
        
    except TimeoutError as e:
        print(f"Timeout: {e}")
        return False
    except Exception as e:
        print(f"Error in task {task_data['id']}: {e}")
        return False

def worker(queue_name='math_tasks'):
    """Worker that processes math tasks from the queue"""
    while True:
        # Get a task from Redis (blocking pop with 5s timeout)
        task = r.blpop(queue_name, timeout=5)
        
        if task is None:
            print("No tasks in queue, worker exiting")
            break
            
        # task is a tuple: (queue_name, task_data)
        _, task_data_json = task
        
        try:
            task_data = json.loads(task_data_json)
            
            # Create a process for each task
            p = multiprocessing.Process(
                target=execute_math_operation,
                args=(task_data,)
            )
            p.start()
            
            # Wait for the process to complete or timeout after 5 seconds
            p.join(timeout=5)
            
            # If process is still alive after timeout, terminate it
            if p.is_alive():
                print(f"Terminating task {task_data['id']} due to timeout")
                p.terminate()
                p.join()
                
        except json.JSONDecodeError:
            print("Error: Invalid task data format")
        except Exception as e:
            print(f"Error processing task: {e}")

if __name__ == '__main__':
    print("Starting math task worker...")
    worker()