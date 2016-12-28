#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

#TODO make this configuration file into a yaml-file
"""
Configuration file for OTIP
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode
DEBUG = True

# How should we connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite://%s' % os.path.join(basedir, 'otip.db')
# vim: tabstop=4 noexpandtab shiftwidth=4 softtabstop=4
