# Welcome to OpenTrivia project!

We are glad you are here. So, you want to contribute to our project? Great, 
bring here your best ideas. We are looking forward to work along with You 
and to have fun together by making this project better. 

# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, 
or any other method with the owners of this repository before making a change.

## What PR we accept?

Theoretically, everything wich can add value to this project is accepted. That's all!
However, in order to give them a name, we are looking for the following contribution types:

1. Code Enhancements: Did you spot an ugly code? Let's make it better.  
2. Ideas: Do you have an idea about a new feature wich we ca add? Let's us know about it.
3. Bugs: Let's try to fix together as many bugs as we can. We know for sure that we will have some of them. :(

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

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

	# Now, because we want our master branch to be up to date with the forked branch 
	# we need to set this using the below command.
	$ git branch --set-upstream-to=upstream/master master
	
	# When you are doing a pull, the changes will not gone coming from 
	# origin/master, instead they will come from upstream/master.
	git pull
	```
4. Create a branch
	`$ git checkout -b <your-branch-name>`
5. Before starting doing something, run the tests and ensure yourself that 
   everything works and nothing is broken. If everything works, 
   then you are ready to make changes. 
7. Make changes. Run again the tests. If the tests are passing. You are on the right way to push the changes.

