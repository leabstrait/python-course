-   **Create and Run Threads:**

    -   Use `threading.Thread()` to create threads with a target callable object (function) and it's arguments.
    -   Start a thread with `thread.start()`.
    -   Use `thread.join()` to wait for thread completion before continuing.

        ```python
        from threading import Thread

        def square_numbers():
            for i in range(1000):
                result = i * i

        if __name__ == "__main__":
            threads = []
            num_threads = 10

            for i in range(num_threads):
                thread = Thread(target=square_numbers)
                threads.append(thread)

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()
        ```

-   **Share Data Between Threads:**

    -   Threads share the same memory space, allowing access to shared (public) data.
    -   Utilize global variables for shared data among threads.
    -   To see an example: create two threads, each thread should access the current database value, modify it (in this case only increase it by 1), and write the new value back into the database value.

    ```python
    from threading import Thread
    import time

    # Shared global variable

    database_value = 0

    def increase():
        global database_value

        # Read the current value from the shared database
        local_copy = database_value

        # Simulate some time-consuming operation
        time.sleep(0.1)

        # Increment the local copy
        local_copy += 1

        # Write the updated value back to the shared database
        database_value = local_copy

    if __name__ == "__main__":
        print('Start value: ', database_value)

        # Create two threads
        t1 = Thread(target=increase)
        t2 = Thread(target=increase)

        # Start the threads
        t1.start()
        t2.start()

        # Wait for both threads to finish
        t1.join()
        t2.join()

        # Display the final value of the shared database
        print('End value:', database_value)

    ```

    -   In this example, both threads increment the database_value without using any locks. The time.sleep(0.1) is still there to simulate a time-consuming operation. Without a lock, there is a potential for a race condition, and the final value of database_value might not be what is expected due to the interleaved execution of threads. The 2 threads should increment the value by 1, so 2 increment operations are performed. But why is the end value 1 and not 2?

-   **Avoid Race Conditions with Locks:**

    -   A race condition happened in the above example.
    -   Race conditions occur when multiple threads change shared data simultaneously:
        -   Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data.
        -   In our case, the first thread accesses the database_value (0) and stores it in a local copy. It then increments it (local_copy is now 1).
        -   With our time.sleep() function that just simulates some time consuming operations, the programm will swap to the second thread in the meantime.
        -   This will also retrieve the current database_value (still 0) and increment the local_copy to 1.
        -   Now both threads have a local copy with value 1, so both will write the 1 into the global database_value.
        -   This is why the end value is 1 and not 2.
    -   Use locks (also called mutex). It is a synchronization mechanism to limit access to a resource in an environment.
    -   A lock has two states: `locked` and `unlocked`. If a `locked` state is in place, other concurrent threads cannot enter the code section until it's `unlocked`.
    -   Functions: `lock.acquire()` to lock, `lock.release()` to unlock.
    -   Always release the lock after acquiring it.
    -   Recereate above example, this time locking the code section where the database value is retrieved and modified. This will prevent the second thread from modifying the global value at the same time as the first thread(since the first thread has `locked` the code section i.e holds the lock).

        ```python
        from threading import Thread, Lock
        import time

        database_value = 0

        def increase(lock):
            global database_value

            lock.acquire()
            local_copy = database_value
            local_copy += 1
            time.sleep(0.1)
            database_value = local_copy
            lock.release()

        if __name__ == "__main__":
            lock = Lock()

            print('Start value: ', database_value)

            t1 = Thread(target=increase, args=(lock,))
            t2 = Thread(target=increase, args=(lock,))

            t1.start()
            t2.start()

            t1.join()
            t2.join()

            print('End value:', database_value)
        ```

-   **Use Locks as Context Managers:**

    - After lock.acquire() we need to call lock.release() to unblock the code.
    - We can also use a lock as a context manager(recommended), which will safely lock and unlock your code.
    -   Employ locks as context managers using `with lock:` for safer locking and unlocking.

        ```python
        from threading import Thread, Lock
        import time

        database_value = 0

        def increase(lock):
            global database_value

            with lock:
                local_copy = database_value
                local_copy += 1
                time.sleep(0.1)
                database_value = local_copy
        ```

-   **Using Queues in Python:**

    -   Queues can be used for thread-safe and process-safe data exchanges and processing both in a multithreaded or multiprocessing environment.
    -   A queue is a linear FIFO(First In First Out) data structure.

        ```python
        from queue import Queue

        # create queue
        q = Queue()

        # add elements
        q.put(1) # 1
        q.put(2) # 2 1
        q.put(3) # 3 2 1

        # now q looks like this:
        # back --> 3 2 1 --> front

        # get and remove first element
        first = q.get() # --> 1
        print(first)

        # q looks like this:
        # back --> 3 2 --> front
        ```

-   **Multithreading with Queues:**

    -   Threads safely exchange data using queues.
    -   Important methods: `q.get()`, `q.put(item)`, `q.task_done()`, `q.join()`, `q.empty()`.


        - `q.get()` : Remove and return the first item. By default, it blocks until the item is available.
        - `q.put(item)` : Puts element at the end of the queue. By default, it blocks until a free slot is available.
        - `q.task_done()` : Indicate that a formerly enqueued task is complete. For each get() you should call this after you are done with your task for this item.
        - `q.join()` : Blocks until all items in the queue have been gotten and proccessed (task_done() has been called for each item).
        - `q.empty()` : Return True if the queue is empty.

    - Example: The following example processes the numbers in a queue(prints them).

        - **Worker Function**: The `worker` function is designed to be executed by each thread. It continuously retrieves items from the queue and performs some processing on them. In this example, it simply prints the value along with the thread name. The use of a lock (`with lock`) ensures that the print statements from different threads don't interfere with each other.

        - **Main Program Logic**:
        - **Queue and Lock Initialization**: Create a thread-safe queue (`q`) and a lock (`lock`) for synchronization.
        - **Daemon Threads Creation**: Generate 10 daemon threads, each assigned the `worker` function as the target. Daemon threads are set to automatically terminate when the main thread exits.
        - **Queue Filling**: Populate the queue with items (numbers from 0 to 19).
        - **Queue Processing**: Wait until all items in the queue have been processed by the worker threads (`q.join()`). This ensures that the main thread doesn't proceed until all items are handled.


        ```python
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
        if __name__ == '__main__':
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
            print('main done')
        ```


-   **Daemon Threads:**

    -   Daemon threads automatically terminate when the main program ends.
    -   Suitable for background tasks that can be abruptly stopped.
    -   Eliminates the need for explicit signaling mechanisms like `threading.Event`.
    - Have to be careful with daemon threads as they are abruptly stopped and their resources(open files, database transactions) may not be released/completed properly

        ```python
        from threading import Thread
        import time

        def daemon_task():
            while True:
                print("Daemon thread is running.")
                time.sleep(1)v

        if __name__ == "__main__":
            daemon_thread = Thread(target=daemon_task)
            daemon_thread.daemon = True
            daemon_thread.start()

            time.sleep(5)  # Main program continues for 5 seconds
            print("Main program is done.")
        ```
