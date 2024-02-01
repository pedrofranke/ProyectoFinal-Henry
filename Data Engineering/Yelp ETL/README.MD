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
