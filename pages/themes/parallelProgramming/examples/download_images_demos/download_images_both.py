import multiprocessing
import os
import time
import requests


def download_image(url, index, folder):
    """Download an image and save it to the specified folder."""
    response = requests.get(url, stream=True)
    file_path = os.path.join(folder, f"image_{index}.jpg")

    with open(file_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print(f"Downloaded: {file_path}")


def download_without_threading(urls, folder):
    """Sequential download without multiprocessing."""
    start_time = time.time()
    for i, url in enumerate(urls):
        download_image(url, i, folder)
    return time.time() - start_time


def download_with_threading(urls, folder):
    """Download using multiprocessing."""
    start_time = time.time()
    processes = []

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=download_image, args=(url, i, folder))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return time.time() - start_time


if __name__ == "__main__":
    # List of image URLs to download
    urls = [
        "https://unsplash.com/photos/CTflmHHVrBM/download?force=true",
        "https://unsplash.com/photos/pWV8HjvHzk8/download?force=true",
        "https://unsplash.com/photos/1jn_3WBp60I/download?force=true",
        "https://unsplash.com/photos/8E5HawfqCMM/download?force=true",
        "https://unsplash.com/photos/yTOkMc2q01o/download?force=true",
    ]

    # Directories to save images
    sequential_path = os.path.join(os.getcwd(), "downloaded_images_sequential")
    multiprocessing_path = os.path.join(
        os.getcwd(), "downloaded_images_multiprocessing"
    )
    os.makedirs(sequential_path, exist_ok=True)
    os.makedirs(multiprocessing_path, exist_ok=True)

    print(f"Running tests on {len(urls)} images...")

    print("\nRunning without multiprocessing...")
    single_time = download_without_threading(urls, sequential_path)

    print("\nRunning with multiprocessing...")
    multi_time = download_with_threading(urls, multiprocessing_path)

    # Compare the results
    print("\nResults:")
    print(f"Without multiprocessing: {single_time:.2f} seconds")
    print(f"With multiprocessing: {multi_time:.2f} seconds")
    print(f"Speedup: {single_time / multi_time:.2f}x")
