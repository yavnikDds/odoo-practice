from odoo import models, fields,api
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta
import logging
_logger = logging.getLogger(__name__)
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
    best_offer = fields.Float(string="Best Offer",compute='_compute_best_offer')
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    description = fields.Text(default='north')
    bedroom = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    total_area = fields.Float(compute='_compute_total_area')
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

    # methods
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        print("total_area compute")
        for record in self:
            record.total_area=(record.living_area or 0) + (record.garden_area or 0)
    
    @api.depends('offer_ids.price') # Add 'price' to track changes in related offers
    def _compute_best_offer(self):
        print("total_area inveres")
        for record in self:
             # Get the highest price among related offers
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0.0 # Default to 0 if no offers
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

    # compute and inverse fields 
    validity = fields.Integer(default=7, compute='_compute_validity', readonly=False)
    date_deadline = fields.Date(compute='_compute_date_deadline', store=True, readonly=False) #,store=True
    create_date=fields.Datetime(default=fields.Datetime.now, readonly=True)

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
    # compute and inverse fields 
    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        # _logger.info("=== COMPUTE DATE DEADLINE STARTED ===")
        for record in self:
            # _logger.info(f"Computing for record ID: {record.id}")
            # _logger.info(f"Current values - Validity: {record.validity}, Create Date: {record.create_date}")
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days=record.validity)
            else:
                record.date_deadline = False
        # _logger.info("=== COMPUTE DATE DEADLINE ENDED ===")

    # def _inverse_date_deadline(self):
    #     for record in self:
    #         if record.create_date and record.date_deadline:
    #             delta = (record.date_deadline - record.create_date.date()).days
    #             record.validity = delta
    #         else:
    #             record.validity = 0


# the inveres function did not work that is why i have used the compute fucntion but it two times hard work
    @api.depends('date_deadline', 'create_date')
    def _compute_validity(self):
        print("=== COMPUTE VALIDITY STARTED ===")
        for record in self:
            print(f"Validity Computing for record ID: {record.id}")
            print(f"Current values - Validity: {record.date_deadline}, Create Date: {record.create_date}")
            if record.create_date and record.date_deadline :
                print("if")
                delta = (record.date_deadline - record.create_date.date()).days
                record.validity = delta
            else:
                print("else")
                record.date_deadline = False
        print("=== COMPUTE VALIDITY ENDED ===")
