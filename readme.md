# Individual project - Customer Segmentation Using Clustering Models

### Project Description:
- This project builds on the basic concepts of customer segmentation, where recency, frequency, and monetary value are calculated and the customer groups are mannualy selected, by introducing more complex feature engineering, multiple additional features for modeling, and by using clustering machine learning models to identify customer groups at a more precise level. 

### Project Goal:
- The goal of this project was to apply feature engineering and machine learning modeling to conduct a high level customer segmentation analysis and provide specific customer groupings as well as insight on the customers within the groups to develop group specific targeted marketing strategies.

### Data Dictionary:

| Variable | Meaning |
|----------|---------|
|last_purchase|is the datetime stamp of the most recent purchase the customer has made and is used to calculate recency|
|recency|takes the datetime stamp from the day after the last entry in the overall dataset and subtracts the last_purchase value to give a number of days since the customers last purchase|
|frequency| is the total number of orders the individual has made with the company|
|sales_total|calculates the total sales value for each order (row) to be used for calculating the customers overall monetary value|
|monetary|is the total value of all orders made by that indivdiual customer|
|average_order_value|is the average value of all orders made by the individual customer|
|avg_items_ordered| is the average quantity of items ordered across all orders made by that customer|
|unique_items_count|is the number of unique items purchased by the individual customer across all their orders|
|dist_rating|is a ranked number representing the distance of the customer's home country from the company's country|

### Key Findings:
- Customer Group 1:

    - Customer group 1 represents our top customers. They have the lowest average number of days since their last order, the highest average frequency of orders, and the second highest average customer monetary value. They also had the highest average number of unique items ordered.

- Customer Group 2:

    - Customer group 2 represents potentially lost customers. They have the highest average number of days since their last purchase (almost a year), the lowest average frequency of orders, and the lowest average customer monetary value. It is interesting to note that while this group likely cotains lost customers they did have the highest average individual order value and the highest average number of items per order.

- Customer Group 3:

    - Customer group 3 represnets at risk customers. They were ranked third in average recency, frequency, and monetary value and had comparable average order value, average number of items ordered, and average number of unique items ordered.

- Customer Group 4:

    - Customer group 4 represents moderate to high value customers. While they were just behind customer group 1 in recency, frequency, and number of unique items ordered, they had the highest average monetary value and comparable secondary feature values to the other groups.

### Marketing Recomendations:
- Customer Group 1:

    - This group represents our top customers so we should target this group promotions to maintain engagement and reward loyalty to the company such as loalty program membership or special early access to new products.

- Customer Group 2:

    - This group most likely represents lost customers so it will be last priority but shouldnt be forgotten. This group may respond to marketing that reminds them about the company or their previous engagements with it such as newsletters or promotions based on previously purchased items. This group may also be able to provide usefull insight as to why they have not made a purchase in a long time or why they did not make more frequent purchases that could inform future marketing efforts and product placement.

- Customer Group 3:

    - This group represents at risk customers and should be targeted with marketing focused on retension such as special offers, discount pricing, and specific customer engagement.

- Customer Group 4:

    - While this group did not make purchases as often as customers in group 1 they had a higher average monetary value making them our biggest spenders. They would likely respond well to marketing such as luxury offers or access to special higher value products. It is also important to note that on average, customers in this group have not made an order in the last two and a half months so they may also respond well to promotions focused on retension such as those suggested for customer group 3. This group may also respond well to promotions for new or interesting products since they had the second highest average number of unique items ordered.

### Next Steps:
- There are numerous ways to continue to refine customer segmentation analysis. If I had more time I would explore these areas:

    - Adding weight to customer features based on specific buisness needs. In this project the clustering was done with all features having equal weight. If, for example, the company was looking to focus on increasing frequency of customer orders, that variable could have more weight added before the clustering modeling stage and would potentially produce different customer groupings.

    - For this project I used a min-max scaler to give all the features the same weight prior to modeling. There are other options for scaling the data, most notably a standard scaler which normalizes the data and would potentially produce different customer groupings.

    - The location data in this dataset waas only seperated by country and while a siple distance from company rating was used in the model, it had minimal impact and minimal value to customer characteristics so it represents an area for further exploration.

    - Feature engineering provides infinite possibilities for data aggregation and with more domain knowledge it would be possible to create domain specific features that could be used with modeling and potentially produce different or more refined customer groupings.

    