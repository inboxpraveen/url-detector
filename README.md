# URL Detector - Phishing Vs Safe URL Predictor using Machine Learning

This repo contains the model design and definition of a url being Phishing (Malicious) or Safe (Legitimate) for you to visit. Alongside the model design, It also will help you lay foundation to hosting it as a complete project rather than just an technical directory. The model design can also be used for submission of SimpliLearn Deep Learning Cyber Security project.

### Notable Links

[1. URL Detector Hosted Demo]()

[2. Complete Explanation - Part 1 - Understanding Model]()

[3. Complete Explanation - Part 2 - Understanding Hosting and Demo]()


## Project Task: Week 1
#### Exploratory Data Analysis:

- Each sample has 32 features ranging from -1,0,1. Explore the data using histogram, heatmaps. 

- Determine the number of samples present in the data, unique elements in all the features. 

- Check if there is any null value in any features. 

**Correlation of features and feature selection:**

Next, we have to find if there are any correlated features present in the data. Remove the feature which might be correlated with some threshold.

Top 5 Most correlated features to target feature ->

- having_Sub_Domain              0.298323

- web_traffic                    0.346103

- Prefix_Suffix                  0.348606

- URL_of_Anchor                  0.692935

- SSLfinal_State                 0.714741


Top 5 Least correlated features to target feature ->

- Iframe                        -0.003394

- Favicon                       -0.000280

- popUpWidnow                    0.000086

- RightClick                     0.012653

- Submitting_to_email            0.018249

