import time
start = time.perf_counter()

def do_something():
    print('Sleeping for 1 sec...')
    time.sleep(1)
    print('Done Sleeping.')

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {finish-start} seconds.')