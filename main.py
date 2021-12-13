import time

from bs4 import BeautifulSoup
import requests

URL = 'https://www.farmaciasahumada.cl/medicamentos.html?p=2'


def main() -> None:
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.find_all('div', class_='product-item-info')

    for product in products:
        product_brand = product.find('p', class_='product-brand-name').text.strip()
        product_name = product.find('a', class_='product-item-link').text.strip()
        product_price = product.find('span', class_='price').text.strip()
        product_details = product.find('strong', class_='product name product-item-name truncate').a['href']

        with open(f'products.txt', 'a') as products_file:
            products_file.write(f'Marca: {product_brand}\n')
            products_file.write(f'Nombre: {product_name}\n')
            products_file.write(f'Precio: {product_price}\n')
            products_file.write(f'Detalle: {product_details}\n')

            print(f'''
            Marca: {product_brand}
            Nombre: {product_name}
            Precio: {product_price}
            Detalle: {product_details}
            ''')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count = 0
    while True:
        main()
        time_wait = 10
        print(f'Executions {count}')
        print(f'waiting {time_wait} seconds!')
        count += 1
        time.sleep(time_wait)
        break

    print('Finished!')
