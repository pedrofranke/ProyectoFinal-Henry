# Yelp Platform ETL (Extract, Transform, Load) Process

In this folder, you will find the files where the data was loaded, and the respective transformations were applied to each of them. Additionally, the custom module [Tools](Tools.py) is included, containing the functions used to handle the data.

## Working Elements

Three datasets were provided for the ETL process, which are:

  * Business: It contains the following columns:

    * business_id: Identifier for each restaurant.
    * name: Restaurant name.
    * address: Restaurant address.
    * city: City where the restaurant is located.
    * state: State where the restaurant is situated.
    * postal_code: Postal code of the restaurant.
    * latitude: Latitude on the map for the restaurant.
    * longitude: Longitude on the map for the restaurant.
    * stars: Rating of the restaurant.
    * review_count: Number of reviews for the restaurant.
    * categories: Categories of the businesses

  * review: It contains the following columns:
    *	review_id: Identifier for each review.
    * user_id: Identifier for each user.
    * business_id: Identifier for each restaurant.
    * stars: Rating of each review.
    * text: Review written by the user.
    * date: Date and time of the review.

  * user: It contains the following columns:
    * user_id: Identifier for each user
    * name: Name of each user
    * review_count: Number of reviews made by the user
    * useful: Number of votes marked as useful by other users for that user.

In this [link](https://drive.google.com/drive/u/0/folders/1WU5_DdsyMk8aHlTQtk5p1IecbJYhu-iU), you can find the datasets already transformed and in parquet format.

The transformations in the datasets involved unnesting some columns as they were in dictionary format. Subsequently, the treatment of null or missing data was addressed, along with handling different data types within a column. Additionally, unnecessary columns, duplicate records, and columns were removed, and a dummy table was created. The entire dataset was then exported in parquet format for improved storage and compression.

Si quieres ir a los archivos con los procesos de limpieza de cada dataset presiona los siguientes links: [ETL_business](ETL_business.ipynb), [ETL_reviews](ETL_reviews.ipynb) y [ETL_user](ETL_user.ipynb)
