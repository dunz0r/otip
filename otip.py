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
from logging import Formatter, Filehandler
from forms import *
import os
#}}}

#{{{ Application config
app = Flask(__name__)
app.config.from_object('config')
#}}}

class name():
	@app.route('/', methods = ['GET', 'POST'])
	def index():
		if request.method == 'GET':
			return 'index'
		elif request.method == 'POST':
			return 'post stuff'

	@app.route('/get', methods = ['GET'])
	def get():
		return 'get'

# vim: tabstop=4 noexpandtab shiftwidth=4 softtabstop=4
