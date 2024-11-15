from odoo import  fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"


    first_name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name", required=True)
    professional_statement = fields.Char(string="Professional statement")
    practicing_from = fields.Date(string="Practicing from")