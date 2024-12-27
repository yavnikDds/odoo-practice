to disable the database settings
    python .\odoo-bin -c odoo.conf --no-database-list
to enable the database settings
    python .\odoo-bin -c odoo.conf
here -r say the database user and -w says database password
    python odoo-bin -c odoo.conf -r odoo -w odoo

                            <!-- to create new module use scaffel command    -->
to create a new module template with the name
        python odoo-bin scaffold student 
        or
        ./odoo-bin scaffold school

to get help about scaffold command
    python odoo-bin scaffold -h

create a new dir 
    ✅ mkdir custom_addons
not-student - its a name of the module custom-addons/. - it's a folder in which the module will be created 
    ✅ python odoo-bin scaffold not-student custom-addons/.
to copy module
    student is templet that we want to copy and new_student is module name that we want to create
    python odoo-bin scaffold -t student  new_student   
    ✅ python odoo-bin scaffold -t ./custom-addon/student school custom-addon/.

add custom_addon folder in the .conf file > go to odoo apps > update apps list
    --addon-path: Specifies directories where Odoo should look for add-ons/modules.
    odoo/addons: The core add-ons directory (default).
    addons: A relative path for another add-ons directory.
    custom-addons: A relative path for custom add-ons.
        python .\odoo-bin --addon-path odoo\addons,addons,custom-addons
    python .\odoo-bin -c odoo.conf --addon-path odoo\addons,addons,custom-addons

the commands are the way to tell the cli what to do 
    python odoo-bin (opens the file) -c odoo.conf(tells it to choose configuration settings and parameters) --addon-path(it is an additional parameters to set addon-path ) odoo\addons,addons,custom-addons (locations) - in summery this command is used for runnig odoo with specific setting in the command

__manifest__.py is a critical file in an Odoo module that defines the metadata and configuration of the module. It tells Odoo what the module is, its dependencies, and how it behaves.
- Located in the root folder of every Odoo module.
- It provides information Odoo needs to load, display, and manage the module.

    Structure of __manifest__.py
    The file contains a Python dictionary with keys like:

    name: The module name displayed in the Odoo UI.

    Example: "Student Management"
    version: The module's version.

    Example: "1.0"
    depends: List of other modules this module depends on.

    Example: ["base", "mail"]
    data: Files (XML, CSV, etc.) loaded by the module.

    Example: ["views/student_view.xml", "security/ir.model.access.csv"]
    installable: Indicates if the module can be installed.

    Example: True
- During installation, Odoo reads this file to register the module.
- Defines how the module interacts with other parts of Odoo.





