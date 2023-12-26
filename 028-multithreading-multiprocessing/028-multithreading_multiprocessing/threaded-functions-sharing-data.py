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
    print("Start value: ", database_value)

    # Create two threads
    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

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
