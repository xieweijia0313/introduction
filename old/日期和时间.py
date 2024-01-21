

import time
#当前时间2023_07_10 21:32:45
print(time.strftime('%Y_%m_%d %H:%M:%S',time.localtime()))


import timeit
#计时
start = timeit.default_timer()
time.sleep(0.1)
end = timeit.default_timer()
#计时=end-start
print(f'Running time: {end - start}s Seconds')