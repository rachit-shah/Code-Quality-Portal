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


# Mocking

We are using MySQL for out database which will have two tables:
1.  Metric by Files
2.  Metric by Project

The first table consists of columns corresponding to each metric which relate to a particular class and file. It will store metrics such as number of methods, parent (to visualize class hierarchy level), coupling (to visualize number of non-inherited classes) and lines of code for each class name and their corresponding file name with timestamps. We can then visualize these metrics in Tableau by grouping on class name, file name or timestamps to the user.

The Second table consists of metrics which relate to the project as a whole. It will have metrics like cyclomatic complexity and average number of faults over test runs with timestamps which correspond to the whole project. We can visualize how these metrics have changed over time in Tableau using timestamps. 

**Table 1 (Metrics by Files)**

<img src="/images/MetricByFiles.png" alt="drawing" width="600"/>

**Table 2 (Metrics by Project)**

<img src="/images/MetricByProject.png" alt="drawing" width="600"/>

In order to mock data for this milestone we have written a python script, stored in the file sql_db.py, that is called by the server to populate the MySQL database. First a connection is made to the database using mysql-connector-python. Then our tables are creating and populated with mock data. To give a good representation of our portal and to aid our visualisations we have chosen to create this data based on an example object-oriented bank system. This system includes 4 different files of code and 24 classes with multiple hierarchy levels. The mock data represents the state of the codebase at 5 different timestamps spread over 3 years (with 6 months in between each timestamp). In order to simulate a realistic reperesentation of a big project over time we have generated 170 rows of timestamped data in total. This allows the user to interact with the visualisations and view the evolution of their codebase with time. 

# Bot/Portal Implementation

Our portal implementation so far is merged onto the branch 'flask_web_app'.

To implement our Code Quality Visualization portal we have created an application using Flask which is a python framework. This application is currently hosted on our local server and will be what we deploy on the deployment server. As of now this app communicates only with the frontend. It will eventually get data from Github's APIs and process it in order generate our  visualisations. Since we haven't yet connected to Github's APIs, our server code is minimum and so we haven't yet implemented any design patterns.

Currently we have prepared a complete mockup of our intended portal. The frontend of the application, written in HTML with CSS and jQuery, allows the user to enter a mock URL from which data is supposed to be fetched. As of now we running a script to populate the MySQL database with mock data once user enters the URL. We are then using Tableau to visualise this data. Tableau directly connects to the MySQL server and generates these visualisations. We have then published the visualisations on Tableau's public server. Once the mock data is inserted into the database, the user is given a choice to select the metrics they wish to view. The frontend then fetches those specific metric dashboards from Tableau's public server and embeds it for the user to view and interact with within the portal itself.

In order to visualise the quality metrics that we have assessed from the code, we have generated multiple visualizations such as Tree Maps, Horizontal and Vertical Bars, Packed Bubbles, Line Chart, etc. We have also implemented filters based on attributes like time stamp, class name, file names, etc. in order to dynamically change the data used to visualize a chart and see a subset of the visualization. For example, if the user only wants to see  data from a specific file or a specific time, they can just choose the filter and visualize it accordingly.

# Task Tracking
[Worksheet](https://github.ncsu.edu/umisra/csc510-project/blob/master/WORKSHEET.md)

# Screencast

[Project ScreenCast - GitHub Link](https://github.ncsu.edu/umisra/csc510-project/blob/master/Screencast%20-%20Milestone%202.mp4)
</br>OR</br>
[Project ScreenCast - Google Drive Link](https://drive.google.com/file/d/14GGw0kaulehem9Zq_Z-SG6WvORE2AU8f/view?usp=sharing)
