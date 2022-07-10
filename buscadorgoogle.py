from requests import session
from requests_html import HTMLSession

def get_source(url):
    session = HTMLSession()
    response = session.get(url)
    return response


def parse_results(response):
     css_identifier_resultado=".GLI8Bc"
     css_identifier_titulo = "h3"
     css_identifier_link = ".yuRUbf a"

     results = response.html.find(css_identifier_resultado)

     output =[]

     for result in results:
        item = {
            'titulo': result.find(css_identifier_titulo, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href']
        }

        output.append(item)
     return output

def google_search():
    response = get_source("https://www.google.com/search?q=Leslie+Lamport")
    return parse_results(response)

resultado_final = google_search()

mi_path ="C:/Users/Admin/Documents/.Informática/Practica1 SistemasD/listagoogle.csv"
f = open(mi_path, 'a+')

"""for resultado in resultado_final:
    print(resultado.get('titulo'),resultado.get('link'))
    print("------------------------")"""

for i in resultado_final:
    var = i.get('titulo') +","+ i.get('link')
    f.write(var)
    f.write(';')
f.close()
    