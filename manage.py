#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""

"""

from flask.ext.script import Manager
from otip import app, db

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

if __name__ == '__main__':
    manager.run
