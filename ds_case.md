# Verve Group data science case study

## Gender classification.
On this task we need to build a classification model, with gender as the target. For this purpose we have to use some summary statistics and visualisations about the dataset.

User can have events from different apps, so with high probability we have less users than events. Which means, we need to find the tuple `user_id` -> `gender`. There are different options to solve this task:

**Option 1.** Aggregate all data to obtain a new dataset where `user_id` is primary key, where for each `user_id` only one row with all aggregated data.

**Option 2.** Classify all rows on the original dataset and then aggregate results to find the final gender, because one user can not have more than one gender.

## Potential problems:
1. There is not any information about count of unique `user_id`, we have only "Frequencies for variable gender" which is less informative than can be, because it shows only that "male" have more events than "female". And no information about real frequency gender for unique `user_id`.
2. `device_name` is a good feature and it can give a lot of information. First of all, from device_name we can mine a person name, using some nlp libraries and a dictionary of names. From this a person's name can make some classes like “definitely a male name”, “definitely a female name” and “unisex name/not name”. But what we have to do with users without device_name. The solution is adding this users to “unisex name/not name” class or make some other class. Like problem 1 missing `device_name` will be more informative if known gender frequency for `device_name`. This information can show some people's behavior and a reason for why `device_name` is missed for 60% of events is connection with the platform of mobile devices or maybe people don't give names for mobile devices (although this is unlikely since the mobile device usually has a default name). Knowing the causes of why and how is `device_name` connected with gender can give us good information, for example if user_id with missed device_name 90% of them "male", it gives a very strong feature.
3. A small amount of information, for all events clicks "YES" only 0.5% it is too few to make normal analysis. If it was billions of rows of events it would be normal, but we have less than 4k rows and it's not enough. 

## Features.
1. How to get feature from `device_name` is given above in the "Potential problems" paragraph.
2. We can’t get features from `ad_category` and `click` because information with clicks isn't enough and it can't give something informative. And `ad_category` is directly related to `click`.
3. `app_category` and `interaction_with_app` provide good information. These two features let us determine how long a user interacts with different apps, because some of the app categories can be gender oriented or most of the audience the same gender.


#### Option 1.
For this option we need to aggregate all data for each user: `app_category` can be encoded on features where each category will be a new feature with values of the sum or average time in this category app.

#### Option 2.
For this option we need to aggregate results of classification. We can use regression, not classification, to provide probability of gender and then find maximum or average of probability to give the answer.

## Model.

Dataset is too small, so using complex and big models is meaningless. Obviously boosting models like Random forest or XGBoost has a lot of advantages, they can work with categorical features, handle nan/null values, but easily are overfitting on the small size datasets. 

We need to use something simpler like Logistic Regression. That algorithm interpreted, very efficient to train, gives information about the importance of each feature. Also it can overfit, so we need to be careful with parameters and it can't handle nan/null values.