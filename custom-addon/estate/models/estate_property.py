from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import date

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property contain all the information related to the about property like advertisment '
    # _inherit = 'estate.property'
    name = fields.Char(required=True, string="Title", help="This is a name of field")
    # One2many field: one property can have multiple offers
    # - 'estate.property.offer': refers to the model where offers are stored
    # - 'property_id': specifies which field in the offer model creates the link
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    tag_ids = fields.Many2many(
        'estate.property.tag',
        string='Tags'
    )
    postcode = fields.Char()
    date_availablility = fields.Date(string="Available Date", copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))  # Default to 3 months from today
    expected_price = fields.Float(required=True, string="Expected Price")
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    description = fields.Text(default='north')
    bedroom = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        default='east',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        required=True,
        copy=False,
        default="new",
    )
    # others fields
    property_type_id = fields.Many2one(comodel_name='estate.property.types', string="Property Type", index=True)
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    seller_id = fields.Many2one('res.users', string="Seller")
    active = fields.Boolean(string="Active", default=True)  # Add the active field

class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "this model will contain all the information about the types and it is kind of settings for the estate model"
    name = fields.Char(required=True, string="Property Type")

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    
    name = fields.Char(required=True, string="Name")

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "this will contain the One2many field and connect to the child model which is estate.property"

    price = fields.Float(string='Price', required=True)
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused")
        ],
        copy=False
    )
    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        string="Partner"
    )
    # Many2one field: each offer belongs to one property
    # When creating offer from property form view, Odoo automatically:
    # 1. Detects which property form we're in
    # 2. Sets this property_id field to link the offer to that specific property
    # 3. Maintains relationship without manual input

    property_id = fields.Many2one(
        "estate.property",
        required=True,
        string="Property"
    )