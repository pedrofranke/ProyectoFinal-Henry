# Data Engineering for Project

This document outlines the Data Engineering process for our project, detailing the scope determination, data processing, and pipeline creation.

## Table of Contents

1. [Project Scope](#project-scope)
2. [Data Processing](#data-processing)
   - [Google and Yelp Data](#google-and-yelp-data)
   - [Data Unification](#data-unification)
3. [Data Visualization and Dictionaries](#data-visualization-and-dictionaries)
4. [Pipeline](#pipeline)

## Project Scope

To determine the project's scope, we utilized web scraping techniques and data from Google Analytics to identify the top 5 states our project will focus on. The detailed process is documented in the [Scope Workbook](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Engineering/Scope.ipynb).

## Data Processing

### Google and Yelp Data

Our initial data sources were JSON files from Google and Yelp, which required thorough analysis and cleaning to ensure compatibility for future exploratory data analysis (EDA). This process resulted in four primary tables: Restaurants, Users, Reviews, and a Category dummy table. These tables were later integrated into BigQuery. The ETL processes for each source are documented below:

- Google: [Google ETL Process](https://github.com/pedrofranke/ProyectoFinal-Henry/tree/main/Data%20Engineering/Google%20ETL)
- Yelp: [Yelp ETL Process](https://github.com/pedrofranke/ProyectoFinal-Henry/tree/main/Data%20Engineering/Yelp%20ETL)

Processed data can be found here: [Processed Data](https://github.com/pedrofranke/ProyectoFinal-Henry/tree/main/Data%20Engineering/Processed%20Data).

### Data Unification

To facilitate EDA and the development of machine learning products, we merged the datasets from Google and Yelp. The unified dataset and the ETL process documentation are available here: [Data Unification Process](https://github.com/pedrofranke/ProyectoFinal-Henry/tree/main/Data%20Engineering/Unification).

## Data Visualization and Dictionaries

To better understand the relationships between different entities in our dataset, we created a Database Entity Relationship (DER) diagram, illustrated below:

<p align='center'>
  <img src="https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Images/DER%20Diagram.jpg" alt="DER Diagram" width="800">
</p>

Additionally, we prepared a comprehensive data dictionary detailing each data element for both Google and Yelp datasets, accessible here: [Data Dictionary](https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Data%20Engineering/Data%20Dictionary.xlsx).

## Pipeline

Our data pipeline is illustrated in the following diagram, showcasing the flow from initial data loading to the final EDA and machine learning model integration:

<p align='center'>
  <img src="https://github.com/pedrofranke/ProyectoFinal-Henry/blob/main/Images/pipeline.giff.gif" alt="Pipeline Diagram" width="800">
</p>

Brief overview of the process:

- Initial loading of Google and Yelp datasets was performed using Visual Studio Code and Python, supplemented by Google Analytics and the Geo PI API.
- The initial datasets were stored in a Google Cloud Storage bucket.
- Using Google Cloud services, we set up a virtual environment with Composer to host Airflow, which automated the ETL process for new files added to the storage bucket. This automation is achieved through DAGs, Python scripts that define the ETL workflow.
- New files detected in the bucket are transformed and then stored in the appropriate BigQuery tables.
- Google Colab was used for final EDA, which feeds into a Power BI dashboard for client interaction and two machine learning models integrated into a Streamlit-based recommendation system, offering a UI for client interaction.
