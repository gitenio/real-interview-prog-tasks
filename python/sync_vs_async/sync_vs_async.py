import asyncio
import time
import sys

# ----------------------------------------------------------------------------------
# BASICS
# ----------------------------------------------------------------------------------

# --- SYNCHRONOUS APPROACH ---
def fetch_data_sync(task_id):
    print(f"Sync: Starting task {task_id}")
    time.sleep(2)  # Blocks the entire program for 2 seconds
    print(f"Sync: Finished task {task_id}")

def run_sync():
    start = time.time()
    for i in range(1, 4):
        fetch_data_sync(i)
    print(f"➡️ Total Sync Time: {time.time() - start:.2f} seconds\n")


# --- ASYNCHRONOUS APPROACH ---
async def fetch_data_async(task_id):
    print(f"Async: Starting task {task_id}")
    await asyncio.sleep(2)  # Pauses this task, letting other tasks run
    print(f"Async: Finished task {task_id}")

    
async def run_async():
    start = time.time()
    # Schedule and run all 3 tasks concurrently
    await asyncio.gather(
        fetch_data_async(1),
        fetch_data_async(2),
        fetch_data_async(3)
    )
    print(f"➡️ Total Async Time: {time.time() - start:.2f} seconds")
    return 10

asyncio.run(run_async())

# ----------------------------------------------------------------------------------
# Introduced in Python 3.11, asyncio.TaskGroup is the recommended way to run multiple
#   tasks concurrently. It acts as an asynchronous context manager that automatically
#   tracks, executes, and safely cleans up a group of tasks
# ----------------------------------------------------------------------------------
async def fetch_data(id: int, delay: int):
    print("[Task {id}] Starting fetch...")
    await asyncio.sleep(delay)
    print("[Task {id}] Data fetched!")
    return {"id": id, "data": "success"}

async def main():
    start_time = time.time()

    # TaskGroup manages the lifetime and errors of all nested tasks
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(1, 2))
        task2 = tg.create_task(fetch_data(2, 3))
        task3 = tg.create_task(fetch_data(3, 1))

    # The block waits automatically for all tasks to finish before exiting
    print(f"Results gathered: {task1.result()}, {task2.result()}, {task3.result()}")
    print(f"Total time taken: {time.time() - start_time:.2f} seconds")


# ----------------------------------------------------------------------------------
# If you are working on older versions of Python (pre-3.11) or prefer a quick way to
#       unpack a list of dynamic tasks and instantly get their results back as a list,
#       use asyncio.gather()
# ----------------------------------------------------------------------------------    
async def square(number: int):
    await asyncio.sleep(0.5)
    return number ** 2

async def main2():
    numbers = [1, 2, 3, 4, 5]
    
    # Map numbers to coroutines
    tasks = [square(num) for num in numbers]
    
    # Run them concurrently and unpack the list with '*'
    results = await asyncio.gather(*tasks)
    
    print(f"Squared numbers: {results}")

asyncio.run(main2())

# ----------------------------------------------------------------------------------
# asyncio runs on a single thread. If you try to run a slow, CPU-bound formula
#    or a traditional synchronous function (like time.sleep() or requests.get()),
#    it will freeze the whole event loop. You can use asyncio.to_thread() to safely
#    offload that blocking function to a separate thread.
# ----------------------------------------------------------------------------------
def standard_blocking_io():
    # Simulate a legacy library that blocks the thread
    time.sleep(2)
    return "Blocking task complete"

async def async_ui_announcement():
    for i in range(4):
        print("Keep running UI animation updates...")
        await asyncio.sleep(0.5)

async def main3():
    # Run the blocking function in a background thread while keeping the event loop moving
    blocking_task = asyncio.to_thread(standard_blocking_io)
    
    await asyncio.gather(blocking_task, async_ui_announcement())
    print(blocking_task.result())

asyncio.run(main3())

# ----------------------------------------------------------------------------------
# Managing TimeoutsNetwork operations can hang indefinitely. You can wrap asynchronous
#   blocks in a timeout context manager using asyncio.timeout
# ----------------------------------------------------------------------------------


async def external_api_call():
    # Simulate an API that is hanging or heavily delayed
    await asyncio.sleep(5)
    return "Data"

async def main4():
    try:
        # Enforce a strict 2-second limit on the operation
        async with asyncio.timeout(2):
            result = await external_api_call()
            print(result)
    except TimeoutError:
        print("The external API took too long and timed out!")

asyncio.run(main4())

# ----------------------------------------------------------------------------------
# Check Python's asyncio: A Hands-on Walkthrough for more on asyncio package
# https://realpython.com/async-io-python/
# ----------------------------------------------------------------------------------
if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())
    obj = run_async()
    obj()
    print(obj)
    print(asyncio.run(obj))

    # run set of tasks using asyncio.TaskGroup
    asyncio.run(main())
    sys.exit()
