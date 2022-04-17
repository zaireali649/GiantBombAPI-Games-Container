# GiantBombAPI-Games-Container

This was a take home assignment for a Machine Learning Engineer interview at a Fortune 500 company. At the time, I completed this to the best of my ability. Can't say if the container portion is correct. This is on my backlog to fix the container if necessary and deploy to AWS. I will also supply a cloudformation template to do this in the future. 

Simple API
Create a simple service to query a video game database with a search string entered by a user on a website or via an HTTP request (using curl or some other method). For example, you may choose to use the Giant Bomb API (register for an API key at http://www.giantbomb.com/api/), where an example HTTP request for game search would be:
http://www.giantbomb.com/api/search/?api_key=[API_KEY]&format=json&query="[SEARCH_TERM]"&resources=game

Some points to consider,
1) The service should run in a container preferrably deployable to AWS.
2) Extra bonus points will be given for services written in Python (our preferred language on the Data Science Team).
3) The service can either have a web page as a front end to take input from the user or exposing an API endpoint to calls via HTTP request.
4) The code design and functionality of the service is important (do not spend too much time on the User Interface).
