import requests

class JSON_data:

    def __init__ (self,url):
        self.url = url
        self.response = requests.get(url)

    def server_status(self):
        return self.response.status_code
    
    def fetch_data(self):
        try:
            if self.server_status() == 200:
                return self.response.json()
            else:
                print(self.server_status())
        except:
            print("Error")
    
    def getcountries(self):
        result = []

        for item in self.fetch_data():
            result.append(item['name']['official'])
        
        return result
    
    def getCurrencies(self):
        result = []

        for item in self.fetch_data():
            result.append(item['currencies']['name']['symbol'])
        return result

url = 'https://restcountries.com/v3.1/all'
obj = JSON_data(url)
print(obj.getcountries())
print(obj.getCurrencies())

