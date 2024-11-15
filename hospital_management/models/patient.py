from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Date of birth")
    phone = fields.Integer(string="Phone")
