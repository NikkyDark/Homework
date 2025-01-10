import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


if __name__ == "__main__":
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # Линейное считывание
    start_time = time.time()
    for file_name in file_names:
        data = read_info(file_name)
        print(f"Считано {len(data)} строк из {file_name}")
    linear_time = time.time() - start_time
    print(f"Время линейного считывания: {linear_time:.2f} секунд")

    # Многопроцессное считывание
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, file_names)

    for i, data in enumerate(results):
        print(f"Считано {len(data)} строк из {file_names[i]}")

    parallel_time = time.time() - start_time
    print(f"Время многопроцессного считывания: {parallel_time:.2f} секунд")
