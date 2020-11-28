import urllib.parse
import requests

class GeolocationAPI(object):
    """
    IP Geolocation - JSON endpoint DOCS:
    https://ip-api.com/docs/api:json
    """
    def __init__(self):
        self.host = "http://ip-api.com/json/"

    def get_ip_location(self, ip, fields=[]):

        if fields:
            get_vars = {"fields": ",".join(fields)}
            url = self.host + ip + "?" + urllib.parse.urlencode(get_vars)
        else:
            url = self.host + ip

        r = requests.get(url)

        return r.json()


class DiversityAPI(object):
    """
    Diversity API DOCS:
    https://diversitydata.io/#diversityapi
    """
    def __init__(self):
        self.host = "https://api.diversitydata.io/"

    def get_info_person(self, fullname):

        get_vars = {"fullname": fullname}
        url = self.host + "?" + urllib.parse.urlencode(get_vars)

        r = requests.get(url)

        return r.json()


class QuickchartAPI(object):
    """
    quickchart.io API DOCS:
    https://quickchart.io/documentation/
    """
    def __init__(self):
        self.host = "https://quickchart.io/chart/create"

    def post_chart(self, type_chart, labels, datasets):

        for dataset in datasets:
            if len(dataset["data"]) != len(labels):
                raise Exception("os arrays labels e datasets devem ter o mesmo tamanho")
        
        json_data = {
            "chart": {
                "type": type_chart,
                "data": {"labels": labels, "datasets": datasets}}
        }

        r = requests.post(self.host, json=json_data)


        return r.json()


if __name__ == "__main__":

    geolocation_api = GeolocationAPI()
    # all_fields = geolocation_api.get_ip_location(ip="24.48.0.1")
    # spec_fields = geolocation_api.get_ip_location(ip="24.48.0.1", fields=["status","message","query","country","city"])

    # print(all_fields)
    # print(spec_fields)

    diversity_api = DiversityAPI()
    # info_person = diversity_api.get_info_person(fullname="camila alejandra cortez")

    # print(info_person)

    quick_chart_api = QuickchartAPI()
    chart = quick_chart_api.post_chart(
        type_chart="bar",
        labels=["Jan", "Fev"],
        datasets=[
			{"label": "Foo", "data": [50, 75]},
			{"label":"Cats","data":[100,200]}
		])

    print(chart)
