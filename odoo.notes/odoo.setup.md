Step 1: Verify Python Installation
    python --version

Step 2: Install and Verify pip (Python Package Installer)
    pip --version

Step 3: Install Virtual Environment Tool
    ✅pip install virtualenv
    virtualenv --version    # not recognised as name of anything


step 4 clone odoo into your local repository 
    open git bash
    go to your project main directory
    go to the main repo of the project you want clone on the github
    copy the https link from the <> Cide dropdown button
    run this command in the git bash
    ✅ $ git clone https://github.com/yavnikDds/odoo.git

Step 4.1: Create a Virtual Environment for Odoo
Navigate to the folder where you cloned the Odoo Community repository:
    cd <path_to_your_odoo_folder>
Create a virtual environment named odoo-venv:
    virtualenv odoo-venv
    for python 3 
    ✅    python -m venv odoo-venv
Activate the virtual environment:
    ✅ .\odoo-venv\Scripts\Activate
    ✅ odoo-venv\Scripts\activate

Step 5: Install Odoo Dependencies
    in power shell terminal in vs code 
    ✅ pip install -r requirements.txt
to verify if needed - Re-run the Install Command: 
    Run the command again:
Check Installed Packages: List the installed Python packages and verify Odoo's dependencies are present:
    ✅ pip freeze

Step 6: Set Up the PostgreSQL Database for Odoo
    6.1:
    to delete user from the database
        DROP USER username;
    to Revoke all privileges the user has
        REVOKE ALL PRIVILEGES ON DATABASE odoo FROM odoo;
    to delete DATABASE
        DROP DATABASE odoo;
    to revoke all previlages from user 
        REVOKE ALL PRIVILEGES ON SCHEMA public FROM odoo;
        DROP USER odoo;
    the squense which worked for me is 
        ✅ DROP DATABASE odoo;
        ✅ REVOKE ALL PRIVILEGES ON SCHEMA public FROM odoo;
        ✅ DROP USER odoo;

Log in to PostgreSQL:
    Open SQL Shell (psql) or pgAdmin, and connect to your PostgreSQL server.
Create a New Database User
    ✅ CREATE USER odoo WITH PASSWORD 'odoo_18';
    ✅ CREATE USER odoo_18 WITH PASSWORD 'odoo_18';
    ✅ ALTER USER odoo CREATEDB;
Verify the User: Check if the odoo user is listed:
    \du

Step 7: Configure Odoo to Use the PostgreSQL Database
Locate the Odoo Configuration File:
    Find the odoo.conf file in your Odoo main directory (if it doesn't exist, you can create it).
    Generate a Default Config File
        ✅ python odoo-bin --save
    now the new odoo.conf file will be generated and you have to changes some of its parameters or configuration options

[options]
; This is the password that allows database operations:
; admin_passwd = admin
    db_host = localhost
    db_port = 5432
    db_user = odoo_18      
    db_password = odoo_18
    db_name = False
    ;addons_path = /usr/lib/python3/dist-packages/odoo/addons
    default_productivity_apps = True
"
Step 8: Run Odoo
Navigate to the Odoo Directory: In the terminal, navigate to your Odoo folder where the odoo-bin file is located:
    cd <path_to_your_odoo_folder>
    Run Odoo: With the virtual environment activated, run Odoo using the following command:
        ✅ python odoo-bin --config=odoo.conf
    use this code to run odoo the above code wont work
        ✅ python odoo-bin -c odoo.conf
    Run the Odoo server using the odoo-bin script.
        Use the odoo.conf file for configuration settings like database, ports, and paths.
    if needed 


<!-- above code will be enough to setup the odoo locally -->
    4. Generate a Default Config File
        python odoo-bin --save

additional steps 
    2. Check PostgreSQL User
        \du
    If the odoo user doesn’t exist, you can create it:
        CREATE USER odoo WITH PASSWORD 'odoo';
    Then grant the necessary privileges:
        GRANT ALL PRIVILEGES ON DATABASE odoo TO odoo;
    
    while login in the psql the password will be hidden even you type so the type correct password and press enter 

    to change user password in psql "If odoo is listed, reset its password by running the following SQL query (replace your_password with the desired password):"
    ALTER USER odoo WITH PASSWORD 'your_password';
    \q

    permissions to grant 
    -- Grant usage on the public schema
GRANT USAGE ON SCHEMA public TO odoo_18;

-- Grant create privileges to the odoo_18 user
GRANT CREATE ON SCHEMA public TO odoo_18;

-- Grant all privileges on all tables in the public schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO odoo_18;

-- Grant all privileges on all sequences in the public schema
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO odoo_18;

-- Grant all privileges on all functions in the public schema
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO odoo_18;


master pass word =  odoo
Database Name = odoo_1
Email = yavnik.dds@gmail.com
Password = odoo_1

Database Name = odoo_2
Email = yavnik.dds@gmail.com
Password = odoo_2

Database Name = odoo_3
Email = yavnik@gmail.com
Password = odoo_2

master pass word =  cefj-9dis-szj4
Database Name = odoo_18
Email = yavnik@gmail.com
Password = odoo_18

selecting a pypthon interpreter is neccessary for ex. .\osoo-venv\Scripts\python.exe-