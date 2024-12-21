import logging
from redis import Redis
from rq import Queue
from sentry_sdk import capture_exception

class ProductionWorker:
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.redis = Redis()
        self.queue = Queue(connection=self.redis)
        self.logger = logging.getLogger(f"worker.{worker_id}")
        
    def process_task(self, task):
        try:
            with self.metrics.timer('task_processing_time'):
                result = self.execute_task(task)
                
            self.logger.info(f"Task {task.id} completed successfully")
            return result
            
        except Exception as e:
            self.logger.error(f"Task {task.id} failed: {str(e)}")
            capture_exception(e)
            self.queue.enqueue(task, retry=True)
            
    def health_check(self):
        return {
            'worker_id': self.worker_id,
            'queue_size': len(self.queue),
            'status': 'healthy',
            'last_heartbeat': self.last_heartbeat
        }