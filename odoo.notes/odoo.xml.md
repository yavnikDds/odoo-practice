The <odoo> root element encapsulates all the definitions for a module. Within this, we'll define:

Views: Visual representations of data.
Actions: Actions that trigger specific operations, like opening a view.
Menus: Menu items to access different parts of the application.

    Step 1: Defining a Tree View
        - Let's start with the simplest view: a tree view. This is a list-like view that displays multiple records in a table format.
            <record id="student_tree_view" model="ir.ui.view">
            <field name="name">student.tree.view</field>
            <field name="model">student</field>
            <field name="arch" type="xml">
                <tree>
                <field name="name"/>
                <field name="age"/>
                </tree>
            </field>
            </record>
        - record tag: Defines a new record in the Odoo database.
        - id attribute: A unique identifier for the record.
        - model attribute: Specifies the model (table) to which the view belongs.
        - name field: The name of the view.
        - arch field: Contains the XML structure of the view.
        - tree tag: Defines a tree view.
        - field tags: Specify the fields to be displayed in the tree view.