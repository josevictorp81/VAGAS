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

