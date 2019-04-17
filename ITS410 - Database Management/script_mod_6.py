# !/bin/python
# Author : Ismail Elmaliki, ITS 410 Module 6
# import MySQL connector
import mysql.connector

# connecting to MySQL database w/ credentials
conn = mysql.connector.Connect(host="localhost", user="jump",
	password="start", database="classicmodels")


cursor = conn.cursor()

# First query - original cost
query_one = (
	     "SELECT " 
		"p.paymentDate, p.amount, c.contactFirstName, c.contactLastName "
	     "FROM " 
		"customers AS c JOIN payments as p ON c.customerNumber = p.customerNumber " 
	     "WHERE " 
		"MONTH(p.paymentDate) = 12 "
	     "ORDER BY "
		 "p.paymentDate"
)

cursor.execute(query_one)

# Display first query before applied 1% discount
print("Before 1% Discount\n-------------------------------------------")
print("PaymentDate\tAmount\t\tFull Name")
for (paymentDate, amount, contactFirstName, contactLastName) in cursor:
     str_var = str(amount)
     if len(str_var) <= 7:
	 print("{}\t{}\t\t{} {}".format(paymentDate, amount, contactFirstName, contactLastName))
     else:
	print("{}\t{}\t{} {}".format(paymentDate, amount, contactFirstName, contactLastName))

# Second query with discount applied
query_two = (
	   "SELECT "
	    	"p.paymentDate, round(p.amount * (99/100),2) as reducedAmount, " 
		"c.contactFirstName, c.contactLastName "
	   "FROM " 
		"customers AS c "
		"JOIN payments as p "
		"ON c.customerNumber = p.customerNumber "
	   "WHERE "
		"MONTH(p.paymentDate) = 12 "
	   "ORDER BY "
		"p.paymentDate;"
 )

cursor.execute(query_two)

# Displays reduced amount with 1% discount applied to prices
print("\nAfter 1% Discount\n-------------------------------------------")
print("PaymentDate\tReduced Amount\tFull Name")
for (paymentDate, reducedAmount, contactFirstName, contactLastName) in cursor:
     str_var = str(reducedAmount)
     if len(str_var) <= 7:
	 print("{}\t{}\t\t{} {}".format(paymentDate, reducedAmount, contactFirstName, contactLastName))
     else:
	print("{}\t{}\t{} {}".format(paymentDate, reducedAmount, contactFirstName, contactLastName))

# Clean up and close database connection
cursor.close()
conn.close()
