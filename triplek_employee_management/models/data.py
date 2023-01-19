from odoo import models, fields

class   TriplekProfile(models.Model):
    _name = "triplek.profile"
    
    name = fields.Char(string='Name' , required=True)
    email = fields.Char(string='Email')
    phone = fields.Integer(string='Phone')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male' , 'Male') , ('female' , 'Female')] , string="Gender")