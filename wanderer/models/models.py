# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class usuarios(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'

     nivel_karma= fields.Integer(readonly=True)
     premium = fields.Boolean(readonly=True)
     fecha_nacimiento = fields.Datetime()
     fecha_registro = fields.Datetime(default = lambda self: fields.Datetime.now())


class accesoSpring(models.Model):
     _name = 'wanderer.accesoSpring'
     _description = 'Acceso Spring'

     

