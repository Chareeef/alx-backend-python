# Python - Async

Welcome to the exciting world of asynchronous programming in Python! 🚀 In this README, we'll dive into the wonders of `async` and `await` syntax, executing async programs with `asyncio`, running concurrent coroutines, and creating asyncio tasks. Let's embark on this journey together!

## async and await Syntax

Imagine we're writing a Python script, and we want to perform multiple tasks simultaneously without blocking the execution flow. That's where `async` and `await` come into play. They allow us to define asynchronous functions and await the results of asynchronous operations respectively.

Here's a quick example to illustrate the syntax:

```python
import asyncio

async def my_async_function():
    print("Async function is doing its magic!")
    await asyncio.sleep(1)
    print("Async function has completed!")

async def main():
    await my_async_function()

asyncio.run(main())
```

In this snippet:
- We define an asynchronous function `my_async_function()` using the `async` keyword.
- Inside the function, we use `await` to pause the execution until an asynchronous operation completes. In this case, `asyncio.sleep(1)` simulates a non-blocking delay of 1 second.
- We create a `main()` coroutine to run our asynchronous function.
- Finally, we use `asyncio.run()` to execute the `main()` coroutine.

## Executing an Async Program with asyncio

To execute an async program with asyncio, we need to follow these steps:
1. Define our asynchronous functions using the `async` keyword.
2. Use `await` to call other asynchronous functions or perform non-blocking operations.
3. Create a `main()` coroutine to orchestrate the execution flow.
4. Use `asyncio.run(main())` to run the `main()` coroutine.

It's that simple! With asyncio, we can unleash the power of asynchronous programming in Python.

## Running Concurrent Coroutines

Concurrency is all about executing multiple tasks seemingly simultaneously. With asyncio, we can achieve concurrency effortlessly using coroutines. Coroutines are functions that can pause and resume execution, making them perfect for asynchronous operations.

Here's how we can run concurrent coroutines:

```python
import asyncio

async def task1():
    print("Task 1 is doing its job!")
    await asyncio.sleep(2)
    print("Task 1 is done!")

async def task2():
    print("Task 2 is doing its job!")
    await asyncio.sleep(1)
    print("Task 2 is done!")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

In this example, `asyncio.gather()` allows us to run multiple coroutines concurrently. Both `task1()` and `task2()` execute simultaneously, speeding up the overall execution time.

## Creating asyncio Tasks

Asyncio tasks provide a convenient way to manage and coordinate asynchronous operations. We can create tasks for individual coroutines and monitor their progress or wait for their completion.

Let's see how to create asyncio tasks:

```python
import asyncio

async def my_async_function():
    print("Async function is doing its magic!")
    await asyncio.sleep(1)
    print("Async function has completed!")

async def main():
    task = asyncio.create_task(my_async_function())
    await task

asyncio.run(main())
```

By using `asyncio.create_task()`, we create a task for the `my_async_function()` coroutine. This allows us to run the coroutine independently and await its completion within the `main()` coroutine.

In conclusion, asynchronous programming in Python opens up a world of possibilities for building efficient and responsive applications. With asyncio, we can handle multiple tasks concurrently, making our programs faster and more scalable. Happy coding! 🎉
