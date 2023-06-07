import threading
import time


class myThread(threading.Thread):
    def __init__(self, thread_id, name, count, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.count = count
        self.delay= delay

    def run(self):
        print(f'{self.name} start\n')
        threadLock.acquire()
        self.print_stuff(self.name, self.delay, self.count)
        threadLock.release() # Allows to compleate the thread we are running before starting a new one

        print(f'{self.name} exit\n')

    @staticmethod
    def print_stuff(name, delay, count):
        while count:
            time.sleep(delay)
            print(f'{name}: {time.ctime(time.time())}, {count}')
            count -= 1


class myThread2(threading.Thread):
    def __init__(self, thread_id, name, count, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.count = count
        self.delay= delay

    def run(self):
        print(f'{self.name} start\n')
        threadLock.acquire()    # Check if some thread is locked
        threadLock.release()    # If no locked thread, release and execute
        self.print_stuff(self.name, self.delay, self.count)


        print(f'{self.name} exit\n')

    @staticmethod
    def print_stuff(name, delay, count):
        while count:
            time.sleep(delay)
            print(f'{name}: {time.ctime(time.time())}, {count}')
            count -= 1


"""
We want to create a system that accept a payment (takes 10 s), send an email for confirmation (5 s), and send us to 
a goodbye page (3 s to load). This means that the user need to wait 18s before having a goodbye page.
We need to complete the payment before sending the email BUT we can load the goodbye page while sending the email.
So we use Thread1, which locks the the thread until it is completed, then Thread2 objects can start in different threads
to speed up the last two processes.
"""

start = time.time()
threadLock = threading.Lock()
thread1 = myThread(1, 'Payment', 10, 1)
thread2 = myThread2(2, 'Send Email', 5, 1)
thread3 = myThread2(3, 'Goodbye', 3, 1)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

print(f'Main thread exit in {time.time()-start}s')