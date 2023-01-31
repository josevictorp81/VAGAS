import re

async def verify_stack_back(title: str) -> str:
    if re.search('.net', title.lower()) or re.search('C#', title.upper()) or re.search('dotnet', title.lower()):
        return '.net'
    if re.search('python', title.lower()) or re.search('fastapi', title.lower()) or re.search('django', title.lower()):
        return 'python'
    if re.search('node', title.lower()):
        return 'node'
    if re.search('ruby', title.lower()):
        return 'ruby'
    if re.search('go', title.lower()) or re.search('golang', title.lower()):
        return 'go'
    if re.search('ios', title.lower()):
        return 'ios'
    else:
        return 'Nâo mencionada no título da vaga! - Back'


async def verify_stack_front(title: str) -> str:
    if re.search('react-native', title.lower()) or re.search('react native', title.lower()):
        return 'react native'
    if re.search('react', title.lower()):
        return 'react'
    if re.search('vue', title.lower()):
        return 'vue'
    if re.search('angular', title.lower()):
        return 'angular'
    else:
        return 'Nâo mencionada no título da vaga! - Front'
