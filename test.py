from bs4 import BeautifulSoup


def main() -> None:
    with open('home.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')
        courses_html_tags = soup.findAll('h5')
        course_cards = soup.find_all('div', class_='card')
        # tags = soup.find('h5')
        # print(soup.prettify())
        for course in course_cards:
            course_name = course.h5.text
            course_price = course.a.text.split()[-1]

            print(f'{course_name} costs {course_price}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
