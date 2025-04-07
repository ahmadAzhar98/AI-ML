import redis
import time
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def create_math_task(task_type, a, b, task_id):
    return {
        'id': task_id,
        'type': task_type,
        'a': a,
        'b': b,
        'created_at': time.time()
    }

def push_math_tasks(queue_name='math_tasks'):
    tasks = [
        ('add', 5, 3, 1),        
        ('multiply', 4, 6, 2),  
        ('divide', 10, 2, 3),    
        ('divide', 8, 0, 4),    
        ('add', 7, 9, 5),        
        ('multiply', 2, 8, 6)    
    ]
    
    for task_type, a, b, task_id in tasks:
        task = create_math_task(task_type, a, b, task_id)
        # print(task)
        # Serialize task as JSON
        # print(json.dumps(task))
        r.rpush(queue_name, json.dumps(task))
        print(f"Pushed {task_type} task ({a}, {b}) to queue as ID {task_id}")
        time.sleep(0.2)  # Small delay between tasks

if __name__ == '__main__':
    push_math_tasks()    