from src.utils.get_search_urls import get_search_url
from .get_list_job import get_list_vancancie
from src.request.requests import Requests
from src.request.soup import BeautifulSoup
from src.webhook.message import JobWebHook

class BaseSearch:
    def search_jobs(stack: str) -> None:
        url = get_search_url(stack=stack)

        res = Requests(url=url).get()
        content = BeautifulSoup.parser(html_doc=res.content)
        
        data_list = get_list_vancancie(content=content, stack=stack)

        for data in data_list:
            JobWebHook.send_message(title=data['title'], requirements=data['requirements'], stack=data['stack'], link=data['link'])    
