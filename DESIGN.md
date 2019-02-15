# Visualization Of Code Convention and Various Quality Metrics of a Repository

Team 6 Members: folia, rshah25, umisra


## Problem:

In large projects there are a number of developers, sometimes in
different locations, working on the same codebase. This makes the system
highly complex and it becomes difficult to monitor convention and code
quality. It’s also challenging to get a higher level view of the entire
codebase and understand its structure.

If convention and quality aren’t regularly maintained the project can
face losses in terms of productivity of the developers and their ability
to collaborate with each other. Additionally, with increase in
complexity of the project there would be a steep learning curve involved
for any new member of the team.

## Solution Description:

The analytical portal proposed would present a dashboard which includes
the visualization of a number of different code convention and quality
metrics such as:

-   **Class Hierarchy Level:** relation between classes (parents and
    their children).

-   **Number of Methods per Class**: total methods present in a class
    (recommended to be less than 20).

-   **Cyclomatic Complexity**: number of linearly independent paths in
    the code.

-   **Coupling between Objects**: number of non-inherited classes a
    target class depends on.

-   **Comments/Documentation**: check if files have required comments.

-   **Lines of Code:** length of each file.

-   **Average Number of Faults Detected over Test:** the number of
    faults detected on test runs of different modules.

-   **Number of Collaborators for a file:** number of developers that
    have worked or are working on a particular file.

The user will provide the link for the repository to assess and an
access token if it is private. We will then mine the repository for code
using web scraping tools and evaluate the aforementioned metrics. The
user can then choose which metrics he wants to see, which will be
displayed on the Portal by embedding the corresponding metric visualized
in Tableau.

The members of the team would have access to this portal and would be
able to view visualizations of the different metrics and observe if any
particular area of the codebase is not efficiently maintained. There’s
also information regarding which developers work on each file and thus
enables accountability and promotes following of convention.
Furthermore, there are metrics tracking the structure of the project and
thus it is easier for new members and managers to understand the code
and workflow.

The tools we are going to use for this project: Beautiful Soup (for Web
Scraping), Python (to process data), Tableau (to visualize), HTML/CSS
(for Portal front-end).


## Use Cases:

### Use-Case 1: Initialize environment

1.  **Preconditions :** It must have a valid address to the particular
    repository. The repository must exist at the provided URL. If the
    repository is private, the user must also provide an access token.

2.  **Main Flow:**

> A valid address to the repository will be provided and then that
> particular repository would be scraped and our given metrics would be
> applied on it. Further the visualization of the metrics would be done
> in Tableau or Power BI and shown to the user by embedding it in our
> Portal.

1.  **Subflows**:

> \[S1\] User provides a valid repository address
>
> \[S2\] Repository is scraped for its code from that address and
> Analysis is further done to measure our code quality metrics.
>
> \[S3\] Visualization would be done in Tableau or Power BI for the
> analysis.
>
> \[S4\] Visualization is shown to the user by embedding the
> graph/visual in our portal.

4.  **Alternate Flows**: If the repository doesn’t exist or it’s private
    without correct access token, the web scraper would return 404 Not
    Found and prompt the user to enter again.

### Use-Case 2: Choose a Metric

1.  **Preconditions:** The web scraping from use case 1 is successfully
    done.

2.  **Main Flow**: After the successful scraping of the repository, user
    would be allowed to choose an option from the given set of choices
    that are the different metrics of the available to evaluate the
    code.

3.  **Subflows:**

> \[S1\] A menu of available Code Quality Metrics is shown to the user
> to pick from and evaluate the code.
>
> \[S2\] The user picks an option.
>
> \[S3\] The corresponding graph and/or description is shown to the
> user.

4.  **Alternate Flows:** If the user does not select any option for the
    metric and submit, then alert user.

### Use-Case 3: Evaluate Complexity of the Code

1.  **Preconditions:** The web scraping from use case 1 is successfully
    done.

2.  **Main Flow:** After successfully scraping the repository, user
    would be able to check the complexity of the code by evaluating the
    graphs of cyclomatic complexity, number of lines of code and class
    hierarchy level. The portal will also provide sections of code which
    contribute most to each of these metrics for the Project Manager to
    evaluate which parts of code needs to be simplified for a new user
    to understand.

3.  **Subflows:**

> \[S1\] Option would be given for the user to check the complexity of
> the code
>
> \[S2\] User selects the option
>
> \[S3\] Complexity of the code would be provided by visualizing the
> complexity metrics Cyclomatic Complexity, Line of code and Class
> hierarchy Level.
>
> \[S4\] The sections of the code would be indicated which contributes
> most to each of these metrics’ complexity.

4.  **Alternative Flow**: The user doesn’t select the option and nothing
    happens.

## Design Sketches:

### Wireframes
![Wireframe 1](/images/wireframe-1.png)

Design Sketches 

Wireframes: 

 

 

 

 

 

Architectural Diagram 

 

 

HTML/CSS Frontend: 
This component is the frontend of the Portal that the user will interact with. The user will provide repository details to this component and after the metrics data is collected, the visualizations are displayed on the frontend and the user can view and interact with it 

Python Application: 
This has two main components: 
1) Beautifulsoup Library:  
This library is used for web scraping (web data extracting or web data harvesting) from websites. Once the application receives the repository link, it uses this library to scrape the given Github repository. It extracts the code present in the repository and passes it on to the data processing component. 
2) Data Processing:  
When data is returned form the Beautifulsoup library it needs to be further processed. The library will simply return the code from the repositories, then the data processing component parses the code files and extracts the required data to generate the metrics. It stores this data in the MySQL database. 
Additionally, when the user wants to view information on particular metrics then the data processing component extracts the required data from the database and uses the Tableau tool to generate visualizations on the data and returns it to the fronted for the user to view. 

Database Component: 
The MySQL database schema is tentatively planned as shown in Table 1 and 2, just to show an idea about how we are going to store the metrics data in a database and consequently use them for Tableau visualization. The first table consists of columns corresponding to each metric which relate to a particular class and file, while the second table consists of metrics which relate to the project as a whole. The first table will store metrics such as number of methods, list of children (to visualize class hierarchy level), coupling (to visualize number of non-inherited classes) and lines of code for each class name and their corresponding file name with timestamps. We can then visualize these metrics in Tableau by grouping on class name, file name or timestamps to the user. The second table consists of metrics like cyclomatic complexity and average number of faults over test runs with timestamps which correspond to the whole project. We can visualize how these metrics have changed over time in Tableau using timestamps.  

 

 

 

Table 1 (Metrics by Files) 

Column Name 

Data Type 

Description 

ID 

Integer 

Primary Key 

Time Stamp 

Time 

Date the row is added 

Class Name 

Varchar 

Name of class whose data is in the row 

Number of Methods 

Integer 

Number of methods in class 

File Name 

Varchar 

File name in which class is present 

Children 

Varchar 

List of child classes 

Coupling 

Integer 

List of classes whose objects are used without inheritance 

Line of Code 

Integer 

Number of lines of code in class 

 

 

Table 2 (Metrics by Project)  

Column Name 

Data Type 

Description 

ID 

Integer 

Primary Key 

Time Stamp 

Time 

Date the row is added 

Cyclomatic Complexity 

Integer 

Number of linearly independent paths in the code 

Fault Detection Per Test 

Integer 

Number of faults detected per test run of the code 

 

 

Github Repositories: 
This component represents the repositories on Github that the user wishes to obtain metrics about. The Beautifulsoup library will extract data from the desired Github repository present in this component 

 

Tableau (Data visualization): 
Tableau is a business intelligence tool that helps visually analyze data. It creates interactive visualizations that users can. When the user requires data of certain metrics the data processing component uses this tool to generate the desired graphs and charts. Then this is embedded into the HTML/CSS frontend and the user is able to interact with the Tableau visualizations within the frontend itself. 

 

A detailed description of the interaction between the components can be seen the diagrams below 

 

The home screen of the application appears as soon as user opens it. From there user has to provide the repository address and token to access it. The token should be legit and the repository address should be correct, else the error would be shown. After successfully getting the repository, it is fully scraped and then stored in the Database. After successfully stored in the database, success response is returned to the application and then the browser shows the next page to the user. From the next page the user selects the metrics and submit that form. 

 

 

After the Initialization phase, the user is shown a new page to choose all the metrics he want to visualize it. User selects the metric and submit it to the browser. The python application fetches data from database and request Tableau for the visualization of the metrics. The visualized data is then forwarded to the browser from where user can see and further visualize it. 



