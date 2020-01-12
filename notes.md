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
