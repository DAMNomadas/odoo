# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class usuarios(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'

     nivel_karma= fields.Integer(readonly=True)
     premium = fields.Boolean(readonly=True, default=False)
     fecha_nacimiento = fields.Datetime()
     fecha_registro = fields.Datetime(default = lambda self: fields.Datetime.now())
     fecha_inicio_premium = fields.Datetime()
     fecha_fin_premium = fields.Datetime(compute='_get_caducidad')

     @api.depends('premium')
     def comprar_premium(self):
          for record in self:
               if not record.premium:
                    record.fecha_inicio_premium = fields.Datetime.from_string(fields.Datetime.now())
                    record.premium = True



class venta(models.Model):
     _name = 'sale.order'
     _inherit = 'sale.order'

     def write(self, vals):
          respuesta = super(venta, self).write(vals)

          if vals.get('state') == 'sale' and any(
                  line.product_id.name == 'Suscripción premium' for line in self.order_line):
               self._otorgar_premium_en_venta(self)
          return respuesta

     @api.model
     def _otorgar_premium_en_venta(self, orden_venta):
         usuario = orden_venta.partner_id

         if usuario:
              usuario.comprar_premium()

     #hacer funcion para hacer compras
     #pasar como parametro la id del usuario, despues seguir todos los pasos,
     #self.env modelo venta, etc
     #el producto se tiene que crear en los datos de data


