# Use Cases

### Use-Case 1: User's First Visit

1.  **Preconditions :** The user provides a valid address to an existing repository. 

2.  **Main Flow:** The user provides a valid address to the repository[S1] and then the system assesses the provided repository by using[S2] Github REST API to fetch the code and applying the quality metrics on the data. Further the visualization of the metrics is done in Tableau [S3] and shown to the user by embedding it in the Portal[S4].  

1.  **Subflows**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] User will give a link to an existing Github repository. If the repository is private, the user must provide an access token.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] The Github REST API is used to get code from that address and analysis is further done to measure the code quality metrics.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The data returned is processed and stored in a database and used to generate visualizations, which will be done in Tableau, for the user's analysis.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S4\] The visualizations are prepared to be shown to the user by embedding the graph/visual in our portal.

4.  **Alternate Flows**: At any moment of analysis, if the system is not able to get the data, or get access to the resources, or any tool required for the analysis fails, an alert specifying the error will be shown to the user.

### Use-Case 2: Choose a Metric

1.  **Preconditions:** The code from the REST API is successfully received.

2.  **Main Flow**: After successfully getting the repository, user will be asked to choose an option[S2] from the given set of choices[S1], i.e. the different metrics available to evaluate the code. After selecting their desired metrics the corresponding visualizations are displayed[S3].

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] The user is presented with a menu of different Code Quality Metrics for which visualisations can be generated.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] The user selects metrics which they wish to analyze.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user is then redirected to a page where the corresponding graphs and visualisations are shown to the user.

4.  **Alternate Flows:** If retreiving repository data or metric processing fails completely or partially then the user is alerted.

### Use-Case 3: Evaluate Complexity of the Code 

1.  **Preconditions:** The repository data from the Github API is successfully received.

2.  **Main Flow:** After successfully getting the repository, user selects metrics related to code complexity [S1] from options provided on the portal [S2]. The user can then view the graphs and visualisations presented based on the metrics they selected and derive information related to the complexity of their code [S3].

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] User selects the options they need for checking the complexity of the code.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] In this case user chooses cyclomatic complexity, number of lines of code and class hierarchy level as the metrics they want to visualise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user can then view the visualisations of these parameters with respect to the repository code received from Github.

4.  **Alternative Flow**: The user doesn’t select any option and nothing happens.

# Task Tracking
[Worksheet]()

# Screencast

[Project ScreenCast - GitHub Link]()
</br>OR</br>
[Project ScreenCast - Google Drive Link]()
