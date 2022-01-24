import scrapy
from validations.validations import format_cpf, format_name

class UniversitySpider(scrapy.Spider):
    name = 'university'

    # Caso queira pegar todos os dados, deixe o valor da first_page como 1 e da last_page como 4671
    # Caso queira, você pode modificar o range alterando os valores para first_page = 1 e last_page = 10
    # para pegar os dados somente das 10 primeiras páginas.
    first_page = 1
    last_page = 50
    range_scrap = range(first_page, last_page + 1)

    # list comprehension para guardar todas as urls que serão acessadas.
    start_urls = [f'https://sample-university-site.herokuapp.com/approvals/{i}' for i in range_scrap]

    # Entra na página e localiza todos os elementos com cpf e pega sua href
    def parse(self, response):
        for link in response.css('li a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_user)
    
    # Realiza esta função, quando entra em um cpf.
    def parse_user(self, response):
        # pega o cpf da url
        cpf = response.request.url.split("/")[4]
        cpf_dict = format_cpf(cpf)
        # Valida o cpf, e se for válido, formata e guarda no banco, caso não seja os dados são pulados.
        users = response.css('div')
        data = [user.css('div::text').get().strip() for user in users]
        yield {
            'name': format_name(data[0]),
            'cpf': cpf_dict['formatted'],
            'score': float(data[1]),
            'valid_cpf': cpf_dict['is_valid'],
        }

