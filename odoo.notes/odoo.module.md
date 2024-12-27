<!-- ----------------------------------------------------- date : 16-12-2024 -->
🤦‍♂️ - Mistakes
#️⃣ - Commands for Powershell
⚒️ - How i perfomed the exercise

The first step of module creation is to create its directory.
- module must contain at least 2 files: the __manifest__.py file and a __init__.py
- the __manifest__.py file must describe our module and cannot remain empty.
- only required field is the name

    Exercise

    Create the required addon files.

    Create the following folders and files:

    /home/$USER/src/tutorials/estate/__init__.py

    /home/$USER/src/tutorials/estate/__manifest__.py

    The __manifest__.py file should only define the name and the dependencies of our modules. The only necessary framework module for now is base.
- Restart the Odoo server and go to Apps. Click on Update Apps List, search for estate and… tadaaa
- but before doing that make sure that you have included the path of the addon in the conf file addon key

     Exercise

    Make your module an ‘App’.

    Add the appropriate key to your __manifest__.py so that the module appears when the ‘Apps’ filter is on.
- added "'application':True," key to the __manifest__ so that it appears in app section 

 Warning

- Do not use mutable global variables.

    A single Odoo instance can run several databases in parallel within the same python process. Distinct modules might be installed on each of these databases, therefore we cannot rely on global variables that would be updated depending on installed modules.

A key component of Odoo is the ORM layer.
- Business objects are declared as Python classes extending Model, which integrates them into the automated persistence system.
- important attribute is _name, which is required and defines the name for the model
- This definition is enough for the ORM to generate a database table named test_model. By convention all models are located in a models directory and each model is defined in its own Python file.
    The model is defined in the file crm/models/crm_recurring_plan.py (see here)

    The file crm_recurring_plan.py is imported in crm/models/__init__.py (see here)

    The folder models is imported in crm/__init__.py (see here)

         Exercise

            Define the real estate properties model.

            Based on example given in the CRM module, create the appropriate files and folder for the estate_property table.

            When the files are created, add a minimum definition for the estate.property model.
- Any modification of the Python files requires a restart of the Odoo server. When we restart the server, we will add the parameters -d and -u:
    -  ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate
    - -u estate means we want to upgrade the estate module, i.e. the ORM will apply database schema changes. In this case it creates a new table. -d rd-demo means that the upgrade should be performed on the rd-demo database. -u should always be used in combination with -d.

🤦‍♂️ the mistake i made here is that i did'not created a __init__.py in models dir which is neccessary for each dir that should be imported in the main __init__.py file 

Model fields
- Fields are used to define what the model can store and where they are stored.
    - Fields are defined as attributes in the model class:

        from odoo import fields, models

        class TestModel(models.Model):
            _name = "test_model"
            _description = "Test Model"

            name = fields.Char()
        The name field is a Char which will be represented as a Python unicode str and a SQL VARCHAR.
to login to the postgres user use this command in powershell teminal 
#️⃣ psql -U odoo_18
to see if the table exist 
#️⃣ \dt estate_property
to see the table 
#️⃣ \d estate_property

Types

- There are two broad categories of fields:
    - ‘simple’ fields - which are atomic values stored directly in the model’s table - examples are Boolean, Float, Char, Text, Date and Selection.
    - relational’ fields - which link records (of the same or different models).
🤦‍♂️ implemented the instruction without the reading whole thing, which lead to an error that i had to resolve mannually. so from now on read the whole thing, try to quickly understand it,apply it, if error comes up reread the whole thing, and after resolving the error and successfully running the program review every single thing in just few minutes

- When the fields are added to the model, restart the server with -u estate
    $ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate
- Connect to psql and check the structure of the table estate_property. You’ll notice that a couple of extra fields were also added to the table. We will revisit them later.

Common Attributes

- Goal: at the end of this section, the columns name and expected_price should be not nullable in the table estate_property:

    - Much like the model itself, fields can be configured by passing configuration attributes as parameters:
        - #️⃣name = fields.Char(required=True)
    - using above code the fields in the database becomes not nullable
    - After restarting the server, both fields should be not nullable.

Automatic Fields

- Odoo creates a few fields in all models
    - id (Id)
      The unique identifier for a record of the model.

    - create_date (Datetime)
      Creation date of the record.

    - create_uid (Many2one)
      User who created the record.

    - write_date (Datetime)
      Last modification date of the record.

    - write_uid (Many2one)
      User who last modified the record.

Chapter 4: Security - A Brief Introduction

- Odoo provides a security mechanism to allow access to the data for specific groups of users.

Data Files (CSV)

- part of a module’s value is in the data it sets up when loaded. One way to load data is through a CSV file.
- a file importing data is located in the data folder of a module.
- When the data is related to security, it is located in the security folder.
- When the data is related to views and actions (we will cover this later), it is located in the views folder.
- Additionally, all of these files must be declared in the data list within the __manifest__.py file.
- content of the data files is only loaded when a module is installed or updated.
- The data files are sequentially loaded following their order in the __manifest__.py file. This means that if data A refers to data B, you must make sure that B is loaded before A.
- Why is all this important for security? Because all the security configuration of a model is loaded through data files, as we’ll see in the next section.

Access Rights
- Goal: at the end of this section, the following warning should not appear anymore:
    - WARNING rd-demo odoo.modules.loading: The models ['estate.property'] have no access rules...
    - When no access rights are defined on a model, Odoo determines that no users can access the data. It is even notified in the log:
    - Access rights are defined as records of the model ir.model.access
    - Each access right is associated with a model, a group (or no group for global access)
    - and a set of permissions: create, read, write and unlink2. Such access rights are usually defined in a CSV file named ir.model.access.csv.

     Exercise
        Add access rights.
        Create the ir.model.access.csv file in the appropriate folder and define it in the __manifest__.py file.
        Give the read, write, create and unlink permissions to the group base.group_user.
        Tip: the warning message in the log gives you most of the solution

         - to do that follow the following steps 
         - 1. Locate the folder for the module (if you're using the estate module, you would typically find this in estate/security/ or a similar subdirectory).
         - 2. Create the ir.model.access.csv file if it doesn't exist
         - 3. Define the access rights for the estate_property model and assign them to the group base.group_user (which represents all regular users).
         - 4. "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
            estate_access,Estate Property Access,estate.model_estate_property,base.group_user,1,1,1,1"
         here 
notes :- This follows Odoo's external ID naming convention:
         The prefix is typically the module name (estate)
         Followed by model_
         Then the model's internal name (estate_property)this is a class name not _name
🤦‍♂️ could not quite understand what the "model_id:id,group_id:id" was as they refer to it as external ID, and just dug to deep which was a mistke instead of just diving into the problem. finally got some understanding after applied it and then got error and then asked clude ai for clarification

<!-- ----------------------------------------------------- date : 17-12-2024 -->
Chapter 5: Finally, Some UI To Play With

Data Files (XML)
- When the format is more complex use the XML format.
- The XML files must be added to the same folders as the CSV files and defined similarly in the __manifest__.py.
- When the data is linked to views, we add them to the views folder.
- When performance is important, the CSV format is preferred over the XML format.
-  the user interface (actions, menus and views) is largely defined by creating and composing records defined in an XML file. A common pattern is Menu > Action > View. To access records the user navigates through several menu levels; the deepest level is an action which triggers the opening of a list of the records.

Actions
- Goal: at the end of this section, an action should be loaded in the system. We won’t see anything yet in the UI, but the file should be loaded in the log: 
    - INFO rd-demo odoo.modules.loading: loading estate/views/estate_property_views.xml
- Actions can be triggered in three ways:
    - by clicking on menu items (linked to specific actions)
    - by clicking on buttons in views (if these are connected to actions)
    - as contextual actions on object
- we would like to link a menu to the estate.property model,
- The action can be viewed as the link between the menu and the model.
    - basic action 
    <record id="test_model_action" model="ir.actions.act_window">
    <field name="name">Test action</field>
    <field name="res_model">test_model</field>
    <field name="view_mode">list,form</field>
    </record>
    - id is an external identifier. It can be used to refer to the record (without knowing its in-database identifier).
    - model has a fixed value of ir.actions.act_window (Window Actions (ir.actions.act_window)).
    - name is the name of the action.
    - res_model is the model which the action applies to.
    - view_mode are the views that will be available; in this case they are the list and form views. We’ll see later that there can be other view modes.

Menus
- Goal: at the end of this section, three menus should be created and the default view is displayed:
    - A basic menu for our test_model_action is:
        - <menuitem id="test_model_menu_action" action="test_model_action"/>
    - The menu test_model_menu_action is linked to the action test_model_action, and the action is linked to the model test_model. As previously mentioned, the action can be seen as the link between the menu and the model.

    - However, menus always follow an architecture, and in practice there are three levels of menus:
        1. The root menu, which is displayed in the App switcher (the Odoo Community App switcher is a dropdown menu)
        2. The first level menu, displayed in the top bar
        3. The action menus

Exercise
 - Add menus.
 - Create the estate_menus.xml file in the appropriate folder and define it in the __manifest__.py file. Remember the sequential loading of the data files ;-
 - Create the three levels of menus for the estate.property action created in the previous exercise. Refer to the Goal of this section for the expected result.

implementation 
 - Create the File:
    - Create a new file named estate_menus.xml. in views folder
-  The file should define a three-level menu hierarchy to link to the estate.property action.
-  Mention estate_menus.xml files in 'data': ['views/estate_menus.xml'],
-  write the below code in "estate_menus.xml"
        <? xml version="1.0" encoding="UTF-8"?>
        < odoo>
            <!-- Top-Level Menu -->
            <menuitem id="estate_menu_root" name="Estate" sequence="1"/>

            <!-- Second-Level Menu -->
            <menuitem id="estate_menu_properties" name="Properties"
                    parent="estate_menu_root" sequence="2"/>

            <!-- Third-Level Menu with Action -->
            <menuitem id="estate_menu_property_list" name="Property List"
                    parent="estate_menu_properties" sequence="3"
                    action="test_model_action"/>
        </odoo>
- Reload Your Module: Update your module:
    - #️⃣ python odoo-bin -c odoo.conf -d odoo_18 -u estate
- you should be able to see changes 
🤦‍♂️ there was some kind of error coming due to the sequence of the "estate_menues.xml" and "estate_property_views.xml" because the action must be define before the menues  

Fields, Attributes And 
"https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#odoo.fields.Field"

- Goal: at the end of this section, the selling price should be read-only and the number of bedrooms and the availability date should have default values. Additionally the selling price and availability date values won’t be copied when the record is duplicated.

    - in most cases we want to fine tune the view.
        - some fields have a default value
        - some fields are read-only
        - some fields are not copied when duplicating the record

Some New Attributes

- Exercise
    Add new attributes to the fields.
    Find the appropriate attributes (see Field) to:
    - set the selling price as read-only
    - prevent copying of the availability date and the selling price values
        -  set the selling price module,  readonly (default: False) to true
        -  copy (default: True) to false
        in fileds of form in models.py file

Default Values

- Any field can be given a default value, add the option default=X, X is either (boolean, integer, float, string) or a function

Exercise
    - Set default values.
    - Add the appropriate default attributes so that:
    - the default number of bedrooms is 2
    - the default availability date is in 3 months
    - Tip: this might help you: today()
    - date_availablility = fields.Date(string="Available Date", copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))  # Default to 3 months from today
    - bedroom = fields.Integer(string="Bedrooms", default=2)

Reserved Fields

documentaion - https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#reference-orm-fields-reserved

- A few field names are reserved for pre-defined behaviors. They should be defined on a model when the related behavior is desired.

    - Exercise
        - Add active field.
        - Add the active field to the estate.property model.
- just add a simple field as a boolean type with string="Active" in the estate_property.py
- a record has active=False, it is automatically removed from any search
- To display the created property, you will need to specifically search for inactive records.   

    -  Exercise
        - Set a default value for active field.
        - Set the appropriate default value for the active field so it doesn’t disappear anymore.
    - just set "default" attribute to "True" for the Active field 

    - Exercise
        - Add state field.
        - Add a state field to the estate.property model. Five values are possible: New, Offer Received, Offer Accepted, Sold and Cancelled. It must be required, should not be copied and should have its default value set to ‘New’.
        - Make sure to use the correct type!

Chapter 6: Basic Views

- Odoo is able to generate default views for a given model.
- In practice, the default view is never acceptable for a business application.
- Views are defined in XML files with actions and menus. They are instances of the ir.ui.view model.
- In our real estate module, we need to organize the fields in a logical way:
    - in the list view, we want to display more than just the name.
    - in the form view, the fields should be grouped.
    - in the search view, we must be able to search on more than just the name. Specifically, we want a filter for the ‘Available’ properties and a shortcut to group by postcode.

List

- List views, also called list views, display records in a tabular form
- Their root element is <list>. 
- The most basic version of list view is 
    <list string="Tests">
        <field name="name"/>
        <field name="last_seen"/>
    </list>
    - Exercise
        - Add a custom list view.
        - Define a list view for the estate.property model in the appropriate XML file. Check the Goal of this section for the fields to display.
        Tips:
        - do not add the editable="bottom" attribute that you can find in the example above. We’ll come back to it later.
        - some field labels may need to be adapted to match the reference.

<!-- ----------------------------------------------------- date : 18-12-2024 -->

- string
    The view title. It is displayed only if you open an action that has no name and whose target is new (opening a dialog).
🤦‍♂️ - The mistake was, to not reading properly the refrence links included in the the artical tutorial, there i found out that (The root element of list views is list (the previous name was tree)).

Form

Goal: at the end of this section, the form view should look like this:

- Forms are used to create and edit single records.
- Their root element is <form>. They are composed of high-level structure elements (groups and notebooks) and interactive elements (buttons and fields):
- It is possible to use regular HTML tags such as div and h1 as well as the the class attribute (Odoo provides some built-in classes) to fine-tune the look.

    - Exercise
        - Add a custom form view.
        - Define a form view for the estate.property model in the appropriate XML file. Check the Goal of this section for the expected final design of the page.

    To perform this exersice, i need to understand what it's exectly are its requirment and what components i needs to fullfil that requirment
     - Requirment - this requirment are simple in this exersice, they need me to make structure visually same as the screenshot.
     - so to that i'll have to read documentation that fulfill the requirments
     - inside this link "https://www.odoo.com/documentation/18.0/developer/reference/user_interface/view_architectures.html#chatter-widget" a section called "Structural components"
     - then apply that in the xml file to create similar structure to the requirments
     - to avoid relaunching the server every time you do a modification to the view
        - $ ./odoo-bin -c odoo.conf -d odoo_18 -u estate --dev xml

Search

- they are used to filter other views’ content (generally aggregated views such as List)
- Their root element is <search>.
- most basic version of this view
    <search string="Tests">
        <field name="name"/>
        <field name="last_seen"/>
    </search>
- Exercise
    - Add a custom search view.
    - Define a search view for the estate.property model in the appropriate XML file. Check the first image of this section’s Goal for the list of fields.

- Search views can also contain <filter> elements, which act as toggles for predefined searches.Filters must have one of the following attributes:
    - domain: adds the given domain to the current search
    - context: adds some context to the current search; uses the key group_by to group results on the given field name

⚒️ - to perform this exersise first i reviewed the whole section about search and relevent link. and then asked chat gpt to explain the code that was given in the example. refer estate_property_views.xml file for it.

Domains

- In Odoo, a domain encodes conditions on records: a domain is a list of criteria used to select a subset of a model’s records. Each criterion is a triplet with a field name, an operator and a value. A record satisfies a criterion if the specified field meets the condition of the operator applied to the value.
- For instance, when used on the Product model the following domain selects all services with a unit price greater than 1000:
- By default criteria are combined with an implicit AND, meaning every criterion needs to be satisfied for a record to match a domain. The logical operators & (AND), | (OR) and ! (NOT) can be used to explicitly combine criteria.

    Exercise

    Add filter and Group By.
    The following should be added to the previously created search view:
        - a filter which displays available properties, i.e. the state should be ‘New’ or ‘Offer Received’.
        - the ability to group results by postcode.

    Domain Filters:

        - Purpose: Dynamically filter records based on specific conditions
        - Structure: List of tuples (field, operator, value)
        Common Operators:

        = (exact match)
        in (multiple values)
        != (not equal)


        - Example: [('state', 'in', ['New', 'Offer Received'])]
        Used in: Search views, record searches, relational fields

    Group By Filter:

        - Purpose: Organize and aggregate records by a specific field
        - Implemented via context: {'group_by': 'field_name'}
        Creates hierarchical view of data
        Allows data analysis and summary views
        - Example: Grouping properties by postcode

⚒️ - to perform this exersise first i reviewed the whole section about domain. and then asked claude for an assistance as no code example was available and created a groupby and domain filter. refer estate_property_views.xml file for it.

Chapter 7: Relations Between Models

<!-- ----------------------------------------------------- date : 19-12-2024 -->

- in any real business scenario we need more than one model. links between models are necessary.
- ex. One can easily imagine one model containing the customers and another one containing the list of users. You might need to refer to a customer or a user on any existing business model.
- A property can have one type. the same type can be assigned to many properties.
- This is supported by the *many2one* concept.
- A many2one is a simple link to another object.
- For example, in order to define a link to the res.partner in our test model, we can write:
    - partner_id = fields.Many2one("res.partner", string="Partner")
- By convention, many2one fields have the _id suffix.
- Accessing the data in the partner can then be easily done with:
    - print(my_test_object.partner_id.name)
- print(my_test_object.partner_id.name)

    Exercise
        Add the Real Estate Property Type table.

        - Create the estate.property.type model and add the following field:

            Field               Type               Attributes
            -------------------------------------------------
            name                Char               required

        - Add the menus as displayed in this section’s Goal
        - Add the field property_type_id into your estate.property model and its form, list and search views
        
        This exercise is a good recap of the previous chapters: you need to create a model, set the model, add an action and a menu, and create a view.

        Tip: do not forget to import any new Python files in __init__.py, add new data files in __manifest.py__ or add the access rights ;-

⚒️- so the approach i am taking here is, carefully reading from the very start and trying my best to understand what it is trying to say.
- first line - i need to add a table, may be its kind of visual thing with linput, like i need to create a form where the functionality to add 'property type, buyer and seller'. and even do not understand it 100 percent but anyways i am going to go forward 
- second line - i need to create a model "estate.property.type" and inside that i need to create a fields with settings metioned.
- third line - need to create a menu as shown in the goal image like Estate > Settings > Property Type
- fourth line - integrate "property_type_id" field into the "estate.property" form, list and search view. 
- fifth line - need to add all the new file in respective __init__ and __menifest__ files.

🤦‍♂️ - the bug here was that the menu was not apearing, i followed the process to write menu > action > view but the menu was still not apearing because in odoo the admin panel and users admin have same interface and the content they see and interact with them are resticted by the security => ir.model.access.csv file, and if i create new model then it should have new access line in the ir.model.access.csv to mention its permissions. to perform any task i need to follow all the steps and convention of the odoo correctly without miss


<!-- ----------------------------------------------------- date : 20-12-2024 -->

going further there are still some other thing left to add
- The buyer can be any individual
- salesperson must be an employee of the real estate agency (i.e. an Odoo user).
- **res.partner**: a partner is a physical or legal entity. It can be a company, an individual or even a contact address. it represents all individuals and companies in Odoo, including customers, vendors, and others.
- **res.users**: the users of the system. Users can be ‘internal’, i.e. they have access to the Odoo backend. Or they can be ‘portal’, i.e. they cannot access the backend, only the frontend (e.g. to access their previous orders in eCommerce).

    - Exercise
        - Add the buyer and the salesperson.
        - Add a buyer and a salesperson to the estate.property model using the two common models mentioned above. They should be added in a new tab of the form view, as depicted in this section’s Goal.
        - The default value for the salesperson must be the current user. The buyer should not be copied.
        - Tip: to get the default value, check the note below or look at an example

⚒️- just added the buyers and sellers field with relevent models to the form view using notebook and page tag

Many2many

- define the concept of property tags. for example  ‘cozy’ or ‘renovated’.
- A property can have many tags tag can be assigned to many properties.this supported by many2many concept.
- A many2many is a bidirectional multiple relationship: any record on one side can be related to any number of records on the other side.
- By convention, many2many fields have the _ids suffix.
- list of records is known as a recordset
    Exercise
    Add the Real Estate Property Tag table.
    - Create the estate.property.tag model and add the following field
    Field       Type        Attributes
    ----------------------------------
    name        Char        required
    - Add the menus as displayed in this section’s Goal
        ⚒️ - so section's goal shows that i have to add a third level menu, inside setting with a name "Property Tags". So in order to do this, first i have to just add a code inside menu.xml file because all the preparetion are made already to create menu-sub menu-third level menu.
        1. add code for third level menu => create an action code =>create model => add model access info in access file => create a view
    - Add the field tag_ids to your estate.property model and in its form and list views
        ⚒️ - to do that go the model file and add tag_ids eith many2many config

    - Exercise
    Add the Real Estate Property Tag table.
        - Create the estate.property.tag model and add the following field:

        Field           Type            Attributes
        ------------------------------------------
        name            Char            required

        - Add the menus as displayed in this section’s Goal
        - Add the field tag_ids to your estate.property model and in its form and list views

        Tip: in the view, use the widget="many2many_tags" attribute as demonstrated here. The widget attribute will be explained in detail in a later chapter of the training. For now, you can try to adding and removing it and see the result ;-
        ⚒️ - added manu just like before with with modification in menu>action>model>views
        ⚒️ - add many2many field where i need select the multiple tags to the model(estate.property) in which you are actually going to use and also add field inside respective view with relevent attributes
            - normal char field in settings>proprerty tags view and relevent model
        - and that's it you are good to go 

One2many

Goal : a new estate.property.offer model should be created with the corresponding form and list view.
- offers should be added to the estate.property model:
- define the concept of property offers. A property offer is an amount a potential buyer offers to the seller. The offer can be lower or higher than the expected price.
- An offer applies to one property, but the same property can have many offers.
- By convention, one2many fields have the _ids suffix. They behave as a list of records, meaning that accessing the data must be done in a loop:
    - for test in partner.test_ids:
        print(test.name)
- Because a One2many is a virtual relationship, there must be a Many2one field defined in the comodel.

Exercise
    - Add the Real Estate Property Offer table.
    - Create the estate.property.offer model and add the following fields:
    Field       Type                        Attributes      Values
    -----------------------------------------------------------------------
    price       Float                       
    status      Selection                   no copy         Accepted, Refused
    partner_id  Many2one (res.partner)      required
    property_id Many2one (estate.property)  required
    - Create a list view and a form view with the price, partner_id and status fields. No need to create an action or a menu.
    - Add the field offer_ids to your estate.property model and in its form view as depicted in this section’s Goal.
    ⚒️-To perform this exersise create a model 'estate.property.offer' with fields 'price', 'status', 'partner_id' and the id is a 'property_id'
    - create a 'offer_ids(fields.One2many)' in 'estate.property'
    - so here in offer_ids will connect to the 'estate.property.offer' with the help of `offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")` getting all the offers for that perticular offer 
    - so now model part is over then we need to define its view with the list and form view. in the `estate.property`
        - here, use this code `<page string="Offers">
                            <group>
                                <field name="offer_ids" nolabel="1">
                                    <list string="Property Offers" editable="bottom">
                                        <field name="price"/>
                                        <field name="partner_id"/>
                                        <field name="status"/>
                                    </list>
                                    <form>
                                        <group>
                                            <field name="price"/>
                                            <field name="partner_id"/>
                                            <field name="status"/>
                                        </group>
                                    </form>
                                </field>
                            </group>
                        </page>` with field one2many to get data of many2one field, here this 'offer_ids' fetch all the data from the its companineon field that is in the estate.property.offers with help of its property_id field, and it also stores the 'property_id' info because it is used in one2many field 
- There are several important things to notice here. First, we don’t need an action or a menu for all models.
- Some models are intended to be accessed only through another model.
- in this case. an offer is always accessed through a property.
- despite the fact that the property_id field is required, we did not include it in the views.
- Well that’s part of the magic of using the Odoo framework: sometimes things are defined implicitly. 
- When we create a record through a one2many field, the corresponding many2one is populated automatically for convenience.


-------------------------------------------- 1. Odoo 17 and 18 Development Tutorial

'auto_install':True,
# If a module has `auto_install: True` and all its dependencies are installed, Odoo will automatically install the module. However, if any dependency is missing, the module won't be installed.

What is a fields?
- The term "fields" refers to attribute or the properies of mapped class that correspond to columns in a database table.
- these are like datatypes but for the database

Types of fields in odoo
-> simple fields(integer, float, boolean, Char(it store small string value in the database), text(contain more data compare to the Char), html (it stores the string values as html content), Selection(its like a drop down), Date field(to store date), Datetime(to store date with time), Monetary (it stores the decimal plud currency), binary(to store any files in Base64 format),image(to store the only images in database Base64 format), json(stores json structure in database))
-> Relational fields ( Many2one(in a senario many thing can belong to one(ex. selecting, a same country can belong to many user)), One2many(it is like where the one thing belong to many thing, a vice versa of Many2one), Many2many (you have to choose many things at once like tags etc.))
-> Function/Compute/Reference fields(its value is calculated dynamically based on the values of other fields)
-> related fields(its like a map to some data stored in model for example a school address to show in student module,its basically read only field )
-> reference fields(its like many2one field but you can choose diffrent models )

Here's a brief summary of the attributes

**Field Attributes:**

* **String:** it is used for labeling purpose.
* **Required:** Makes the field mandatory to fill in.
* **Invisible:** Hides the field from the user interface.
* **Groups:** Restricts access to the field to specific user groups.
* **Size:** Sets the maximum length of the string.
* **Index:** Creates an index on the field for faster searching.
* **Help:** Provides a tooltip or help message for the field.
* **copy:** True(default) enable the the coping the content on duplication, Flase make it disable.

**View Attributes:**

* **Default:** Sets a default value for the field.
* **Readonly:** Makes the field read-only, preventing user input.
* **Translate:** Allows the field's label to be translated into different languages if the multilanguage option is available.
* **States:** Defines visibility and editability of the field based on record states.
* **Widget:** Specifies a custom widget for the field's display and input.
* **Tracking:** Tracks changes to the field's value over time. and shows it in below activities of odoo module,but you can use it as it is, it will thorugh error othervise
- in xml use "1" and in python side use True
- xml attribute gets first priorty if they overwrite a python attributes
- the . which are used on the python side becomes _ in the postgres side
These attributes are used to customize the behavior and appearance of fields in Odoo models and views.

=> Text field vs Char field 
text - can store large and multiple line of text
char - store relativley less data

if no label name is mentioned (using string attribute) it will take the field name with first char as Capital and removeing all underscore

html field is like textarea which lets you markup up text with gui just like word
- place holder will show a psudo text
- use nolabel to just show the input field
- tracking will keep the history of the all the changes to the field

Boolean field
- it creates a checkbox 
- default=True #will make it checked by default

- you will always need to import fields and models from odoo

selection/combobox field 
- field.Selection(
    [('male','Male'),('female','Female')]
<!-- [('backend','frontend')] -->
)
- examples
    1. gender = fields.Selection(
        [('male','Male'),('female','Female')]
    )
    2. adv_gender = fields.Selection(get_options_for_adv_gender) 
    def get_options_for_adv_gender(self):
        return [('not-male','Not-Male'),('not-female','Not-Female'),('not-human','Not-Human')]
    3.  from odoo import api, fields, models
        @api.model
        def _get_vip_list(self):
            return [('a','A'),('b','B'),('c','C')]
        adv_gender = fields.Selection(get_options_for_adv_gender) 
- placeholder will only appear when no field is selected

integer field
- roll_number=fields.integer()
<!-- without string attribute the in front end roll_number will apear as Roll Number replacing the first letter with capital and _ with space -->
- for interger if user input 0 then required will not work and solution is 
    - overwrite create and write method
    - add odoo or postgres constraint 
    - widget
- you can add index attribute to any fields and it will create a betree index in postgeress and wont affrect odoo in front or backend 

-------------------------------------------- /1.Odoo 17 and 18 Development Tutorial
Chapter 8: Computed Fields And Onchanges
- The relations between models are a key component of any Odoo module.They are necessary for the modelization of any business case.
- the value of one field is determined from the values of other fields and other times we want to help the user with data entry. These cases are supported by the concepts of computed fields 


Computed Fields

    - Goal: at the end of this section:
        In the property model, the total area and the best offer should be computed:
        In the property offer model, the validity date should be computed and can be updated:

we have defined the living area as well as the garden area. It is then natural to define the total area as the sum of both fields.

--------------------------------------------- NotebookLm
When to use these

    When deciding between Computed Fields and Onchange Methods, consider the following:
        ● Prioritize Computed Fields when the calculated value needs to be accessible outside the form view context, such as in reports or automated processes.
        ● Avoid using Onchange Methods for business logic as they are only triggered within the form view and may not execute in other scenarios.
        ● Carefully assess performance implications when using stored computed fields, particularly when dealing with complex dependencies
    - The optimal approach depends on the specific requirements and context of your Odoo module development.
    - use these features where user have to calculate something manually, like cart total value, or discount on some purchase value etc.
--------------------------------------------- /NotebookLm

- Fields can also be computed. In this case, the field’s value computed on-the-fly by calling a method of the model.
- To create a computed field, create a field and set its attribute compute to the name of a method. The computation method should set the value of the computed field for every record in self.
- By convention, compute methods are private, meaning that they cannot be called from the presentation tier, only from the business tier. Private methods have a name starting with an underscore _.


Dependencies

- The value of a computed field, depends on the values of other fields. The ORM expects the developer to specify those dependencies on the compute method with the decorator depends(). The given dependencies are used by the ORM to trigger the 

Note -

    - self is a collection.
    - The object self is a recordset, i.e. an ordered collection of records. It supports the standard Python operations on collections, e.g. len(self) and iter(self), plus extra set operations such as recs1 | recs2.
    - Iterating over self gives the records one by one, where each record is itself a collection of size 1. You can access/assign fields on single records by using the dot notation, e.g. record.name.

Exercise -
    Compute the total area.
        - Add the total_area field to estate.property. It is defined as the sum of the living_area and the garden_area.
        - Add the field in the form view as depicted on the first image of this section’s Goal.
⚒️ - add a field in the model like this `total_area = fields.Integer(compute='_compute_total_area')`
    -     `@api.depends("living_area", "garden_area")`   # mention the depends fields
          `def _compute_total_area(self):` #def function name with self as a parameter
          `for record in self:` # run a loop for self with the allies for single record and get the values of that single record
          `record.total_area=(record.living_area or 0) + (record.garden_area or 0)` # no need to return the, the odoo will automatically return the value.

Exercise -
    Compute the best offer.
    - Add the best_price field to estate.property. It is defined as the highest (i.e. maximum) of the offers’ price.
    - Add the field to the form view as depicted in the first image of this section’s Goal.

⚒️ - @api.depends('offer_ids.price') 
    The @api.depends decorator informs Odoo's ORM about the dependencies of a computed field.
    - offer_ids.price' specifies that Odoo should track changes specifically to the price field of any related offer in offer_ids.
    - Without this, the ORM wouldn’t know that changing the price in offer_ids requires recomputing best_offer.
    - Even though the code explicitly mentions 'offer_ids.price', Odoo doesn’t limit you to iterating only over price.
    - You can still loop through the full offer_ids recordset (record.offer_ids) to access all fields, not just price.
    - mapped extracts specific field values (price) from each record in a recordset. Returns a list of those values
    - max() finds the largest value in the list of prices returned by mapped('price').


Inverse Function

- we can define a validity duration for an offer and set a validity date.

Exercise
    Compute a validity date for offers.

    - Add the following fields to the estate.property.offer model:
    Field           Type            Default
    validity        Integer         7
    date_deadline   Date

    Where date_deadline is a computed field which is defined as the sum of two fields from the offer: the create_date and the validity. Define an appropriate inverse function so that the user can set either the date or the validity.
    Tip: the create_date is only filled in when the record is created, therefore you will need a fallback to prevent crashing at time of creation.
    - Add the fields in the form view and the list view as depicted on the second image of this section’s Goal.






































tips -
    - implemented the instruction without the reading whole thing, which lead to an error that i had to resolve mannually. so from now on read the whole thing, try to quickly understand it,apply it, if error comes up reread the whole thing, and after resolving the error and successfully running the program review every single thing in just few minutes 
