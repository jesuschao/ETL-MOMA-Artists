# W5-ETL-Project

# [W5-ETL-Project] Jesús Chao

## Approach to artists in MOMA since the last 50 years")

![](https://losviajesdesofia.com/wp-content/uploads/MoMA-Museum.jpg)

PURPOSE.

The aim of this project is extending a MOMA´s artists database taken from [Kaggle](https://www.kaggle.com/momanyc/museum-collection) with some interesting insights of the education and economy from the countries they are from. Naturally, this work is just an approach/sketch to the artists´s instruction and economic environment but does not want to draw any conclusion of it; many other facts should have been taken into account.

PROCEDURE.

1_ I have imported a database from kaggle referred to the art&artists that have exhibited their work in MOMA. To get a better outline, I have decided to focus on the artists that have have exposed in the last 50 years.

2_ I have cleaned the csv from columns that are irrelevant for my goal; "Title", "ConstituentID", "ArtistBio" ... In addition to this, I modified other columns such as "Date", "Nationality" or "Artist" for managing the table.


3_ I have introduced some data using "BeautifulSoup" scrapping from these websites;

    - [Chartsbin](http://chartsbin.com/view/41109) that shows the creativity index by country.
    - [Country economy](https://countryeconomy.com/gdp?year=1980) that shows the GDP by country.

4_ Finally, I have joined all the information in one single table using MySQL.


![](https://i.ytimg.com/vi/v9YSbIEhFik/maxresdefault.jpg)


BIBLIOGRAPHIC REFERENCES AND RESOURCES.

[Kaggle](https://www.kaggle.com/datasets)

[Numpy](https://numpy.org/doc/1.18/)

[Pandas](https://pandas.pydata.org/)

[Python functions](https://docs.python.org/3/library/functions.html)

[Stack overflow](https://stackoverflow.com/)