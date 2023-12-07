# FrenchRoast

A project in the ~~javaspace~~ datapipe.

This is a straight-forward ~~Java~~ Python project.

## What you start with

In the directory `resources` you will find two files.

A single input file, `transactions.csv`.
It contains 20,000 rows of data (so a small set).
Each line is one `transaction` describing an action to a customer's account.

We don't know, when we start, how many different, unique customers are in the file.
We don't know how many accounts each customer has.
But that should not matter.

Your code should be able to adapt to a different file of transactions, with different data
entirely, and produce a clean JSON file.
_So don't count on having the same number of customers and or number of accounts per customer_

You should look at the CSV input file and examine it closely.
The first line is the column names, each line after that, contains the data for a single transaction.
The first line of data in the file looks like:

```
1,103,10000,withdrawal,714.25,Fri Dec 06 12:30:05 EST 2013
```

This means you need to add `714.25` to customer number `103`'s number `10000` account.

You are to read in the transactions in the CSV file and produce a JSON summary file after
processing each and every transaction.

There is a `target.json` already there to show you
what you are aiming to produce.

### Process? How?

Well, each transaction refers to a single customer, and is either a `deposit` or a `withdrawal`.
You need to create a `Customer` for each customer you come across in the file.
Each customer will have some number of `Account`s as well.
You'll need to create a new `Account` for each account you come across that is tied to a given `Customer`.

Each row has an amount, and you need to add (deposit) or subtract (withdrawal) the amount from the customer's account.
_It is perfectly fine for a customer's account to have a negative balance_.
No need to worry about overdrafts(!).

Once you have a data structure in memory that contains all the customer's accounts, and all the transactions have been applied, you need to output a JSON file which shows all the customers, all their accounts, and their final balances after applying all the transactions in the file.

How? Up to you. But don't overthink it, you do this with just Core Python.

## What you end with

You need to create a couple Python classes that when you run the main method in one of your
classes, it produces as output, a new file `resources/results.json` which is __identical__ to the file `resources/target.json`.

That's it, that's all. Not complicated.

You need to get _no output at all_ from running the command
```
diff target.json results.json
```
in a terminal window. 
When you get no output at all, consider yourself complete.
__diff__ _is a command line program you can run to see all the differences between two text files._
In this case, we are using it to check on your created JSON file after all the transaction processing.

_(so yeah, you'll need to generate your `results.json` file and compare it to `target.json` using the __diff__ command in the terminal/shell)_

## Things you should consider

What does the data structure inside of `Customer` class look like? How do you model the `Account` class as well? How are `Customer` & `Account` related?

And what does class `Transaction` look like? How do you read in the text data, make a data structure (objects?) out of it, and then use that data structure to process each transaction, modifying each `Customer`'s `Account` as you handle each `Transaction`?

You might want to make a few unit tests, to make yourself certain that your `Transaction`, `Customer` and `Account` classes work like you expect them to.

Once you are generating the correct JSON file from the input data file, contact us and
we will run your code against a second set of input and compare the output to a second set of JSON output. If your code works correctly and produces the second JSON result from the second CSV input, you will pass the assessment.

You will get partial credit for work you attempt, and can, based on the discretion of the instructors, pass the assessment without producing perfect JSON output. 

Make it clean, elegant, and SOLID. Use everything thing you've learned.

## And Finally

Observe all the same rules and restrictions you had for the other two assessments.

Make _commits_ and _pushes_ throughout the day.

We want to see you write real Python code, code you are proud of.
