from pathlib import Path
import time

path = Path()

async def exists_job_name(name: str) -> bool:
    with open(f'{path}/jobs.txt', 'r') as file:
        names = file.read()
        return True if name in names else False


async def save_job_name(data: list) -> list:
    new_data = []
    for d in data:
        exists = await exists_job_name(d['title'])
        if not exists:
            with open(f'{path}/jobs.txt', 'a+') as file:
                file.write(f'{time.strftime("%X")} - {d["title"]}\n')
            new_data.append(d)
    
    return new_data
