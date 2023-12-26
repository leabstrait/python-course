import os
import psutil
from multiprocessing import Pool


def get_cpu_affinity(process_id):
    try:
        process = psutil.Process(process_id)
        affinity = process.cpu_affinity()
        return affinity
    except psutil.NoSuchProcess as e:
        print(f"Process with ID {process_id} not found.")
    except psutil.AccessDenied as e:
        print(f"Access to process with ID {process_id} denied.")
    except Exception as e:
        print(f"Error: {e}")


def get_cpu_info(cpu_list):
    cpu_info = []
    for cpu in cpu_list:
        cpu_info.append(psutil.cpu_percent(percpu=True)[cpu])
    return cpu_info


def cube(number):
    process_id = os.getpid()
    affinity = get_cpu_affinity(process_id)
    cpu_info = get_cpu_info(affinity)

    affinity_padded = " ".join(map(lambda n: str(n).rjust(3), affinity))
    cpu_info_padded = " ".join(map(lambda n: str(int(n)).rjust(3), cpu_info))
    print(
        process_id,
        "is the process id running on",
        "\n",
        affinity_padded,
        "\n",
        cpu_info_padded,
    )

    return number * number * number


if __name__ == "__main__":
    numbers = range(10)

    p = Pool()
    print("Total CPU cores:", os.cpu_count())

    # By default, this allocates the maximum number of available processors
    # for this task --> os.cpu_count()
    result = p.map(cube, numbers)

    # or
    # result = [p.apply(cube, args=(i,)) for i in numbers]

    p.close()
    p.join()

    print(result)
