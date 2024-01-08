from src.search.search import BaseSearch
import asyncio
import time

from src.utils.save_name_job import register_search_hour


async def main() -> None:
    print(f'start: {time.strftime("%X")}')
    await register_search_hour()

    await asyncio.gather(
        BaseSearch.search_jobs(stack='django'),
        BaseSearch.search_jobs(stack='node'),
        BaseSearch.search_jobs(stack='ruby'),
        BaseSearch.search_jobs(stack='.net'),
        BaseSearch.search_jobs(stack='back no label'),
        BaseSearch.search_jobs(stack='frontend'),
        BaseSearch.search_jobs(stack='flutter'),
        BaseSearch.search_jobs(stack='DevOps'),
        BaseSearch.search_jobs(stack='iOS'),
        BaseSearch.search_jobs(stack='data-science'),
        BaseSearch.search_jobs(stack='java'),
        BaseSearch.search_jobs(stack='ui-ux'),
        BaseSearch.search_jobs(stack='react'),
    )
    print(f'end: {time.strftime("%X")}')


if __name__ == '__main__':
    asyncio.run(main())
