step 1.
- go to the directory 
	cd c:\odoo\odoo_18
step 2.
- intialize the .git file if haven't done already
	git init
- to remove the .git file. the path should be relative to the current dir path
	 rm -rf custom-addon/.git

step 3.
- add a files and folder you want to commit 
	 git add custom-addon/
	 
step 4.
- finally commit the added files with a message 
	$ git commit -m "Add custom-addon with estate module and related views and models"

step 5.
- choose directory
	- to check which directory is chosen for the pushing the code
		$ git remote -v
	- to set path of the directory
		$ git remote add origin https://github.com/yavnikDds/odoo_18.git

step 6.
- push code 
	$ git push -u origin main

step 7.
- all done. now sit and relax the current version of your code is effectivly immortal
