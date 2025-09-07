from concurrent.futures import ThreadPoolExecutor
import threading
import time

def first_loop(seconds):
    time.sleep(seconds)
    print(f"first_loop executes in {seconds} seconds")
    return "Alok"
# def second_loop(seconds):
#     time.sleep(2)
#     print(f"second_loop executes in {seconds} seconds")
#     return "Bhuyan"
    
# start_time = time.perf_counter()
        
# first_thread = threading.Thread(target=first_loop)
# second_thread = threading.Thread(target=second_loop)

# first_thread.start()
# second_thread.start()

# first_thread.join()
# second_thread.join()
# end_time = time.perf_counter()

def pooling_thread():
    with ThreadPoolExecutor(max_workers=16) as executor:
        list = [3,2,1]
        results = executor.map(first_loop,list)
        for result in results:
            print(result)
        


pooling_thread()