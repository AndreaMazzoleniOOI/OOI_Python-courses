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
        self.print_stuff(self.name, self.delay, self.count)
        print(f'{self.name} exit\n')

    @staticmethod
    def print_stuff(name, delay, count):
        while count:
            time.sleep(delay)
            print(f'{name}: {time.ctime(time.time())}, {count}')
            count -= 1


if __name__ == '__main__':
    thread1 = myThread(1, 'Thread1', 10, 1)
    thread2 = myThread(2, 'Thread2', 5, 1.5)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('Main thread exit')