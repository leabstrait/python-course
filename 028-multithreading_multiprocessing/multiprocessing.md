- **Creating and Running Processes**

  You create a process with `multiprocessing.Process()`. It takes two important arguments:

  - `target`: a callable object (function) for this process to be invoked when the process starts.
  - `args`: the (function) arguments for the target function. This must be a tuple.

  Start a process with `process.start()`. Call `process.join()` to tell the program that it should wait for this process to complete before it continues with the rest of the code.

  ```python
  from multiprocessing import Process
  import os

  def square_numbers():
      for i in range(1000):
          result = i * i

  if __name__ == "__main__":
      processes = []
      num_processes = os.cpu_count()

      # Create processes and assign a function for each process
      for i in range(num_processes):
          process = Process(target=square_numbers)
          processes.append(process)

      # Start all processes
      for process in processes:
          process.start()

      # Wait for all processes to finish
      # Block the main program until these processes are finished
      for process in processes:
          process.join()
  ```

- **Sharing Data Between Processes**

  Since processes don't live in the same memory space, they need special shared memory objects to share data. Data can be stored in a shared memory variable using `Value` or `Array`.
    - Value(type, value): Create a ctypes object of type type. Access the value with .target.
    - Array(type, value): Create a ctypes array with elements of type type. Access the values with [].

  ```python
  from multiprocessing import Process, Value, Array
  import time

  def add_100(number):
      for _ in range(100):
          time.sleep(0.01)
          number.value += 1

  def add_100_array(numbers):
      for _ in range(100):
          time.sleep(0.01)
          for i in range(len(numbers)):
              numbers[i] += 1

  if __name__ == "__main__":
      shared_number = Value('i', 0)
      print('Shared Value at beginning:', shared_number.value)

      shared_array = Array('d', [0.0, 100.0, 200.0])
      print('Shared Array at beginning:', shared_array[:])

      process1 = Process(target=add_100, args=(shared_number,))
      process2 = Process(target=add_100, args=(shared_number,))

      process3 = Process(target=add_100_array, args=(shared_array,))
      process4 = Process(target=add_100_array, args=(shared_array,))

      process1.start()
      process2.start()
      process3.start()
      process4.start()

      process1.join()
      process2.join()
      process3.join()
      process4.join()

      print('Shared Value at end:', shared_number.value)
      print('Shared Array at end:', shared_array[:])
  ```

  In this example, we can notice that the results aren't as expected, we expect the Shared Value to be 200 at the end as two processes work on it adding 100 each, but it's not 200.
  Also same with the Shared Array, we need it to be [200, 300, 400] but it's not.

- **Avoiding Race Conditions with Locks**

  - A race condition occurs when two or more processes or threads can access shared data and try to change it at the same time.
    - In the example the two processes have to read the shared value, increase it by 1, and write it back into the shared variable.
    - If this happens at the same time, the two processes read the same value, increase it and write it back.
    - Thus, both processes write the same increased value back into the shared object, and the value was not increased by 2.
  - A `Lock` can prevent this by locking the state during critical code sections.

  ```python
  from multiprocessing import Lock, Process, Value, Array
  import time

  def add_100(number, lock):
      for _ in range(100):
          time.sleep(0.01)
          lock.acquire()
          number.value += 1
          lock.release()

  def add_100_array(numbers, lock):
      for _ in range(100):
          time.sleep(0.01)
          for i in range(len(numbers)):
              lock.acquire()
              numbers[i] += 1
              lock.release()

  if __name__ == "__main__":
      lock = Lock()

      shared_number = Value('i', 0)
      print('Shared Value at beginning:', shared_number.value)

      shared_array = Array('d', [0.0, 100.0, 200.0])
      print('Shared Array at beginning:', shared_array[:])

      process1 = Process(target=add_100, args=(shared_number, lock))
      process2 = Process(target=add_100, args=(shared_number, lock))

      process3 = Process(target=add_100_array, args=(shared_array, lock))
      process4 = Process(target=add_100_array, args=(shared_array, lock))

      process1.start()
      process2.start()
      process3.start()
      process4.start()

      process1.join()
      process2.join()
      process3.join()
      process4.join()

      print('Shared Value at end:', shared_number.value)
      print('Shared Array at end:', shared_array[:])
  ```

- **Using Locks as Context Managers**

  Locks can also be used as context managers, ensuring they are properly released.

  ```python
  def add_100(number, lock):
      for _ in range(100):
          time.sleep(0.01)
          with lock:
              number.value += 1
  ```

- **Using Queues in Python**

  Data can be shared between processes with a `Queue`, which is thread and process-safe. It follows the First In First Out (FIFO) principle.

  ```python
  from multiprocessing import Process, Queue

  def square(numbers, queue):
      for i in numbers:
          queue.put(i * i)

  def make_negative(numbers, queue):
      for i in numbers:
          queue.put(i * -1)

  if __name__ == "__main__":
      numbers = range(1, 6)
      q = Queue()

      p1 = Process(target=square, args=(numbers, q))
      p2 = Process(target=make_negative, args=(numbers, q))

      p1.start()
      p2.start()

      p1.join()
      p2.join()

      # ordering may not be sequential
      while not q.empty():
          print(q.get())
  ```
- **Process Pools**

  - A process pool object in Python controls a pool of worker processes for job submission, supporting asynchronous results with timeouts, callbacks, and a parallel map implementation.  - It can automatically manage available processors, splitting data into smaller chunks processed in parallel by different processes. For detailed information, see [official documentation](https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.pool).

  Important methods include:

  - `map(func, iterable[, chunksize])`: Chops the iterable into chunks and submits them to the process pool as separate tasks. The chunk size can be specified with the `chunksize` parameter. It blocks until the result is ready.

  - `close()`: Prevents further tasks from being submitted to the pool. Once all tasks are completed, worker processes exit.

  - `join()`: Waits for the worker processes to exit. You must call `close()` or `terminate()` before using `join()`.

  - `apply(func, args)`: Calls the function `func` with arguments `args`. It blocks until the result is ready and is executed in only one of the workers of the pool.

  Note: There are also asynchronous variants `map_async()` and `apply_async()` that do not block. They can execute callbacks when results are ready.

  ```python
  from multiprocessing import Pool

  def cube(number):
      return number * number * number

  if __name__ == "__main__":
      numbers = range(10)

      p = Pool()

      # By default, this allocates the maximum number of available processors
      # for this task --> os.cpu_count()
      result = p.map(cube, numbers)

      # or
      # result = [p.apply(cube, args=(i,)) for i in numbers]

      p.close()
      p.join()

      print(result)
  ```