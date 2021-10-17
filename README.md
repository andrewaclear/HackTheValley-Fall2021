# slacker tracker

> author, front-end: *Andrew D'Amario* © October 2021
> 
> back-end: *Aahil Samnani* © October 2021

We chose the [HEALTH ROUTE](https://hackthevalley.io/) ![](static/factions-health.png).

*It will never leave you lacking... if you be slacking, it be tracking... so get hacking!*

Many of us (especially computer science students) suffer from spending too much time on the computer which is very bad for our health. Moreover, we often find ourselves wasting too much time on the computer, gaming or doing something recreational like social media, rather than the work we should be doing... and for some, they work too much and don't take the breaks they should. *slacker tracker* is a Full-stack Web Application that helps you track the amount of time you spend, **working**, **gaming**, and **offline**. Using the optimal ranges (with respect to healthy living) of times we should be spending doing these things every week, *slacker tracker* helps you see if you have a healthy balanced life or not. When you are working on the computer, run the work timer. When you are gaming (recreating on the computer), run the game timer. When you are off the computer (the app is closed), it keeps track of your offline time. Lastly, to make sure you don't cheat, you have an hour leeway of **unallocated** time when you are on your computer (app is open) but haven't started the game or work timer.

If at the end of the week you have spent an acceptable amount of time doing each of these things, your *slacker tracker* score will increase, if not, it will decrease. In this way you have an accountability with your friends in your group who can see how well (or not) you are doing this week, and how high or low your *slacker tracker* score is (how good you have been doing in general). So friends can help each other stay on track and live happier, healthier, and more balanced lives!


##### Front-end

CSS/HTML API for user bubbles, buttons, header, registration page, and the interface elements. [Chart.js](https://www.chartjs.org/) for the bar graphs.

##### Back-end

The backend was implemented using Python, Flask and SQLite. Users can create an account for the app. The app records the user's personal information and screen time in a SQLite database. The use of Flask allows the backend to communicate with the frontend through rendering HTML templates and requesting data from HTML forms.

#### Potential Optimal Ranges per week
- 30 <= work <= 60
- 3 <= game <= 20
- 90 <= offline <= 120
- unallocated_optimal <= 1

### Screenshots

![](static/scrnli_10_17_2021_2-39-03%20AM.png)

![](static/scrnli_10_17_2021_2-39-56%20AM.png)

![](static/scrnli_10_17_2021_2-59-10%20AM.png)


### Running 

1. Clone repository.
2. Install [Python](https://www.python.org/downloads/) if not already.
3. Create a python virtual environment and activate it.
4. Install pip to latest version if not already.
5. Download requirements via `python3 -m pip install -r requirements.txt`
6. Run db_create.py to create a SQLite database to store data generated by the application.
7. Run app via `FLASK_DEBUG=1 flask run`


