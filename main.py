from src.search.search import BaseSearch

class Main:
    def run():
        # BaseSearch.search_jobs(stack='django')
        # BaseSearch.search_jobs(stack='node')
        # BaseSearch.search_jobs(stack='ruby')
        BaseSearch.search_jobs(stack='back no label')
        print(True)

if __name__ == '__main__':
    Main.run()