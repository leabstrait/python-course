from multiprocessing import Process, Value, Array, Lock
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

    shared_number = Value("i", 0)
    print("Shared Value at beginning:", shared_number.value)

    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("Shared Array at beginning:", shared_array[:])

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

    print("Shared Value at end:", shared_number.value)
    print("Shared Array at end:", shared_array[:])
