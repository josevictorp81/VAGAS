from bs4 import BeautifulSoup as bsp


class BeautifulSoup:
    async def parser(html_doc):
        return bsp(html_doc, 'html.parser')
