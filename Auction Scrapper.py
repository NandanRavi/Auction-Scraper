import requests
from bs4 import BeautifulSoup
import csv


class Scraper:
    def __init__(self):
        self.data_list = []
        self.n_list = []

    def find_missing_number(self, arr):
        n = len(arr) + 1
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        missing_number = expected_sum - actual_sum
        return missing_number

    def scrape_page(self, element):
        print(element['id'], "Scraping")
        URL = requests.get(element['link'])
        html_text = URL.content
        soup = BeautifulSoup(html_text, 'html.parser')
        meta_data = soup.find('meta', property="og:image")
        div_data = soup.find_all('div', class_="lot-page__lot")
        data_dict = {
            'image': meta_data['content'],
            **element
        }
        try:
            for divData in div_data:
                data_dict["property"] = divData.find('p', class_="lot-page__lot__preface").text
                data_dict["Sno"] = divData.find('h3', class_="lot-page__lot__number").text
                data_dict["authorName"] = divData.find('h1', class_='lot-page__lot__maker__name').text
                data_dict["material"] = divData.find('p', class_='lot-page__lot__additional-info').text
                data_dict["estimatePrice"] = divData.find('p', class_='lot-page__lot__estimate').text
                data_dict["sellPrice"] = divData.find('p', class_='lot-page__lot__sold').text
        except:
            data_dict["property"] = None
            data_dict["Sno"] = None
            data_dict["authorName"] = None
            data_dict["material"] = None
            data_dict["estimatePrice"] = None
            data_dict["sellPrice"] = None

        return data_dict

    def scrape_web(self):
        URL = requests.get("https://www.phillips.com/auctions/auction/UK010122")
        html_text = URL.content
        soup = BeautifulSoup(html_text, "html.parser")
        datas = soup.find_all('li', class_='lot single-cell')

        for data in datas:
            try:
                num = data.find('strong', class_="phillips-lot__description__lot-number-wrapper__lot-number").text
                name = data.find('p', class_='phillips-lot__description__artist').text
                anchor_tag = data.find('a', class_="phillips-lot__description phillips-lot__description--has-hammer")
                if anchor_tag:
                    link = anchor_tag.get('href')
                else:
                    link = None
                self.data_list.append({
                    'id': num,
                    'name': name,
                    'link': link,
                })
                self.n_list.append(int(num))

            except:
                num = self.find_missing_number(self.n_list)
                self.n_list.append(num)
                self.data_list.append({'id': num,
                            'name': None,
                            'link': None,
                            })

        final_list = []
        for Dlist in self.data_list:
            if Dlist['link'] is not None:
                final_list.append(self.scrape_page(Dlist))

        with open('main.csv', 'a', encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f,
                                        fieldnames=['id', 'name', 'link', 'image', 'property', 'Sno', 'authorName',
                                                    'material', 'estimatePrice', 'sellPrice'])
            csv_writer.writeheader()
            csv_writer.writerows(final_list)


scraper = Scraper()
scraper.scrape_web()
