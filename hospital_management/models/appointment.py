from odoo import  fields, models


class HospitalAppointment(models.Model):
    _name =  "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient", "Patient", tracking=True)
    appointment_date = fields.Date(string="Appointment date", tracking=True)
    note = fields.Text(string="Note", tracking=True)


