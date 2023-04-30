# Online-Shop
Represents online shop.
# Versions:
* Django 3.2.16
* Python 3.8.8

# Encountered problems and difficulties (and some history of development):

#### 1. How to render your own form with additionals styles.css, using Django`s {{ form }} ? ( Form class - WordForm ) 
* In documentation, found attribute for my WordForm class named "template_name". Allows to render your own template. Good. Tried. Did`t work. Checking futher. Damn: 
<br> ![image](https://user-images.githubusercontent.com/67171139/215750421-7b9cd883-48b9-43a9-81c2-a112d290743d.png)
<br> My Django is too archaic... Two ways out - rebuild all project with Django4, or find other ways. Searching... <br> 
* Okey, found out that is possible to change Django version on latest without any critical conflicts - fixing some and...We have opportunities to create and configure our own forms by template_name in Form_Class. Sehr gut!
![image](https://user-images.githubusercontent.com/67171139/217643425-6316415f-43cd-426d-9e65-a0064500a15c.png)


#### 2. How  to look after unlogged users?
* Django gives 2 ways (may be more) - a) Use @login_required decorator and - b) Use self-made page and check if user logged in. <br>
* 1st way will redirect us directly to the logging in page without any hints, then - to required page.
* 2nd way draw such a url-rote: requiered_page ->  u_a_not_loggedin_page - > login_page -> requiered_page. <br>
As a developer, I prefer just use a decorator and forget about difficulties. But as a ordinary user - I prefer 2nd way - more user-friendly and clearly behaviour. <br>
User is always right :)
