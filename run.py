import threading
import requests
import random
import requests

# URL to make the REST call to
url = 'https://{your-domain}/embed'

# Function to make a REST call and keep the connection open
def make_rest_call():
    # Set the maximum size of the connection pool
    max_pool_size = 100

    # Create a Session object with the desired connection pool size
    session = requests.Session()
    session.mount('https://', requests.adapters.HTTPAdapter(pool_connections=max_pool_size, pool_maxsize=max_pool_size))

    # Now you can make requests using the session object
    response = session.post(url, json={"inputs": f"query: Hello World! {random.randint(1, 100000)}"}, timeout=60)
    print(f"Thread {threading.current_thread().name} received response code: {response.status_code}")
    # The connection will remain open as we do not close it.

# List to keep track of threads
threads = []

# Create and start 20 threads
for c in range(10):
    for i in range(2):
        thread = threading.Thread(target=make_rest_call, name=f'Thread-{i+1}')
        threads.append(thread)
        thread.start()

    # Optionally, join the threads to ensure they all complete (if you want to wait for them)
    for thread in threads:
        thread.join()

print("All threads have started and made their REST calls.")
