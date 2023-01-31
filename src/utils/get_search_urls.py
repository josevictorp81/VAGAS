from decouple import config

def get_search_url(stack: str) -> str:
    if stack == 'django':
        return config('SEARCH_DJANGO_URL')
    if stack == 'node':
        return config('SEARCH_NODE_URL')
    if stack == '.net':
        return config('SEARCH_NET_URL')
    if stack == 'ruby':
        return config('SEARCH_RUBY_URL')
    if stack == 'back no label':
        return config('SEARCH_JOBS_BACK_NO_LABEL')
    if stack == 'frontend':
        return config('SEARCH_FRONTEND_URL')
    if stack == 'flutter':
        return config('SEARCH_FLUTTER_URL')
    if stack == 'DevOps':
        return config('SEARCH_DEVOPS_URL')
    if stack == 'iOS':
        return config('SEARCH_IOS_URL')
    if stack == 'data-science':
        return config('SEARCH_DATA_SCIENCE_URL')
    if stack == 'java':
        return config('SEARCH_JAVA_URL')
    if stack == 'ui-ux':
        return config('SEARCH_UI_UX_URL')
