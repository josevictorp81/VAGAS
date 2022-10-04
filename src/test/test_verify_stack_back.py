from ..utils.verify_stack import verify_stack_back, verify_stack_front

def test_return_python():
    """ test return python label """
    assert verify_stack_back(title='[Joinville] Python Developer @ Neocredit') == 'python'


def test_return_net():
    """ test return .net label """
    assert verify_stack_back(title='.NET Engineer na Coodesh') == '.net'


def test_return_ruby():
    """ test return ruby label """
    assert verify_stack_back(title='Back-end developer Ruby on Rails Pleno na SambaTech') == 'ruby'


def test_return_node():
    """ test return node label """
    assert verify_stack_back(title='Fullstack NodeJS Dev Jr - Whats') == 'node'


def test_return_go():
    """ test return go/golang label """
    assert verify_stack_back(title='Fullstack go - Whats') == 'go'


def test_return_no_label():
    """ test return no label """
    assert verify_stack_back(title='Fullstack developer Java Sênior - Tecnologia Única') == 'Nâo mencionada no título da vaga! - Back'
    assert verify_stack_back(title='Fullstack NodeJS Dev Jr - Whats') != 'Nâo mencionada no título da vaga! - Back'


def test_return_reat_native():
    """ test return react native label """
    assert verify_stack_front(title='React-native developer Sênior') == 'react native'


def test_return_reat():
    """ test return react label """
    assert verify_stack_front(title='React developer Pleno') == 'react'


def test_return_vue():
    """ test return vue label """
    assert verify_stack_front(title='Vue.js developer Pleno') == 'vue'


def test_return_agular():
    """ test return agular label """
    assert verify_stack_front(title='Angular developer Pleno') == 'angular'


def test_return_no_label_title():
    """ test return no title label """
    assert verify_stack_front(title='Fullstack developer Pleno') == 'Nâo mencionada no título da vaga! - Front'
