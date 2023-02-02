from src.utils.get_search_urls import get_search_url
from src.utils.save_name_job import save_job_name
from .get_list_job import get_list_jobs
from src.adapters.requests import Requests
from src.adapters.soup import BeautifulSoup
from src.webhook.message import JobWebHook

class BaseSearch:
    async def search_jobs(stack: str) -> None:
        url = get_search_url(stack=stack)

        res = await Requests(url=url).get()
        content = await BeautifulSoup.parser(html_doc=res.content)
        
        data_list = await get_list_jobs(content=content, stack=stack)

        data = await save_job_name(data_list)
        # print(f'{stack} - {data}')

        for d in data:
            await JobWebHook.send_message(title=d['title'], requirements=d['requirements'], stack=d['stack'], link=d['link'])    
