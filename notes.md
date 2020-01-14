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
