from decouple import config

STACKS_URLS: dict = {
    'django': config('WEBHOOK_PYTHON_URL'),
    'python': config('WEBHOOK_PYTHON_URL'),
    'node': config('WEBHOOK_NODE_URL'),
    '.net': config('WEBHOOK_NET_URL'),
    'ruby': config('WEBHOOK_RUBY_URL'),
    'Nâo mencionada no título da vaga! - Back': config('WEBHOOK_BACK_NO_STACK_URL'),
    'react native': config('WEBHOOK_REACT_NATIVE_URL'),
    'react': config('WEBHOOK_REACT_URL'),
    'vue': config('WEBHOOK_VUE_URL'),
    'angular': config('WEBHOOK_ANGULAR_URL'),
    'Nâo mencionada no título da vaga! - Front': config('WEBHOOK_FRONT_NO_STACK_URL'),
    'go': config('WEBHOOK_GO_URL'),
    'flutter': config('WEBHOOK_FLUTTER_URL'),
    'DevOps': config('WEBHOOK_DEVOPS_URL'),
    'ios': config('WEBHOOK_IOS_URL'),
    'data-science': config('WEBHOOK_DATA_SCIENCE_URL'),
    'java': config('WEBHOOK_JAVA_URL'),
    'ui-ux': config('WEBHOOK_UI_UX_URL')
}


async def get_webhook_url(stack: str):
    return STACKS_URLS.get(stack)
