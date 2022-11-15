from datetime import datetime
from src.utils.convert_month import convert_month_str_to_int
from src.utils.verify_stack import verify_stack_back, verify_stack_front

def get_list_jobs(content, stack: str):
    vacancies = content.find_all('div', attrs={'class': 'flex-auto min-width-0 p-2 pr-3 pr-md-2'})
    vacancies.reverse()
    data = []
    stack_label = stack
    for vacancie in vacancies:
        posted = vacancie.find('relative-time', attrs={'class': 'no-wrap'})
        date_posted = posted.text.replace(',', '').split(' ')
        
        month = convert_month_str_to_int(date_posted[0])

        if month == datetime.now().month and int(date_posted[1]) == datetime.now().day:
            title = vacancie.find('a', attrs={'class': 'Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title'})
            requirements = vacancie.find('span', attrs={'class': 'lh-default d-block d-md-inline'})
            requirements = requirements.text.replace('\n\n\n', '').strip() if requirements else 'Sem subtítulo'
            link = 'https://github.com' + title['href']
            if stack == 'back no label':
                stack_label = verify_stack_back(title=title.text)
            if stack == 'frontend':
                stack_label = verify_stack_front(title=title.text)
            data.append({'title': title.text, 'requirements': requirements, 'link': link, 'stack': stack_label})
        
    return data