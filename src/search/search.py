from src.utils.get_search_urls import get_search_url
from src.utils.save_name_job import save_job_name
from .get_list_job import get_list_jobs
from src.adapters.requests import Requests
from src.adapters.soup import BeautifulSoup
from src.webhook.message import JobWebHook

class BaseSearch:
    def search_jobs(stack: str) -> None:
        url = get_search_url(stack=stack)

        res = Requests(url=url).get()
        content = BeautifulSoup.parser(html_doc=res.content)
        
        data_list = get_list_jobs(content=content, stack=stack)

        data = save_job_name(data_list)

        for d in data:
            JobWebHook.send_message(title=d['title'], requirements=d['requirements'], stack=d['stack'], link=d['link'])    
