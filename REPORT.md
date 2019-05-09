# Screencast

[Project ScreenCast - GitHub Link](https://github.ncsu.edu/umisra/csc510-project/blob/master/Final%20Screencast.mp4)
</br>OR</br>
[Project ScreenCast - Google Drive Link](https://drive.google.com/file/d/18UWsL8mPyEsceKI31FQtKaldBlhfmSkB/view?usp=sharing)


# Problem

For any software development project including a team of developers, if the complexity and quality of the project aren’t regularly maintained the team can face losses in terms of productivity of the developers and their ability to collaborate with each other. In large projects there are a number of developers, sometimes in different locations, working on the same codebase. This makes the system highly complex and it becomes difficult to monitor code complexity and quality. It’s also challenging to get a high-level view of the entire codebase and understand its structure. 

In order to solve these issues a manager may wish to oversee all the files involved in the project and monitor their complexity. Additionally, a new member of the team would like to view the hierarchy of the classes and object dependencies. Also, managers may wish to ensure that code is properly commented or documented, and that it is kept short and modular so that it is readable. Thus, we created an analytical portal visualizing these metrics so that team managers and members can easily analyze the code through easy to understand and interactive visualizations.

# Features

Our project evaluates Java code that is available in github repositories. The following metrics are visualised by our project:

<img src="/images/Features.png" alt="drawing" width="750"/>

First we have the 'Total Number of Comments' in every file. This can show you the extent to which each class is documented.

<img src="/images/Comments.png" alt="drawing" width="750"/>

Then we have the 'Total Number of Methods' per class per file. Here you can visualize the size of each class and the modularity of each file in the project.

<img src="/images/Methods.png" alt="drawing" width="750"/>

Then we have the 'Cyclomatic Complexity' per class. A cyclomatic complexity value above 10 is considered inefficient. So after seeing the visualizations you could work on your code to decrease this metric.

<img src="/images/Cyclomatic.png" alt="drawing" width="750"/>

Then we have the 'Total Collaborators' for the project at any given time. The x-axis represents time and the y-axis shows the number of collaborators. The name on the point in the graph is the name of the major collaborator at that particular time.

<img src="/images/Collaborators.png" alt="drawing" width="750"/>

Then we have the 'Total Number of Lines of Code' per class. It givea a good view on the size of each class within the project.

<img src="/images/Lines.png" alt="drawing" width="750"/>

Then we have the 'Class Hierarchy' of all the classes. Parent classes are in the first coloumn and their corresponding child classes are in the second column.

<img src="/images/Hierarchy.png" alt="drawing" width="750"/>

Finally we have the 'Coupling of Objects' of the classes. High coupling is a negative sign with respect to the complexity of the code.

<img src="/images/Coupling.png" alt="drawing" width="750"/>



# Reflection
In retrospect, out of the 8 code metrics which we were going to implement, we couldn't implement "Average No. of Faults Detected Over Time" as we needed to implement automated builds of projects which is an another project in itself. We also had to change the scope of the metric "Number of Collaborators" from a per-file basis to a per-project basis. We had to do this as the GitHub REST Api doesn't provide details about who touched a specific file and the history of it. It only provides information about the collaborators on a project wide basis. Looking back, I think we could implement this metric on a per-file basis if we analyze each of the commits for each user but we didn't get time to implement it later down the stage. Also, while working on "Cyclomatic Complexity" metric we came across a library called "lizard" which not only could analyze the cyclomatic complexity but also the no. of comments, lines of code, methods, etc. for which we had already implemented our own logic. We could have saved time implementing this and could have used the saved time to work on the number of collaborators on per-file basis or any other additional metric. 

We also started out the database with MongoDB, then realized that we needed a paid version of it if we wanted it to sync with Tableau. So we switched to a MySQL server. During deployment, we first considered heroku as it was short and simple to do. However, for deployment on heroku we realized we should have used Flask's internal sqlite database. Hence, we had to deploy on DigitalOcean which had a very painstaking process to deploy with multiple steps. If we had started out the database with Flask's internal DB, we could have deployed it on heroku in a short and simple way.

# Limitations

Currently our project only evaluates Metrics for Java code in github repositories. In the future it can be expanded to include more programming languages to gain the ability to study a larger range of projects on github. 

In the future, we could also add more metrics like Duplicate Code, Dead Code, Unneccessary Conditional Statements, Unneccessary Variables and Methods etc. to get a better overview of the quality of the code.


 
