#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""
OneTime Information Provider
Share files/text-snippets via self-destructing links
"""

#{{{ Imports
from flask import Flask, render_template, request, redirect, url_for
import logging
from logging import Formatter, FileHandler
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
import os
#}}}

#{{{ Application config
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
#}}}

#{{{ Oti Class - Creates the id and encrypts the information
class Oti(db.Model):
	"""
	Class that creates an Oti
	"""
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.LargeBinary)
	pub_date = db.Column(db.DateTime)
	del_date = db.Column(db.DateTime)

	def __init__(self, content, del_date):
		self.content = bytes(content, 'UTF-8')
		self.pub_date = datetime.datetime.utcnow()
		self.del_date = self.pub_date + datetime.timedelta(seconds=int(del_date))

#}}}

#{{{ Pages class
class pages():
	"""
	The pages class contains the webpages that are rendered
	"""
	@app.route('/', methods = ['GET', 'POST'])
	def new_oti():
		"""
		This lets you create a new oti
		"""
		if request.method == 'GET':
			return render_template('new_oti.html')
		elif request.method == 'POST':
			oti = Oti(request.form['content'], request.form['del_date'])
			db.session.add(oti)
			db.session.commit()
			return redirect(url_for('show_oti', oti_id=oti.id))

	@app.route('/<int:oti_id>', methods = ['GET'])
	def show_oti(oti_id,encryption_key=None):
		"""
		Presents the oti
		"""
		oti = Oti.query.get_or_404(oti_id)
		return render_template('oti_created.html', oti=oti)
#}}}

# Run the application
if __name__ == '__main__':
	app.run()
# vim: tabstop=4 noexpandtab shiftwidth=4 softtabstop=4
