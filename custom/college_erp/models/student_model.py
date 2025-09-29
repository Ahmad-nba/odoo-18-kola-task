# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student'      # Technical name of the model
    _description = 'Student Record'
