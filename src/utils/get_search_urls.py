from decouple import config

SEARCH_URLS: dict = {
    'django': config('SEARCH_DJANGO_URL'),
    'python': config('SEARCH_PYTHON_URL'),
    'node': config('SEARCH_NODE_URL'),
    '.net': config('SEARCH_NET_URL'),
    'ruby': config('SEARCH_RUBY_URL'),
    'back no label': config('SEARCH_JOBS_BACK_NO_LABEL'),
    'frontend': config('SEARCH_FRONTEND_URL'),
    'flutter': config('SEARCH_FLUTTER_URL'),
    'DevOps': config('SEARCH_DEVOPS_URL'),
    'iOS': config('SEARCH_IOS_URL'),
    'data-science': config('SEARCH_DATA_SCIENCE_URL'),
    'java': config('SEARCH_JAVA_URL'),
    'ui-ux': config('SEARCH_UI_UX_URL'),
    'react': config('SEARCH_REACT_URL')
}


def get_search_url(stack: str) -> str:
    return SEARCH_URLS.get(stack)
