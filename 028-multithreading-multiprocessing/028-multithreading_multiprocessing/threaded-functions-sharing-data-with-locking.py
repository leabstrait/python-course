from threading import Thread, Lock
import time

# Shared global variable

database_value = 0


def increase(lock):
    global database_value

    # Acquire the lock before accessing the shared database
    lock.acquire()

    # Read the current value from the shared database
    local_copy = database_value

    # Simulate some time-consuming operation
    time.sleep(0.1)

    # Increment the local copy
    local_copy += 1

    # Write the updated value back to the shared database
    database_value = local_copy

    # Release the lock after accessing the shared database
    lock.release()


if __name__ == "__main__":
    # Create a lock object
    lock = Lock()
    # Display the initial value of the shared database
    print("Start value: ", database_value)

    # Create two threads
    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))

    start_time = time.time()

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    end_time = time.time()

    print(f"Time taken: {end_time - start_time}")

    # Display the final value of the shared database
    print("End value:", database_value)
