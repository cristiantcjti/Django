from django.test import LiveServerTestCase
from selenium import webdriver
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/django_project/Projects/tdd_busca_animal/chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )
        
    def tearDown(self):
        self.browser.quit()


    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando 
        """ 

        home_page = self.browser.get(self.live_server_url + '/')        

        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        busca_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(busca_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        busca_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
 


