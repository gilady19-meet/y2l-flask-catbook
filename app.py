from flask import Flask, request
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:num>')
def catbook_catpage(num):
	c=get_all_cats()
	for i in c:
		if i.id==num:
			name=i.name
	return render_template("cat.html" , n=num , name=name)


@app.route('/addcat' , methods=['GET', 'POST'])
def addcat():
	if request.method == 'GET':
	    return render_template('form.html')
	else:
	    name = request.form['firstname']
	    create_cat(name)       
	    return render_template('response.html',n = name)

	




if __name__ == '__main__':
   app.run(debug = True)
