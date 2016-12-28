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
from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
import os
#}}}

#{{{ Application config
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#}}}

#{{{ Oti Class - Creates the id and encrypts the information
class Oti(db.Model):
	"""
	The oti class creates the oti and encrypts the information
	"""
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.LargeBinary)
	pub_date = db.Column(db.DateTime)
	del_date = db.Column(db.DateTime)

	def __init__(self, content, del_date):
		self.content = content
		self.pub_date = datetime.utcnow()
		self.del_date = del_date

#}}}

#{{{ Pages class
class pages():
	"""
	The pages class contains the webpages that are rendered
	"""
	@app.route('/', methods = ['GET', 'POST'])
	def index():
		"""
		Not unsurprisingly, this renders the index page
		"""
		if request.method == 'GET':
			return 'index'
		elif request.method == 'POST':
			return 'post stuff'

	@app.route('/<int:oti_id>:<string:encryption_key>', methods = ['GET'])
	def get(oti_id,encryption_key):
		"""
		Presents the oti
		"""
		oti = Oti.query.get_or_404(oti_id)
		return 'OTI ID: %d, encryption_key: %s' % (oti_id, encryption_key)
#}}}

# Run the application
if __name__ == '__main__':
	app.run()
# vim: tabstop=4 noexpandtab shiftwidth=4 softtabstop=4
