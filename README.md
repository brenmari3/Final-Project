# Final-Project
Todo List CLI

By default, your CLI tool should write to a file called TODO.txt, TODO.csv, or TODO.json. (You may use the output format of your choice)

You should be able to have a subcommand, either by positional argument or a flag that will display your current TODO list items by reading them from your TODO save file.

Each TODO list item should have:

an id value
ad topic or category of the type of task (think of how you would categorize your assignments due for various classes)
a description of what the task is doing,
status of the TODO item (incomplete/in progress/complete)
With defined input arguments,your TODO list CLI tool should be able to modify your final TODO list file:

add new items to your TODO list file
change the status of the TODO item (incomplete/in progress/complete)
update previously added TODO items (description, date, category, etc.)
Add an option to be able to create or update a separate TODO list file with a different name (TODO2.txt, work-todo.csv, chores.csv, etc...)

your CLI tool can write to a file like TODO.txt by default, but you should be able to manage multiple todo lists with a separate argument.
For example by passing a --list-name argument you can point to a new or already defined TODO list file so that the tool can manage multiple lists.

Clean Code Requirements

Use Error statements of various types and print() statements to provide proper feedback to the users.
Apply sufficient comments to your code explaining how it works.
Name your submission .py file lastname_firstname_todo.py. For your submission, post your final .py file on your github and send me the link in the Brightspace Submission.
