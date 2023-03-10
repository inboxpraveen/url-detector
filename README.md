# URL Detector - Phishing Vs Safe URL Predictor using Machine Learning

This repo contains the model design and definition of a url being Phishing (Malicious) or Safe (Legitimate) for you to visit. Alongside the model design, It also will help you lay foundation to hosting it as a complete project rather than just an technical directory. The model design can also be used for submission of SimpliLearn Deep Learning Cyber Security project.

### Notable Links

[1. URL Detector Hosted Demo](https://urldetector.deta.dev/)

[2. Complete Explanation - Part 1 - Understanding Model and Training]()

[3. Complete Explanation - Part 2 - Understanding Hosting and Demo]()

<!-- ## Project Task: Week 1
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

After removal of useless and less coordinating features, the final features are:

['having_IPhaving_IP_Address', 'URLURL_Length', 'Shortining_Service','having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain', 'SSLfinal_State','Domain_registeration_length', 'Favicon', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL','age_of_domain', 'DNSRecord', 'web_traffic', 'Google_Index','Statistical_report', 'Result']


## Hosting

Our next step is to do hosting on a free cloud service.

Since this is a small project which does not require any large memory dependencies, we can use any cloud service out there.

So, I am choosing [Deta]() as this provides free lifetime service.

#### Initial Steps

1. our first goal is to make sure you have deta installed on your local system. To do so, just follow any one the following instructions based on your operating system.

1.1 Installing deta on Windows
    - Open your windows powershell with admin
    - Enter the command without quotes - "iwr https://get.deta.dev/cli.ps1 -useb | iex"

1.2 Installing deta on Linux
    - Open your Terminal
    - Enter the command without quotes - "curl -fsSL https://get.deta.dev/cli.sh | sh"
    - If you get error saying no package curl, then run this command - "sudo apt-get install curl" and then repeat the previous step again.

1.3 Installing deta on Mac
    - Open your Terminal
    - Enter the command without quotes - "curl -fsSL https://get.deta.dev/cli.sh | sh"

After this, we need to login to deta using the following command:
    deta login

this will open up a web browser page where you should login and it will redirect you back to your command/terminal saying you have been logged in successfully. -->