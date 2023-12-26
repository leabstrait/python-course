from threading import Thread, Lock, current_thread
from queue import Queue


# Worker function to be executed by each thread
def worker(q, lock):
    while True:
        value = q.get()  # Blocks until an item is available in the queue

        # Do some processing with the value (printing in this case)
        with lock:
            # Use a lock to prevent multiple threads from printing simultaneously
            print(f"in {current_thread().name} got {value}")

        # Notify the queue that the processing on this item is complete
        q.task_done()


# Main program
if __name__ == "__main__":
    # Create a thread-safe queue and a lock for printing
    q = Queue()
    lock = Lock()

    # Create 10 daemon threads, each invoking the worker function
    num_threads = 10
    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # Threads die when the main thread exits
        t.start()

    # Fill the queue with items (numbers from 0 to 19)
    for x in range(20):
        q.put(x)

    # Wait until all items in the queue have been processed by the worker threads
    q.join()

    # Main thread continues only after all items are processed
    print("main done")
