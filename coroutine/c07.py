import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('waiting:',x)
    return 'good'

start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)

loop.run_until_complete(task)
print(task.result())
print('Time:',now()-start)