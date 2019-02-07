Topic: Visualization Of Code Convention and Various Quality Metrics of a
Repository

Team 6 Members: folia, rshah25, umisra

Problem**:**

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

Solution Description:
=====================

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

\
Use Cases:
==========

Use-Case 1: Initialize environment
==================================

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

1.  **Alternate Flows**: If the repository doesn’t exist or it’s private
    without correct access token, the web scraper would return 404 Not
    Found and prompt the user to enter again.

Use-Case 2: Choose a Metric

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

1.  **Alternate Flows:** If the user does not select any option for the
    metric and submit, then alert user.

Use-Case 3: Evaluate Complexity of the Code
===========================================

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

1.  **Alternative Flow**: The user doesn’t select the option and nothing
    happens.


