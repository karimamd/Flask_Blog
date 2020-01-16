* __ name __ is name of module in python , basically tell python where to look for things
* Flask routes are website pages website.com/route
* before running app : export FLASK_APP=flaskblog.py (file name), no spaces
then flask run
* export FLASK_ENV=development makes changes in real time to localhost without needing to rerun flask
OR export FLASK_DEBUG=1
* the link is equivalent to localhost:post_no
* can return direct HTML tfrom decorator functions and it will get rendered automatically

* can add

if __name__ =='__main__':
    app.run(debug=True)

to run the app using python by running the main file however, using flask run enables using flask shell for debuging

* running with python is better in the case of not needing to set environment variables each time terminal is shut

* if wanted multiple pages ? routes to use the same function just add all the decorators before the function

* all functions in file must use different names

* can return '''Large multiline html''' but can get messy very soon
so we use templates and create a templates folder to put them in it, templates are files containing all html we want to render and usually is dynamic templates which change HTML based on conditions

* can get any page source html from browser

* can pass variables to rendered html templates simply by adding arguments to render_template with our desired name and we can access those variables in html files

* Flask uses Jinja 2 for templating engine

* can use for loops bu open blocks and close by endfor blocks

* blocks are between 2 curly braces {% for post in posts%} while variables are in four {{post.title}} and we can use dot operator inside to access object attributes

* can use if conditionals in Jinja in HTML so that we base condition off of passed variables
{% if variable_name %} -> means if variable has a value i.e. passed

* can use template inheritance in Jinja to avoid repeating html code between multiple files

We put all common code between all files in a template file lets call it layout.html and put blocks in it in places of different code
{% block block_name%} {% endblock block_name%}

no need to write block_name in endblock but this is cleaner

In shared files add {% extends "layout.html" %} and then define blocks with the same name of layout to replace them

* there is a flask extension to bootstrap called flask bootstrap, but using normal bootstrap may be more flexible

* in order to start using bootstrap we copied meta tags in bootstrap docs and put them along with bootstrap css include tag <link> and put them in <head> above title to be able to use bootstrap in layout.html and consequently in all files using it as a template

* also copied the optional <script> JavaScript tags in the bootstrap docs above the closing body tag

* to test that these were working we put the blocks inside a div with a container class which is a class in bootstrap that is assigned certain visual edits

* the next step would be fixing the UI using bootstrap
for this section code snippets are copied into layout.html template inside the body tag on after the other, one is a navigation bar header and other is side probably
tutorial does not have much details on how to do this things, only focuses on Flask

* url_for flask fn is imported to get the routes for different functions
<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='main.css') }}">
used this to link the css file to the layout file

* *** starting tutorial 3: registration forms

* sign up and login should not be done from scratch because too complicated
* flask wt forms is one famous lib for this
* we put forms in separate py file for clealiness

* lib has validators which put constraints
* DataRequired constrains not having empty fields

* this lib helps build forms easily without repeating validation codes
* There is email validator to check that entered is correct email
* and there are different types of fields corresponding to different data types and fields of a form in general
* the string we pass to fields is the label of the field

* we put a secret key in the app and that should be an env variable at some point
* secret keys are for security protect against forgery and some other stuff

* we user app.config['SECRET_KEY']=''
and generated the key by pythons built in secrets library
import secrets
secrets.token_hex(16)

any long string will work
* to create the form in html template we put div tags and inside them form tags with method= post and action is empty string which means will post to the same url
the class "content-section" given to the div is in css helps look little nicer

* {{form.hidden_tag()}} important to include for security , dont worry much about details but definitly needed

* can give one tag multiple classes separated by space in same quotes
mb-4 means margin botton is 4

* when need to access form variable must be in {{}}
* can give those variables classes but opening braces and putting classes inside
{{form.username.label(class="form-control-label")}}

* we access form variables by their specified variable names in the classes in forms.py

* so we created all field forms inside block that will get replaced in html

* url_for function we pass name of function not name of the route

* if we submit the form now we get Method not Allowed error because we did not specify that our route accept post requests
* @app.route("/register", methods= ['GET', 'POST'])
this solves the problem

* now we need to validate fields before submission
* there is flash in Flask which is a one time flash message
* can specify bootstrap classes to flashes as second argument
* there is redirect fn in flask that we can use to redirect user if data is validated correctly

* must include flash in layout.html in order for it to appear and must chose its place also
