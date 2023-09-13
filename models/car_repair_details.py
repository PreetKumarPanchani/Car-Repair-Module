from odoo import api, fields, models

class CarRepairDetails(models.Model):
    _name = 'car_repair.details'
    _description = 'Car Repair Details'

    chassis_number = fields.Char(string='Chassis Number')
    car_model = fields.Char(string='Car Model')
    car_brand = fields.Char(string='Car Brand')
    license_plate = fields.Char(string='License Plate')
    color = fields.Char(string='Color')
    seats_number = fields.Integer(string='Seats Number')
    doors_number = fields.Integer(string='Doors Number')
    last_odometer = fields.Float(string='Last Odometer')
    model_year = fields.Char(string='Model Year')
    fuel_type = fields.Selection([
        ('diesel', 'Diesel'),
        ('gasoline', 'Gasoline'),
        ('full_hybrid', 'Full Hybrid'),
        ('plug_in_hybrid_diesel', 'Plug-in Hybrid Diesel'),
        ('plug_in_hybrid_gasoline', 'Plug-in Hybrid Gasoline'),
        ('cng', 'CNG'),
        ('lpg', 'LPG'),
        ('hydrogen', 'Hydrogen'),
        ('electric', 'Electric'),
    ], string='Fuel Type')
    transmission = fields.Selection([
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ], string='Transmission')
    horsepower = fields.Float(string='Horsepower')
    reason_for_repair = fields.Text(string='Reason For Repair')
    power = fields.Float(string='Power')
    co2_emissions = fields.Float(string='CO2 Emissions')
    list_of_damage = fields.Text(string='List of Damage')
    co2_standard = fields.Char(string='CO2 Standard')
