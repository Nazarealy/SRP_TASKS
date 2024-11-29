import requests
from collections import Counter
from time import time
import threading
from queue import Queue

# Завантаження тексту
URL = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

def download_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Функція для підрахунку частоти слів
def word_count(text):
    words = text.split()
    cleaned_words = [word.strip(",.!?\"'").lower() for word in words]
    return Counter(cleaned_words)

# Синхронний підхід
def synchronous_approach(text):
    start_time = time()
    word_counts = word_count(text)
    top_100 = word_counts.most_common(100)
    end_time = time()
    return top_100, end_time - start_time

# Паралельний підхід із перевіркою Race Condition
def parallel_approach(text, num_threads):
    def worker(q, results, lock):
        while not q.empty():
            chunk = q.get()
            local_count = word_count(chunk)
            # Race Condition може виникнути тут, якщо не використовувати Lock
            with lock:
                results.update(local_count)
            q.task_done()

    start_time = time()
    words = text.split()
    chunk_size = len(words) // num_threads
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    q = Queue()
    for chunk in chunks:
        q.put(chunk)

    results = Counter()
    lock = threading.Lock()
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(q, results, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    top_100 = results.most_common(100)
    end_time = time()
    return top_100, end_time - start_time

# Функція для репродюсації Race Condition
def demonstrate_race_condition():
    counter = 0
    def increment():
        nonlocal counter
        for _ in range(100000):
            counter += 1  # Без блокування тут можливий некоректний результат

    threads = [threading.Thread(target=increment) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return counter

# Головна функція
def main():
    text = download_text(URL)

    print("Running synchronous approach...")
    top_100_sync, sync_time = synchronous_approach(text)
    print(f"Synchronous time: {sync_time:.2f} seconds")

    print("\nRunning parallel approach...")
    num_threads = 4  # Ви можете змінювати кількість потоків
    top_100_parallel, parallel_time = parallel_approach(text, num_threads)
    print(f"Parallel time with {num_threads} threads: {parallel_time:.2f} seconds")

    # Вивід слів у рядок для зручності
    print("\nTop 100 words (synchronous):")
    print(", ".join(f"{word}: {count}" for word, count in top_100_sync))

    print("\nTop 100 words (parallel):")
    print(", ".join(f"{word}: {count}" for word, count in top_100_parallel))

    print("\nDemonstrating race condition...")
    result = demonstrate_race_condition()
    print(f"Race condition test result: {result} (expected: 200000)")

if __name__ == "__main__":
    main()
