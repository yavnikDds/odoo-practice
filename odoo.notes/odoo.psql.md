to access the database in PowerShell
    psql -U odoo_18 -d odoo_18
    -U specifies the user (odoo_18 in this case).
    -d specifies the database (odoo_18).
Odoo uses table names that are usually the technical name of the model. For res.users and res.partner, the table names are:

res_users (for res.users)
/d to see table 
/dt to see table existance
