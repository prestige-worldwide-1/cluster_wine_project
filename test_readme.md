
# Predicting Wine Quality

by Scott Mattes and Martin Reyes

***
[[Project Description](#description)]
[[Project Planning](#goals)]
[[Hypotheses](#hypotheses)]
[[Deliverables](#deliverables)]
[[Key Findings](#findings)]
[[The Plan](#plan)]
[[Data Dictionary](#dictionary)]
[[Data Acquisition and Prep](#wrangle)]
[[Data Exploration](#exploration)]
[[Statistical Analysis](#stats)]
[[Steps to Reproduce](#reproduction)]
[[Takeaways and Conclusions](#conclusions)]
[[Recommendations](#recommendations)]
[[Next Steps](#next_steps)]
___

## <a name="description"></a>Project Description
[[Back to top](#top)]
The goal of this project is to identify drivers of wine quality for the California Wine Institute, utilizing data-driven analysis and machine learning techniques. The primary focus will be on exploring how the utilization of clusters (groupings) of wine samples can improve the performance of the machine learning model, specifically in the context of winery supply chain marketing. This analysis is on data from the Cortez et al 2009 dataset.

## <a name="goals"></a>Project Goals
[[Back to top](#top)]
1. Discover drivers of wine quality.
2. Find useful clusters that help machine learning (ML) models predict wine quality.
3. Use main drivers and clusters to develop a machine learning model to predict wine quality.

## <a name="deliverables"></a>Deliverables
[[Back to top](#top)]

A GitHub repostory which includes:
1. A comprehensive analysis of the dataset, highlighting the drivers of wine quality.
2. Insights on the impact of chemical components on wine quality.
Findings from the cluster analysis and their implications.
3. Comparative evaluation of machine learning models with and without cluster utilization.

A 5-minute professional presentation which includes:
1. An overview of the project
2. A review of key findings


## <a name="hypotheses"></a>Hypotheses
[[Back to top](#top)]
1. **Chemical Composition Impact**: We hypothesize that specific chemical components in wine, such as acidity, residual sugar, and alcohol content, significantly influence wine quality. We expect to observe certain threshold values beyond which these components may positively or negatively affect the wine's overall rating.

2. **Cluster Analysis Effect**: We hypothesize that creating clusters of similar wine samples based on their chemical attributes will help identify distinct groups of wines with similar characteristics which predict their quality rating. By incorporating these clusters as additional features in our machine learning model, we anticipate an improvement in predictive accuracy.

3. **Interaction Effects**: We will investigate potential interactions between different features to determine if their combined influence has a more significant impact on wine quality than individual effects alone.


### 1st Hypothesis

Null hypothesis: There is no significant relationship between _____
Alternative hypothesis: There is a significant relationship between _____

----Results-----

R coefficient: _____ 
P-value: _____

The p-value is _____



### 2nd Hypothesis

Null hypothesis: There is no significant relationship between _____
Alternative hypothesis: There is a significant relationship between _____

----Results-----

R coefficient: _____ 
P-value: _____

The p-value is _____


### 3rd Hypothesis

Null hypothesis: There is no significant relationship between _____
Alternative hypothesis: There is a significant relationship between _____

----Results-----

R coefficient: _____ 
P-value: _____

The p-value is _____



## <a name="findings"></a>Key Findings
[[Back to top](#top)]
***FILL IN LATER***

## <a name="plan"></a>The Plan
[[Back to top](#top)]
1. **Data Preprocessing**: We will begin by exploring the dataset to handle any missing values, outliers, or data integrity issues. Feature engineering will be performed to create additional relevant features, if necessary.

2. **Exploratory Data Analysis (EDA)**: In this phase, we will visualize the distribution of each feature and its relationship with wine quality. We will identify any notable trends or patterns that support or refute our initial hypotheses using appropriate statistical testing such as pearson's r.

3. **Cluster Analysis**: Using unsupervised learning techniques such as K-means clustering, we will group similar wine samples together based on their physiochemical attributes. This will help us gain insights into the different segments of wines present in the dataset.

4. **Machine Learning Models**: We will build predictive models using various algorithms like linear regression, decision trees, random forests, and gradient boosting. Additionally, we will incorporate the identified clusters as additional features and compare the model performance with and without them.

5. **Evaluation**: Model performance will be evaluated using appropriate metrics like root mean squared error (RMSE), and accuracy. The use of clusters will be assessed based on the improvement in model accuracy and interpretability.

## <a name="dictionary"></a>Data Dictionary
[[Back to top](#top)]
| Feature           | Description                                             |
|-------------------|---------------------------------------------------------|
| Fixed acidity     | The non-volatile acids in the wine (g/dm³).             |
| Volatile acidity  | The volatile acids in the wine (g/dm³).                 |
| Citric acid       | The amount of citric acid in the wine (g/dm³).          |
| Residual sugar    | The amount of sugar remaining after fermentation (g/dm³). |
| Chlorides         | The amount of salt in the wine (g/dm³).                |
| Free sulfur dioxide | The free form of SO2, which prevents microbial growth and oxidation (mg/dm³). |
| Total sulfur dioxide | The total amount of SO2, including free and bound forms (mg/dm³). |
| Density           | The density of the wine (g/cm³).                       |
| pH                | The pH level, which measures acidity or alkalinity.     |
| Sulphates         | The amount of sulfur dioxide added as a preservative (g/dm³). |
| Alcohol           | The alcohol content of the wine (% vol.).              |
| Quality           | The quality rating of the wine, on a scale from 0 to 10 (target variable). |

## <a name="wrangle"></a>Data Acquisition and Prep
[[Back to top](#top)]
***FILL IN LATER***

## <a name="exploration"></a>Data Exploration
[[Back to top](#top)]
***FILL IN LATER***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]
***FILL IN LATER***

## <a name="reproducuction"></a>Steps to Reproduce
[[Back to top](#top)]
1. Acquire data from: 'https://query.data.world/s/fgwezltmmhwzdq6frrv7pf6jrl6vps?dws=00000' and 'https://query.data.world/s/otk67utgv5232zzz3ooavdfwpcj2vz?dws=00000'.
2. Set random_state to 123.

## <a name="conclusions"></a>Takeaways and Conclusions
[[Back to top](#top)]

Key drivers of `quality`: 
- Volatile acidity (0.05)
- Alcohol (0.47)
- Density (-0.33)
- Chlorides (0.09)

Best performing ML model:
***FILL IN LATER***


## <a name="recommendations"></a>Recommendations
[[Back to top](#top)]
***FILL IN LATER***


## <a name="next_steps"></a>Next Steps
[[Back to top](#top)]
***FILL IN LATER***