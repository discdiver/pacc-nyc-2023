import time

from prefect import flow, task


@task
def print_values(values):
    for value in values:
        time.sleep(1)
        print(value)


@flow
def main():
    print_values([1, 2])  # runs immediately
    coros = [print_values.submit("abcd"), print_values.submit("6789")]


if __name__ == "__main__":
    main()
