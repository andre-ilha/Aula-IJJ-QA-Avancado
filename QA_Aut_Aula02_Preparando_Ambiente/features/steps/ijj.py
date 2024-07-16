from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from behave import given, when, then

@given('nos estamos com a pagina do instituto aberta')
def step_impl(context):
    context.browser = Firefox()
    context.browser.get('https://www.jogajuntoinstituto.org/')
    title = context.browser.title
    assert 'Instituto Joga Junto' in title, "Página incorreta na busca"

@when('nos preenchemos o formulário')
def step_impl(context):
    input_nome = context.browser.find_element(By.ID, "nome")
    input_nome.send_keys('André Alves de Lima')

    input_email = context.browser.find_element(By.ID, "email")
    input_email.send_keys('alveslimaandre@gmail.com')

    input_assunto = context.browser.find_element(By.ID, "assunto")
    select = Select(input_assunto)
    select.select_by_index(5)

    input_msg = context.browser.find_element(By.ID, "mensagem")
    input_msg.send_keys('Meu primeiro script de automação - Squad 6')

@then('apertamos o botão de enviar')
def step_impl(context):
    button_enviar = context.browser.find_element(By.XPATH, "//button[@type='submit']")
    button_enviar.submit()

    time.sleep(10)
    context.browser.quit()