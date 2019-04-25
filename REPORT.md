# Screencast

[Project ScreenCast - GitHub Link](https://github.ncsu.edu/umisra/csc510-project/blob/master/final-final-screencast.mp4)
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

# Limitations

Currently our project only evaluates Metrics for Java code in github repositories. In the future it can be expanded to include more programming languages to gain the ability to study a larger range of projects on github. 

In the future, we could also add more metrics like Duplicate Code, Dead Code, Unneccessary Conditional Statements, Unneccessary Variables and Methods etc. to get a better overview of the quality of the code.


 
