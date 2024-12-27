1. Check Odoo Log Files
    Tool: Odoo logs

    insert this lines in odoo.conf
        log_level = debug
        logfile = odoo.log
        logfile = C:\odoo\odoo-com\odoo\odoo.log  ; Path to Odoo log file


    Purpose: To identify errors or warnings when Odoo fails to start, or during module loading or database connections. Logs are the first place to look when troubleshooting.

    How: Inspect logs at C:\odoo\odoo-com\odoo\logs or the default location specified in odoo.conf.

    What to look for: Error messages such as "ModuleNotFoundError" or "Failed to load server-wide module web" point out missing or misconfigured modules.

    To get immediate output in the terminal, try:
        python odoo-bin -c odoo.conf --log-handler=*:DEBUG

2. Check Odoo Log Files
    Tool: Odoo logs

    Purpose: To identify errors or warnings when Odoo fails to start, or during module loading or database connections. Logs are the first place to look when troubleshooting.
    
    How: Inspect logs at C:\odoo\odoo-com\odoo\logs or the default location specified in odoo.conf.
    
    What to look for: Error messages such as "ModuleNotFoundError" or "Failed to load server-wide module web" point out missing or misconfigured modules.

3. Ensure Proper Addons Path Configuration
    Tool: Odoo configuration file (odoo.conf)

    Purpose: Ensure the addons_path in the odoo.conf file includes the correct paths to all Odoo addons, especially if the error mentions missing modules.

    How: Open the odoo.conf file and verify that the addons_path includes directories where Odoo modules (e.g., web) are stored.

    What to look for: Missing or incorrect paths in addons_path that prevent Odoo from loading certain modules.

5. Install Missing Dependencies (e.g., Wkhtmltopdf)
    Tool: Wkhtmltopdf, Wkhtmltoimage

    Purpose: These tools are required by Odoo for rendering PDF reports and images. If they're missing, Odoo will generate warnings like "You need Wkhtmltopdf to print a pdf version of the reports."

    How: Install wkhtmltopdf and wkhtmltoimage on your system.

    What to look for: Install the tools if the log mentions their absence.

9. Check Database Connectivity
    Tool: Database connection strings and settings in odoo.conf

    Purpose: Ensure Odoo can connect to the database. Missing or incorrect database configuration can result in failures.
    
    How: Verify the db_host, db_user, db_password, and other database settings in odoo.conf.
    
    What to look for: Errors related to database connectivity, like authentication issues or database not found.


to see errrors in error log
-   python odoo-bin -c odoo.conf --log-level=debug

Clear the cache using:
    python odoo-bin -c odoo.conf --update=all --log-level=debug

for model debuigging, in this case it is compute and inverse
- use prints statement just like you used to do php with echo
- put them at each junction and condition to see the flow of the code
you can also use '_logger.info("=== COMPUTE DATE DEADLINE STARTED ===")
' 