from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    patient_name = fields.Char(string='Name')
    patient_age = fields.Integer(string='Age')
    Notes = fields.Text(string='Notes')
    patient_image = fields.Binary(string='Image')
    