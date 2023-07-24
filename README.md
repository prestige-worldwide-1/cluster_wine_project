
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
[[Modeling](#model)]
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


## <a name="findings"></a>Key Findings
[[Back to top](#top)]
1. The top four predictive features of wine quality are:
- alcohol percentage 
- density
- volatile acidity 
- chlorides

2. Regression models trained on 2-dimensional and 3-dimensional clusters of features found in this dataset offer only negligible performance increase from regression models trained on the original columns in the dataset.


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
Data acquired from data.world
('https://query.data.world/s/fgwezltmmhwzdq6frrv7pf6jrl6vps?dws=00000' and 'https://query.data.world/s/otk67utgv5232zzz3ooavdfwpcj2vz?dws=00000')

6,497 rows/wine scores
1,177 duplicate wines dropped from data
Saw no missing values
Saw minor outliers, but kept them.
The data was split to avoid data leakage (70/15/15 split)


## <a name="exploration"></a>Data Exploration
[[Back to top](#top)]

Bivariate exploration:
Alcohol, density, volatile acidity, and chlorides showed an apparent relationship through exploratory graphs.


## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### 1st Hypothesis

Confidence level: 95%

Null hypothesis: There is no significant relationship between alcohol and qualtiy.
Alternative hypothesis: There is a significant relationship between alcohol and qualtiy.

----Results-----

R coefficient: 0.48 
P-value: 1.01e-217

The p-value is below the alpha. We can reject the null hypotheses. We can be confident that the relationship between alcohol and quality is significant. 

### 2nd Hypothesis

Confidence level: 95%

Null hypothesis: There is no significant relationship between density and qualtiy.
Alternative hypothesis: There is a significant relationship between density and qualtiy.

----Results-----

R coefficient: -0.35
P-value: 4.19e-110

The p-value is The p-value is below the alpha. We can reject the null hypotheses. We can be confident that the relationship between density and quality is significant. 


### 3rd Hypothesis

Confidence level: 95%

Null hypothesis: There is no significant relationship between volatile acidity and qualtiy.
Alternative hypothesis: There is a significant relationship between volatile acidity and qualtiy.

----Results-----

R coefficient: -0.26
P-value: 6.74e-60

The p-value is The p-value is below the alpha. We can reject the null hypotheses. We can be confident that the relationship between volatile acidity and quality is significant.


### 4th Hypothesis

Confidence level: 95%

Null hypothesis: There is no significant relationship between chlorides and qualtiy.
Alternative hypothesis: There is a significant relationship between chlorides and qualtiy.

----Results-----

R coefficient: -0.21
P-value: 2.37e-37

The p-value is The p-value is below the alpha. We can reject the null hypotheses. We can be confident that the relationship between chlorides and quality is significant.


## <a name="model"></a>Modeling
[[Back to top](#top)]

The baseline model was DummyRegressor, which makes every prediction 5.8, the mean quality score.

Performance metrics:
Train:	RMSE = 0.877247065526987	R2 = 0.0
Test:	RMSE = 0.8709556563730244	R2 = -0.004223135332819483


The best model without clusters was OLS.

Performance metrics:
Train:	RMSE = 0.7398947098676343	R2 = 0.2886292628795276
Test:	RMSE = 0.7464181576392369	R2 = 0.2624312195350209


The best model with clusters was OLS.

Performance metrics:
Train:	RMSE = 0.7397021358155124	R2 = 0.28899951479789776
Test:	RMSE = 0.7465117684370821	R2 = 0.26224620599845816


## <a name="reproducuction"></a>Steps to Reproduce
[[Back to top](#top)]
1. Acquire data from: 'https://query.data.world/s/fgwezltmmhwzdq6frrv7pf6jrl6vps?dws=00000' and 'https://query.data.world/s/otk67utgv5232zzz3ooavdfwpcj2vz?dws=00000'.
2. Set random_state to 123.
3. Follow steps outlined in the final report document using the functions found in the wrangle, exploration and modeling .py files


## <a name="conclusions"></a>Takeaways and Conclusions
[[Back to top](#top)]

Key drivers of `quality`: 
- Alcohol (0.48)
- Density (-0.35)
- Volatile acidity (-0.26)
- Chlorides (-0.21)

Best performing ML model was OLS without clusters.

Performance metrics:
Train:	RMSE = 0.7398947098676343	R2 = 0.2886292628795276
Test:	RMSE = 0.7464181576392369	R2 = 0.2624312195350209


## <a name="recommendations"></a>Recommendations
[[Back to top](#top)]
1. Emphasize alcohol, volatile acidity, and chlorides during feature engineering for any future modeling attempts
2. Consider predicting without clusters


## <a name="next_steps"></a>Next Steps
[[Back to top](#top)]
1. Find clusters with alternative methods like DBSCAN
2. Use classification algorithms to predict wine quality
3. Collect more data on features of wine that can be incorporated into future models (e.g. grape varieties, fertilizers, climate conditions, etc.)

