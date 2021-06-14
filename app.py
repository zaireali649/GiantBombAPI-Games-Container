#%%

# =============================================================================
# Create a simple service to query a video game database with a search string entered by a user on a website or 
# via an HTTP request (using curl or some other method). For example, you may choose to use the Giant Bomb API 
# (register for an API key at http://www.giantbomb.com/api/), where an example HTTP request for game search would be:
# http://www.giantbomb.com/api/search/?api_key=[API_KEY]&format=json&query="[SEARCH _TERM]"&resources=game
# Some points to consider,
# 1.	The service should run in a container preferrably deployable to AWS.
# 2.	Extra bonus points will be given for services written in Python (our preferred language on the Data Science Team).
# 3.	The service can either have a web page as a front end to take input from the user or exposing an API endpoint 
#       to calls via HTTP request.
# 4.	The code design and functionality of the service is important (do not spend too much time on the User Interface).
# =============================================================================

#%%

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = ""

@app.route('/')
def home():
    html = """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Search games</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    </head>
    <script>
    function myFunction() {
    var search= $('#search').val();
      $.ajax({
                  url: "/search",
                  type: "POST",
                  data: {search:search}
              }).done(function(response) {
                var html = "<br><br><br><p> <b> RESULT : <b><p>";
                response = JSON.parse(response.response);
                $(".show-data").text(JSON.stringify(response, undefined, 4));
                });
        };
      </script>
    <body>
        <p>
            Enter Game Name<br><br>
                <input type="text" id="search" name="search"><br><br>
                <button id="clicked" onclick="myFunction()">Submit</button>
            </p>
        Response:
        <pre class="show-data" style="display: inline-block; border:2px solid Black;" >
        </pre>
    </body>
    </html>
    """
    
    return html

@app.route('/search', methods=['GET','POST'])
def my_form_post():
    search = request.form['search']

    url = "https://www.giantbomb.com/api/search/?api_key={}&format=json&query={}&resources=game".format(API_KEY, search)

    headers = {
        'Cookie': 'device_view=full',
        'User-Agent': 'PostmanRuntime/7.26.8'
    }

    response = requests.request("GET", url, headers=headers, data={})
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
	app.run()