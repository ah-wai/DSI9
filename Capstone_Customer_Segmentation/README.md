# Project Capstone: Customer Segmentation for an e-commerce retailer from the UK

## Problem Statement:
Group and understand the habits of the customers so that the company can gain a deeper understanding of their preferences.
​
## Methodology:
Using transaction data, we will first group the products into categories before grouping customers based on their shopping habits.<br>
Finally, we will break down their habits and recommend potential actions to gain incremental revenue for the company
​
## Constrains:
1. There are missing description and customerid which might mean potential error in the analysis.<br>
2. Some of the product description are not related to the product, hence you can't 100% be sure that the sale transacted or delivered <br>
3. There are no pre-defined product categories, without this, it will impact on the granularity of the analysis or how deep we can go with the grouping of the customers 
​
## Materials:
1. Data <br>

  - The original dataset is labelled "data.csv", the rest are the post manipulation subset/ check points of the original dataset <br>
2. 1.0 Customer Segmentation <br>

  - Main coding sequence for the analysis of the data <br>
3. Presentation slides in pptx and pdf <br>
4. final_model for export to deployment <br>
5. simliar words.png for categorical grouping of the products <br>

## Recommendation & Conclusion:
 ### Modelling & Prediction
During the first phase, we will assume that missing customerid are new customers without registering/logging in, hence the missing customerid.<br> 
After removing duplicates and other unnesscary data, we will begin grouping products into their categories.<br> 
Using a Latent Dirichlet Allocation (LDA) model, we will extract frequent words in the dataset to cluster them into their groups.<br> 
After which, we will group all transactions together then group all customers by transactions to find out total customers. <br>
Once done, we will use a semi-supervised approach to group these customers into their classes. <br>
First, using Agglomerative Hierarchical Clustering (an unsupervised model), we will group these customers into their classes. <br> 
Once we obtain their labels, we will parse them through a decision tree (a supervised model) to determine if the approach was clearly able to define them. <br>
With a 99.3% accuracy, we can safely say that the approach works for this dataset. <br> 
Finally, we will use the decision tree to breakdown each classes habits. <br>

    1. Loyal Customers
    2. Heavy Occasional Customers
    3. Light Loyal Customers
    4. Occasional Customers
    5. Trailist
    
Using this, we will then be recommend actions for each groups and also potential incremental earnings based on these actions. <br>

## Presentation Slides <br>
You may find the presentation slides [here](https://github.com/ah-wai/DSI9/blob/master/Capstone_Customer_Segmentation/Capstone%20Presentation.pdf)
