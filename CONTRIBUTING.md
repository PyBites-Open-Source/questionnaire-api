# Welcome to OpenTrivia project!

We are glad to be hear. So? You want to contribute to our project? Great, 
bring here your best ideas. We are looking forward to work along with You 
and to have fun by making this project better. 

## What PR we accept?

Theoretically, everything wich can add value to this project is accepted. That's all!
However, in order to give them a name, we are looking for the following contribution types:

1. Code Enhancements: Did you spot an ugly code? Let's make it better.  
2. Ideas: Do you have an idea about a new feature wich we ca add? Let's us know about it. Don't be shine.
3. Bugs: Let's try to fix together as many bugs as we can. We know for sure that we will have some of them. :*(

## Set up instructions

1. Fork the repo
2. Clone your fork
3. Set the upstream repository for master
	```
	# Step 1: Add the upstream remote
	$ git remote add upstream <paste-the-link-of-the-forked-repository>
	
	# You can replace "upstream" with any name you want. 
	# Fetch all the changes from upstream remote
	$ git fetch upstream
	
	# At this point you should have "origin" and "upstream"
	$ git remote
	origin
	upstream

	# Now, because we want our master to be up to date with the original forked 
	# master, we have to set this using the below command.
	$ git branch --set-upstream-to=upstream/master master
	
	# When you doing a pull, the changes will not gone comming from 
	# origin/master, instead they will come from upstream/master.
	git pull
	```
4. Create a branch
	`$ git checkout -b <your-branch-name>`
5. Before starting doing something, run the tests and ensure yourself that 
   everything works and nothing is broken. If everything works, 
   then you are ready to make changes. 
7. Make changes. Run again the tests. If the tests are passing. You are on the right way to push the changes.

