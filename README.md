# Model Classification Project

## Project description:
- Identify drivers of churn from the Telco dataset
- Run statistical tests to identify relationships between features
- Construct a machine learning model to predict customer churn


## Data dictionary:
|                       | type    | description                                                             |
|:----------------------|:--------|:------------------------------------------------------------------------|
| customer_id           | object  | The customers unique ID                                                 |
| is_female             | int64   | The customers gender                                                    |
| senior_citizen        | int64   | Whethe or not the customer falls under the description "senior citizen" |
| fam_status            | object  | Whether or not the customer is partnered or has children                |
| tenure                | int64   | How many months the customer has been with Telco                        |
| phone_lines           | object  | How many phone lines the customer has                                   |
| online_services       | object  | Whether or not the customer has online backup or security               |
| tech_support          | object  | Whether or no the customer has tech support                             |
| streaming             | object  | Whether or not the customer streams movies or tv                        |
| contract_type_id      | int64   | How the customer is signed up for billing                               |
| paperless_billing     | int64   | Whether the customer is mailed bills or not                             |
| payment_type_id       | int64   | How the customer pays their bill                                        |
| monthly_charges       | float64 | How much the customer is charged per month                              |
| total_charges         | float64 | Total charges during the customers time with Telco                      |
| churn                 | int64   | Whether the customer is still with Telco or not                         |
| internet_service_type | object  | Whether the customer has Fiber, DSL, or no internet                     |
| years_held            | float64 | Years the customer has been with Telco                                  |


## Project Plan:
- Import necessary packages and functions
- Acquire and clean data, acquire MVP, split into necessary groupings (Train, test, validate)
- Explore and look over data for relationships/trends
- Run statistical tests to further identify relationships between features
- Additional data cleaning to prepare for modeling
- Experiment with different models to see which are most effective at predicting train data
- Choose best couple models from train to use on validate
- Best model on validate performed on test
- Deliver results


## Instructions for recreation:
- Import all packages and functions
- env.py file with SQL password, username, and host to acquire data
- Use get_telco_data() function to acquire initial data
- Use clean_telco() function to prepare data for exploration
- Split the data into train, test, and validate
- Plot variables in univariate, bivariate, and multivariate formats to form hypotheses
- Run chi^2 tests on train dataset between the following groups:
    - churn and internet_service_type
    - churn and senior_citizen
    - senior_citizen with and without tech support and churn
- Use modeling_telco() function on result of clean_telco() dataframe to prepare data for modeling (mainly creating dummies)
- Re-split data into train, test, and validate
- Test models with varying parameters for optimization
- Use best models to use on validate set
- Use the best on test data set

## Findings
- Biggest determining factors for churn among most models were contract type, internet type, and years with the company
- In my statistical tests, it was found that internet type was not independent of churn
- It was also found that being a senior citizen was not independent of churn
- Among elderly people, those with tech support were much less likely to churn than those without

## Recommendations
- Surveys to find out why the fiber customers, and month-to-month customers are churning at a higher rate than other groups
- Offer discount for first 3 months of service for new month-to-month customers
- Offer a discount on tech support services for our elderly customers which is correlated with less churn