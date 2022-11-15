from pathlib import Path

path = Path()

def exists_job_name(name: str) -> bool:
    with open(f'{path}/jobs.txt', 'r') as file:
        names = file.read()
        return True if name in names else False


def save_job_name(data: list) -> list:
    new_data = []
    for d in data:
        exists = exists_job_name(d['title'])
        if not exists:
            with open(f'{path}/jobs.txt', 'a+') as file:
                file.write(f'{d["title"]}\n')
            new_data.append(d)
    
    return new_data
