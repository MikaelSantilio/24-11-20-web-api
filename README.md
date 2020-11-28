# Pesquisar WEB APIs e criar um script para acessá-las

Código completo: [main.py](https://github.com/MikaelSantilio/24-11-20-web-api/blob/master/main.py)

## IP Geolocation API

A API de Geolocalização dá informações detalhadas sobre um endreço de IP. A resposta inclue informações sobre país, cidade, CEP, timezone, provedor, etc.

Docs: [https://ip-api.com/docs](https://ip-api.com/docs)

Exemplo de uso:

```python
# Dever ser feita uma requisição GET para o endpoint com o endereço de IP
# http://ip-api.com/json/<<endereco_ip>>

geolocation_api = GeolocationAPI()
all_fields = geolocation_api.get_ip_location(ip="24.48.0.1")

print(all_fields)
# Resposta
"""
{'status': 'success', 'country': 'Canada', 'countryCode': 'CA', 
'region': 'QC', 'regionName': 'Quebec', 'city': 'Montreal', 
'zip': 'H1S', 'lat': 45.5808, 'lon': -73.5825, 'timezone': 'America/Toronto', 
'isp': 'Le Groupe Videotron Ltee', 'org': 'Videotron Ltee', 'as': 'AS5769 Videotron Telecom Ltee', 'query': '24.48.0.1'}
"""

# Também é possivel fazer a requisição GET passando os campos específicos que devem ser retornados dessa forma
# http://ip-api.com/json/<<endereco_ip>>?fields=fields=status,message,query,country,city
spec_fields = geolocation_api.get_ip_location(ip="24.48.0.1", fields=["status","message","query","country","city"])

print(spec_fields)
# Resposta
# {'status': 'success', 'country': 'Canada', 'city': 'Montreal', 'query': '24.48.0.1'}
```

## Diversity API

Uma API para classificar o gênero e raça/etnia de uma pessoa dado o nome completo dela. A API vai retornar o gênero como feminino ou masculino, e etnia como negra, hispânica, asiática, arábica, nativo americano, ilhas dos pacífico ou branco.

Docs: [https://diversitydata.io/#diversityapi](https://diversitydata.io/#diversityapi)

Exemplo de uso:

```python
# Dever ser feita uma requisição GET para o endpoint com o parâmetro fullname
# https://api.diversitydata.io/?fullname<<nome_completo>>

diversity_api = DiversityAPI()
info_person = diversity_api.get_info_person(fullname="camila alejandra cortez")
print(info_person)

# Resposta
"""
{
    'fullname': 'camila alejandra cortez',
    'gender': 'female',
    'ethnicity': 'hispanic',
    'gender probability': 0.9,
    'ethnicity probability': 0.67
}
"""
```

## Quickchart API

QuickChart é um serviço que gera imagens de gráficos de acordo com os parâmetros do body da request.

Docs: [https://quickchart.io/documentation/](https://quickchart.io/documentation/)

Exemplo de uso:

```python
# Dever ser feita uma requisição POST para o endpoint com o body no formato json informando os dados do gráfico.
"""
endpoint: https://quickchart.io/chart/create/
exemplo body:
{
"chart": {
    "type": "bar",
    "data": {"labels": ["Hello", "World"],
    "datasets": [
        {"label": "Foo", "data": [50, 75]},
        {"label":"Cats","data":[100,200]}
    ]}}
}
"""

quick_chart_api = QuickchartAPI()
chart = quick_chart_api.post_chart(
    type_chart="bar",
    labels=["Jan", "Fev"],
    datasets=[
        {"label": "Foo", "data": [50, 75]},
        {"label":"Cats","data":[100,200]}
    ])

print(chart)

"""
{
    'success': True,
    'url': 'https://quickchart.io/chart/render/zf-ad586794-cb12-4b0d-8374-092f6e3f0fce'
} 
"""
```





