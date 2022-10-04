from decouple import config

def get_webhook_url(stack: str):
    if stack == 'django' or stack == 'python':
        return config('WEBHOOK_PYTHON_URL')
    if stack == 'node':
        return config('WEBHOOK_NODE_URL')
    if stack == '.net':
        return config('WEBHOOK_NET_URL')
    if stack == 'ruby':
        return config('WEBHOOK_RUBY_URL')
    if stack == 'Nâo mencionada no título da vaga! - Back':
        return config('WEBHOOK_BACK_NO_STACK_URL')
    if stack == 'react native':
        return config('WEBHOOK_REACT_NATIVE_URL')
    if stack == 'react':
        return config('WEBHOOK_REACT_URL')
    if stack == 'vue':
        return config('WEBHOOK_VUE_URL')
    if stack == 'angular':
        return config('WEBHOOK_ANGULAR_URL')
    if stack == 'Nâo mencionada no título da vaga! - Front':
        return config('WEBHOOK_FRONT_NO_STACK_URL')
    if stack == 'go':
        return config('WEBHOOK_GO_URL')
    if stack == 'flutter':
        return config('WEBHOOK_FLUTTER_URL')
        