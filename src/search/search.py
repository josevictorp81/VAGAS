from ..utils.get_search_urls import get_search_url
from ..utils.get_vacancies import get_list_vancancie
from ..request.requests import Requests
from ..request.soup import BeautifulSoup
from ..webhook.message import JobWebHook

class BaseSearch:
    def search_jobs(stack: str):
        url = get_search_url(stack=stack)

        res = Requests(url=url).get()
        content = BeautifulSoup.parser(html_doc=res.content)
        
        data_list = get_list_vancancie(content=content, stack=stack)

        for data in data_list:
            JobWebHook.send_message(title=data['title'], requirements=data['requirements'], stack=data['stack'], link=data['link'])
            # print(data['title'], data['stack'])
        
        return True
                

