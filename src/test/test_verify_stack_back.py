from ..utils.verify_stack import verify_stack_back

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