import multiprocessing
import requests

def downloadFile(url, name):
    response = requests.get(url=url)
    open(f"file{name}.jpg", 'wb').write(response.content)

if __name__ == "__main__":  
    url = 'https://picsum.photos/200/300'
    processes = []

    for i in range(5):
        process = multiprocessing.Process(target=downloadFile, args=[url, i])
        process.start()
        processes.append(process)

    for p in processes:
        p.join()
