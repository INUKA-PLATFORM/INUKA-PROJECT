# KickOutHunger

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#installation-requirements)
+ [Technology Used](#technologies-used)
+ [License](#license)
+ [Contributors Info](#contributors-info)

## Description
Kick Out Hunger is an organization that is aimed at ending Campus Hunger. We recognize that due to the prevailing hard economic times a lot of students in Universities  are going without daily consistent meals. This misfortune has led to students performing poorly or dropping out of school. 

- Kenyan university students face significant food security challenges, with many struggling to afford nutritious meals due to high tuition fees and living expenses. 

- This financial strain often forces students to skip meals or rely on inadequate, low-cost food options. The lack of consistent access to healthy food affects their academic performance and overall well-being. 

- Addressing this issue is crucial to ensuring that students can focus on their studies and achieve their full potential.

## User Stories

Student Can :-

* Register in the application.
* Login to the application.
* Use a financial Wallet to pay for meals.


Admin can :-
* Activate student accounts and send mail/notifications.
* Add users .
* Generate reports.


[Back to Top](#kickouthunger)

**Registration**
- Capturing of student details.

![Registration](./authentication/static/images/register.png)


**Login**
- After account activation student can login.

![Registration](./authentication/static/images/login.png)

[Back to Top](#kickouthunger)

## Behaviour Driven Development
| Behaviour | Input | Output |
| ---------------- | --------------- | ------------------ |
| Application starts | **On page load** | User get to see the home page where it describes the organization details including mission and vision, and user can navigate to various sections. User can also donate but for student users who want to benefit from the program they click on `Join us Link`. Here they can `Register` or `Login` |
| Registration| **Registration page** | The registration page has a register form for new users(students)  to register to the application and are redirected to login |
| Button click | **Donate** | Upon clicking Donate button a donor is able to fill in the information and enter amount to donate.The process is easy and seamless|
| Forms | **Form filling** | User gets to fill in various forms, and depending on various tasks the form are meant for, upon submission the act is done e.g for login on form submission users(Students) is redirected to their wallet|

[Back to Top](#kickouthunger)

## Installation Requirements

### Prerequisites

- Django
- Pip & Python
- Postgres Database/ MySql Database.
- Gunicorn
## Instructions
   
##### Clone Repository:  
 ```bash 
git clone https://github.com/INUKA-PLATFORM/INUKA-PROJECT.git
```
##### Install and activate Virtual Environment virtual  
 ```bash 
cd <projectname> && python3 -m venv <virtualenvironmentname> && source <virtualenvironmentname>/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate

 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py runserver 

 or
 ./manage.py runserver
```
##### Test Application  
 ```bash 
 python manage.py test <appname>
```
Open the application on your browser `127.0.0.1:8000`.  

[Back to Top](#kickouthunger)

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE)

## Live Site

## Contributor's Info

  
 :email: [Martyn Musembi](mweumartin@gmail.com)  

 :email: [Solomon Wainaina](wainainasolomonfx@gmail.com)  

 :email: [Balala](balalasheikh@gmail.com)  

 :email: [David Nanjila](nanjiladavid2@gmail.com)  

 :email: [Vivian Obino](vivobino94@gmail.com) 

 :email: [Eunice Kimani](yuniskimani2015@gmail.com)

 :email: [Reuben Kipkemboi](rotichkipkemboireuben@gmail.com)  

[Back to Top](#kickouthunger)
