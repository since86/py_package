import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('waiting:',x)
    return 'good'

start = now()

coroutine = do_some_work(2)

print(coroutine)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
duration = now() - start
print('Time:',duration)