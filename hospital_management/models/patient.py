from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Date of birth")
    phone = fields.Integer(string="Phone")
