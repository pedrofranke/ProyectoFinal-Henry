
# Exploratory analysis of Google Maps and Yelp data

![imagen-readme.jpg](https://i.postimg.cc/xjgPNtcQ/imagen-readme.jpg)

## This analysis was carried out to better understand the gastronomic market in the states of New York, California, Texas, Florida and Pennsylvania, during recent years.

# Used technology
- ![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
- ![Colab](https://img.shields.io/badge/-GoogleColab-333333?style=flat&logo=googlecolab)
- ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
- ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
- ![Matplot](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
- ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
- ![NLTK](https://img.shields.io/badge/-NLTK-333333?style=flat&logo=nltk)

## Primary analysis

The first thing that was done in this exploratory analysis was to analyze the databases of [Google Maps](https://drive.google.com/drive/folders/16m-isy1RleH-GhWiC6X5NUmeG-70rGsI?usp=drive_link) :world_map: and [Yelp](https://drive.google.com/drive/folders/1pZEN-KQ6RebnOPg66Sp-Wtl9UXS1Ueb5?usp=drive_link) :bellhop_bell:. This was mainly to see differences and similarities of data from the different platforms and the records of each one.
- [Google](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Analysis/Google%20EDA/EDA_google.ipynb) EDA. 
- [Yelp](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Analysis/Yelp%20EDA/EDA_yelp.ipynb) EDA. 


## Final analysis

> [!NOTE]
> The databases were unified, in order to carry out the definitive exploratory analysis of the data set.

Then we find the unified Google Maps and Yelp databases (this database can be found [here](https://drive.google.com/file/d/1ncUbULkHI1RvguloSLCPQe3vECIyQoD7/view?usp=drive_link)). 

Which contain data from different restaurants in the 5 states mentioned above (New York, California, Texas, Florida and Pennsylvania).

Based on this we began to carry out a deep analysis in 3 different approaches:
- ***Analysis of the number of reviews over time:***
     - Allowed us to see the progress over the years, then in each year and also for each month, which helps us get an idea of when people usually visit restaurants the most.<br>
![rese-as-por-a-o.png](https://i.postimg.cc/yNfT5Fm3/rese-as-por-a-o.png)
- ***Competitiveness analysis:***
     - This analysis allows us to have a better vision of the market where we want the client to enter, since we can visualize the average rating found in each state and also the percentage of competitiveness that exists in each of the states.<br>
![competencia-por-estado.png](https://i.postimg.cc/DZDvZMTQ/competencia-por-estado.png)
- ***Quantitative analysis:***
     - This analysis allows us to visualize the number of restaurants that we can find in each state and their distribution, growth and category.<br>
![restaurantes-por-a-o.png](https://i.postimg.cc/26MPZqSM/restaurantes-por-a-o.png)

### Unified database analysis notebook and functions

- [Here](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Analysis/EDA%20final/EDA_final.ipynb) you can see the entire exploratory analysis notebook carried out for the final conclusions.
- [Here](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Analysis/EDA%20final/functions.py) you can view the different functions used during the analysis.

