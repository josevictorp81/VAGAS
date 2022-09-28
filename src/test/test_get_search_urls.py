from ..utils.get_search_urls import get_search_url
from decouple import config


def test_return_django_url():
    """ test return search django url """
    assert get_search_url(stack='django') == config('SEARCH_DJANGO_URL')
    assert get_search_url(stack='django') != config('SEARCH_NODE_URL')


def test_return_node_url():
    """ test return search node url """
    assert get_search_url(stack='node') == config('SEARCH_NODE_URL')
    assert get_search_url(stack='node') != config('SEARCH_DJANGO_URL')


def test_return_ruby_url():
    """ test return search ruby url """
    assert get_search_url(stack='ruby') == config('SEARCH_RUBY_URL')
    assert get_search_url(stack='ruby') != config('SEARCH_NET_URL')


def test_return_net_url():
    """ test return search .net url """
    assert get_search_url(stack='.net') == config('SEARCH_NET_URL')
    assert get_search_url(stack='.net') != config('SEARCH_RUBY_URL')


def test_return_no_label_url():
    """ test return search no label url """
    assert get_search_url(stack='back no label') == config('SEARCH_JOBS_BACK_NO_LABEL')
    assert get_search_url(stack='back no label') != config('SEARCH_RUBY_URL')