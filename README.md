# Дипломна робота

**English version (in progress)**

![img](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/00-img/diploma-work.jpg?raw=true)

# Вміст

1. [Тема та опис роботи](#1-%D1%82%D0%B5%D0%BC%D0%B0-%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D0%B0%D0%BD%D0%B0%D0%BB%D1%96%D0%B7%D1%83-%D1%82%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%96-%D1%82%D0%B5%D0%BA%D1%81%D1%82%D1%83)
2. [Збір даних](#2-%D0%B7%D0%B1%D1%96%D1%80-%D0%B4%D0%B0%D0%BD%D0%B8%D1%85)

# 1. Тема: «Інтелектуальна система аналізу тональності тексту» 

### I. Мета

Моєю метою є розробка моделі для аналізу тональності текстів українських текстів. Існує чимало рішень для англомовних текстів, але цим не може похвалитися солов'їна, що хочеться виправити.

### II. Як ви можете допомогти?

Якщо Вам цікавить схожа тема, то напишіть мені на пошту: **oleksandr.kosovan@yahoo.com**


# 2. Збір даних

### I. Вибір джерела збору даних

Для збору текстів я обрав [hotline](https://hotline.ua/reviews/yp/). Чому? Тому, що даний сайт має посортовані відгуки на позитивні та негативні, що забирає етап маркування даних. Позитивні відгуки - це відгуки з оцінками  **від 7 до 10**, а негативні оцінки **від 0 до 3**.

![screen reviews](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/00-img/screen-rozetka.png?raw=true)

### ІІ. Як я збирав дані?

Для збору даних з вебсторінки я використовував бібліотеку [Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)). Але під час збору даних, я зустрівська з кількома проблемами.

**1 проблема** 

При використанні Beautiful Soup я отримував помилку: *503 Service Temporarily Unavailable*. Скоріше всього, hotline зробило обмеження, яке не дозволяє парсити сторінку звичними для цього підходами і це цілком логічно. Як я обійшов це обмеження? Я скористався [Selenium](https://selenium-python.readthedocs.io/) — інструмент для автоматизації роботи в web-браузері,  а саме використав [chromedriver](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver). [Jupyter Notebook](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/02-data-collections/02-scraping-test.ipynb)

**2 проблема**

Далеко не всі відгуки на сайті написані українською мовою, тому я вирішив виявляти український текст і тільки тоді його записувати. Для цього я скористався бібліотекою [langdetect](https://pypi.org/project/langdetect/), яка чудово справилася зі своїм завданням. [Jupyter Notebook](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/02-data-collections/01-langdetect-test.ipynb)

**3 проблема**

Якщо відбирати тільки українськомовні тексти, то втрачається значна частина текстів. Тому є сенс скористатися Google Перекладачем. Я протестував три бібліотеки:

- [googletrans](https://pypi.org/project/googletrans/) (*має обмеження на кількість запитів*)
- [translate](https://pypi.org/project/translate/) (*не працює*)
- [google.cloud.translate_v2](https://pypi.org/project/google-cloud-translate/) (*чудово працює. але потребує додаткових налаштувань на google cloud. Є платним. Я скористався пробним періодом.*)

[Jupyter Notebook](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/02-data-collections/01-langdetect-test.ipynb)

[Cloud Translation documentation](https://cloud.google.com/translate/docs) є, дійсно, зручним інструментом. Також можна моніторити кількісно та якісно всі запити на API.

![api](https://github.com/OleksandrKosovan/sentiment-analysis-uk/blob/master/00-img/api-screen.png?raw=true)



