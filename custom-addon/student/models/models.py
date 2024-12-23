from odoo import fields, models # imports two essential modules from the Odoo framework:
# This module provides field definitions for various data types (like Char, Integer, Boolean, etc.) that can be used to define the structure of Odoo models.
# This module is used to define the core structure of Odoo models, including their name, description, and fields.

class Student(models.Model): # python class named Student that inherits from the models.Model class. This means that the Student class will represent an Odoo model.
    _name = "student" # This line sets the internal name of the model to student. This name is used internally by Odoo to identify the model.
    # This line specifies the name of the database table that will be created. In this case, a table named student will be created.

    _description = "this is student profile." #This line sets a human-readable description for the model.

    name = fields.Char("name") #fields.Char: This specifies that the name field will store a Character string.
    # This line defines a field named name of type Char.
    # In the database, this will create a column named name of type VARChar (or a similar text type, depending on the database system).
    # "Name": This is the human-readable label for the field, which will be displayed in the Odoo interface.
    age = fields.Char("age")

    first_name = fields.Char("first_name")
    last_name = fields.Char("last_name")
    occupation = fields.Char("occupation")
    net_worth = fields.Char("net_worth")