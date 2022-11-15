from pathlib import Path

path = Path()

def main():
    with open(f'{path}/jobs.txt', 'r+') as file:
        file.truncate(0)


if __name__ == '__main__':
    main()