import asyncio


async def print_values(values):
    for value in values:
        await asyncio.sleep(1)  # yield
        print(value)


async def main():
    await print_values([1, 2])  # runs immediately
    coros = [print_values("abcd"), print_values("6789")]

    # asynchronously gather the tasks
    await asyncio.gather(*coros)


if __name__ == "__main__":
    asyncio.run(main())
