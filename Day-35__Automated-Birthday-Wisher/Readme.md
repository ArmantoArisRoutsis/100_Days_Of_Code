## 100 Days Of Code With Python

# Day 35

## Automated Birthday Wisher

### About This Project

#### The user can input the information of people he wants to wish for their birthday into a new csv file or the already provided "birthdays.csv" file. The application will use the datetime module to get the current date. Then using the pandas library it will read the csv file and get hold of each row and determine if the current date matches any of the days of the rows. If there is a match then the app will randomly choose one of the birthday letter templates(located in the "letter_templates" folder). It will replace the "[NAME]" string in the template letter with the name of the person who's birthday matched the current date. Finally an email will be sent using the smtplib module to their address. You can view this application live by clicking [this link.](https://repl.it/@ArisRoutsis/Automated-Birthday-Wisher#main.py)

### Technologies Used

- ##### Python 3
- ##### Pandas
- ##### datetime
- ##### smtplib
