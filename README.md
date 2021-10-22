# Anomaly Detection Project

By: Johnathon Smith

Date: Oct 22nd, 2021
***

### Executive Summary
***

__Project Goal__

The goal of this project was to acquire, prepare, and explore Codeup's curriculum access logs in order to answer at least five of the seven questions asked in an email we received.

__Overall Findings__

* The most trafficked lessons are javascript-i for full stack web developers, fundamentals for data science students, and html-css for front end developers.
* The Ceres cohort referred to the javascript lesson far more than the other cohorts in the java full stack web development program.
* Arches referred to javascript-i more than the other cohorts and Kings referred to content way more than the other cohorts in the php full stack web developer program.
* The Darden cohort referred to the Classfication lesson far more than the other cohorts in the data science program.
* There are 20 students that accessed the curriculum less than or equal to 20 times while active.
* These students were mostly java full stack web developers, but three of them were data scientists.
* The most common request was for javascript-i.
* The java full stack web developer graduates are still accessing the spring and javascript-i lessons.
* The php graduates are still accessing the content and javascript-i lessons.
* Data science grads are accessing the fundamentals, sql, and classification lessons.
* The front end grads are mostly accessing the html-css lessons.
* While there are many lessons that only had a few views, some of the most prevalent sections involve regression in excel, and control-structures and promises in javascript.

***

__Deliverables__

* An email containing the answers to the questions that were asked and a presentation-ready slide attached with the same information.
* A Github Repository containing:
    * A clearly labeled final report jupyter notebook.
    * The .py files necessary to reproduce my work.
* Finally, a README.md file documenting my project planning with instructions on how someone could clone and reproduce my project on their own machine. Goals for the project, a data dictionary, and key findings and takeaways should be included.

__Context__

* The Codeup curriculum access logs were obtained from the Codeup database.

__Data Dictionary__

| Feature | Datatype | Definition |
|:--------|:---------|:------------|
| path | object | The original request path |
| user_id | int | An arbitrary number assigned to each unique user |
| cohort | object | The cohort the user belongs to |
| ip | object | The ip address of the network the user made the request from |
| start_date | object | The start date of the user's cohort |
| end_date | object | The end date of the user's cohort |
| program | object | The program the user is/was enrolled in |
| subdomain | object | The focus of the program the user is/was enrolled in |
| year | int | The year the curriculum was accessed |
| month | object | The month the curriculum was accessed |
| day | object | The day of the week the curriculum was accessed |
| hour | int | The hour of the day the curriculum was accessed |
| is_graduate | bool | Indicates whether or not the user is a graduate of Codeup |
| current_student | bool | Indicates whether or not the user is a current student at Codeup |
| request_section | object | The first section of the path string |
| request_subject | object | The second section of the path string |
| request_lesson | object | The third section of the path string |
| param_4 | object | The fourth section of the path string |
| param_5 | object | The fifth section of the path string |
| param_6 | object | The sixth section of the path string |
| param_7 | object | The seventh section of the path string |
| param_8 | object | The eighth section of the path string |

***

### My Process

* Write a README.md file that details my process, my findings, and instructions on how to recreate my project.
* Acquire the Codeup Curriculum access logs from the Codeup database.
* Clean and prepare the access log data:
    * Added information for the student's program
    * Created columns for access year, month, day, and hour
    * Created columns that identify each user as graduates or current students
    * Split the path string along each '/' character for easier exploration.
    * Drop unnecessary columns.
    * Finally, convert the date column to a datetime object and set it as the index.
* There will be no modeling for this project, so I will not split the data into train, validate, and test before exploration.
* Explore the data and look for anomalous behavior or events.
* Document conclusions, takeaways, and next steps in the Final Report Notebook.

***

##### Plan -> Acquire / Prepare
* Create and store functions needed to acquire and prepare the Codeup curriculum access log data in a wrangle.py file.
* Import the wrangle.py module and use it to acquire the data in the Final Report Notebook.
* Complete some initial data summarization (`.info()`, `.describe()`, ...).
* List key takeaways.

***

##### Plan -> Acquire / Prepare -> Explore
* Create visuals that will help discover anomalous behavior or events.
* Answer the questions asked.
* List key takeaways.

***

### Reproduce My Project

***

- [x] Read this README.md
- [ ] Download the final report Jupyter notebook.
- [ ] Download the wrangle.py module into your working directory.
- [ ] Ensure your own env.py file is in your working directory.
- [ ] Run the final report Jupyter notebook.