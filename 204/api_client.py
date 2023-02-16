import asyncio

from prefect import get_client


async def main():
    async with get_client() as client:
        deployments = await client.read_deployments()
        for idx, deployment in enumerate(deployments):
            print(f"[{idx + 1}] {deployment.name}")


if __name__ == "__main__":
    asyncio.run(main())
