import signal, time
def handler(signum, time): 
    print("\nI Got the sigint!!, But I am not stopping!"); 

signal.signal(signal.SIGINT, handler)
i = 0; 
while True: 
    time.sleep(.1); 
    print(i, end="");
    i+=1;
