from odoo import  fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    # _inherit = ["mail.thread"]
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"


    first_name = fields.Char(string="First name", required=True, tracking=True)
    last_name = fields.Char(string="Last name", required=True, tracking=True)
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female")
    ],  tracking=True)
    professional_statement = fields.Char(string="Professional statement", tracking=True)
    practicing_from = fields.Date(string="Practicing from", tracking=True)