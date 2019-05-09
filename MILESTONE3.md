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

**Description**

In our first use case we have asked user to provide us a valid Github Repository URL so that we can get that URL, then do some string manipulation on that, so as to get Owner and Repo Name from that URL. If the URL is not a valid URL then an error message is shown saying its not a valid url. Now we would recursively get all the '.java' extension files using the REST API. Now as we receive the file, simultaneously we start scraping the data inside the file with all are metrics required for visualzation. We have also shown a progress bar to track the status of all the files being fetched. As soon as the user enters the Repository url and clicks the submit button, he would be able to see all the files that are being fetched using the github rest api beneath the progress bar. Now if the user entered a repository which is not public then an access token is also provided along with the url to fetch all the files. In our portal we are only visualizing Java code. 


### Use-Case 2: Choose a Metric

1.  **Preconditions:** The code from the REST API is successfully received.

2.  **Main Flow**: After successfully getting the repository, user will be asked to choose an option[S2] from the given set of choices[S1], i.e. the different metrics available to evaluate the code. After selecting their desired metrics the corresponding visualizations are displayed[S3].

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] The user is presented with a menu of different Code Quality Metrics for which visualisations can be generated.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] The user selects metrics which they wish to analyze.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user is then redirected to a page where the corresponding graphs and visualisations are shown to the user.

4.  **Alternate Flows:** If retreiving repository data or metric processing fails completely or partially then the user is alerted.

**Description**

In our second use case, we are assuming that our first use case is passed and we are recursively receiving all the java files of the github repositry entered by the user. Simultaneously we start parsing the code of the file received. We have made a class which will store all the classes metric attributes received in the files like Total methods in a class, Total comments per class, Lines of code per class, Cyclomatic complexity per class, Parents off all the class. For the overall project we have computed Total collaborators and Major collaborator. Now we will simultaneouly populate our database as soon as we keep getting the files and parse it. We have implemented out own logic from scratch to find total comments in the class, total methods in the class, lines of code for the class and finding the parents of every class. We have used Github Rest Api to get the total collaborators of the project and major collaborator of the project. When all the files are parsed the SQL database is formed with all the classes encountered. Now this database can be directly taken by the tableau serverfor visualization of the metrics. Now after the visualization is done on the dashboard, these dashboards are embedded on the final web page of our portal showcasing all the visualizations.


### Use-Case 3: Evaluate Complexity of the Code 

1.  **Preconditions:** The repository data from the Github API is successfully received.

2.  **Main Flow:** After successfully getting the repository, user selects metrics related to code complexity [S1] from options provided on the portal [S2]. The user can then view the graphs and visualisations presented based on the metrics they selected and derive information related to the complexity of their code [S3].

3.  **Subflows:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S1\] User selects the options they need for checking the complexity of the code.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S2\] In this case user chooses cyclomatic complexity, number of lines of code and class hierarchy level as the metrics they want to visualise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \[S3\] The user can then view the visualisations of these parameters with respect to the repository code received from Github.

4.  **Alternative Flow**: The user doesn’t select any option and nothing happens.

**Description**

Our third use case is a specific type of second use case. In this we are specifically visualizing the complexity of the code. The metrics that can be majorly used are the Cyclomatic complexity of the class, Lines of code and total methods inside the class. For finding lines of code and total methods inside the class, we have implemented our own logic from scratch. While for finding cyclomatic complexity we have used an inbuilt python library, lizard, that will find the cyclomatic complexity of all the classes within a file. As soon as we find these above metrices we populate this in our database. Now after that database will be populated, we will form the visualizations using tableau and embed those dashboards in our final webpage of our portal.


# Task Tracking
[Worksheet](https://github.ncsu.edu/umisra/csc510-project/blob/master/WORKSHEET.md)

# Screencast

[Project ScreenCast - GitHub Link](https://github.ncsu.edu/umisra/csc510-project/blob/master/Screencast%20-%20Milestone%203.mp4)
</br>OR</br>
[Project ScreenCast - Google Drive Link](https://drive.google.com/file/d/1pffZ40t8k5bTkDbwipd1G0ttnYKuPbLw/view?usp=sharing)
