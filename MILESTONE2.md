# Use Cases

### Use-Case 1: User's First Visit

1.  **Preconditions :** The user provides a valid address to an existing repository. 

2.  **Main Flow:** The user provides a valid address to the repository[S1] and then the system will assess the provided repository by using[S2] Github REST API to fetch the code and applying the quality metrics on the data. Further the visualization of the metrics would be done in Tableau or Power BI[S3] and shown to the user by embedding it in the Portal[S4].  

1.  **Subflows**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] User will give a link to an existing Github repository. If the repository is private, the user must provide an access token.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] The Github REST API is used to get code from that address and analysis is further done to measure our code quality metrics.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The data returned is processed and stored in a database and used to generate visualizations which would be done in Tableau or Power BI for the user's analysis.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S4\] The visualizations are prepared to be shown to the user by embedding the graph/visual in our portal.

4.  **Alternate Flows**: At any moment of analysis, if the system is not able to get the data, get the access to the resources or any tool fails while assessing which would be required for the analysis, an alert specifying the error would be shown to the user.

### Use-Case 2: Choose a Metric

1.  **Preconditions:** The code from the REST API is successfully
    received.

2.  **Main Flow**: After the successful getting of the repository, user
    would be allowed to choose an option[S2] from the given set of choices[S1],
    that are the different metrics available to evaluate the
    code. After selecting the options the corresponding visualizations would be shown[S3].

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] The user is presented with a menu of different Code Quality Metrics for which visualisations can be generated.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] The user selects metrics which they wish to analyze.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user is then redirected to a page where the corresponding graphs and visualisations are shown to the user.

4.  **Alternate Flows:** If the web scraping or the processing of metric fails completely or partially then alert the user.

### Use-Case 3: Evaluate Complexity of the Code **

1.  **Preconditions:** The Repository data from the Github API is successfully
    received. The user has selected to view data on cyclomatic complexity, number of lines of code and class
    hierarchy level.

2.  **Main Flow:** After successfully getting the repository, user
    would be able to check the complexity of the code by evaluating the
    graphs of cyclomatic complexity, number of lines of code and class
    hierarchy level[S1][S3] by selecting the suitable options[S2]. The portal will also provide sections of code which
    contribute most to each of these metrics[S4] for the Project Manager to
    evaluate which parts of code needs to be simplified for a new user
    to understand.

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] User selects the options they need for checking the complexity of the code.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] in this case user chooses cyclomatic complexity, number of lines of code and class hierarchy level as the metrics they want to visualise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user can then view the visualisations of these parameters with respect to the repository code received from Github.

4.  **Alternative Flow**: The user doesn’t select the option and nothing
    happens.


# Mocking

First of all we are using MYSQL for out database. The Database will have 2 tables:
1.  Metric by Files
2.  Metric by Project

The first table consists of columns corresponding to each metric which relate to a particular class and file. It will store metrics such as number of methods, parent (to visualize class hierarchy level), coupling (to visualize number of non-inherited classes) and lines of code for each class name and their corresponding file name with timestamps. We can then visualize these metrics in Tableau by grouping on class name, file name or timestamps to the user.

The Second table consists of metrics which relate to the project as a whole. It will have metrics like cyclomatic complexity and average number of faults over test runs with timestamps which correspond to the whole project. We can visualize how these metrics have changed over time in Tableau using timestamps. 

**Table 1 (Metrics by Files)**

<img src="/images/MetricByFiles.png" alt="drawing" width="600"/>

**Table 2 (Metrics by Project)**

<img src="/images/MetricByProject.png" alt="drawing" width="600"/>

Now for mocking the data, we used python to connect with MYSQL. We wrote down the scripts in python to insert data into MYSQL Database. We first connceted the SQL server using connector. We created tables and inserted that data using python scripts. The file namely sql_db.py is used for it and its also pushed in our github repository.

# Bot/Portal Implementation

# Task Tracking

# Screencast
