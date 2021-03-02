# Import Library

import psycopg2
from psycopg2 import Error

# Complete the function to create connection


def getConnection():
    # Write Your Code Here


def closeConnection(connection):
    connection.close()
    print("Connection is Closed")


def getCustomer(customer_id):
    try:
        connection = getConnection()  # Create a connection using the connection function
        # Write Your Code Here - Create a cursor object from the connection

        # Write Your Code Here - Create a query variable, by writing a SELECT query to fetch the customer using the customer_id as the filter.

        cursor.execute(query, (customer_id,))
        # Write Your Code Here - Create an object that will hold the records, Hint use fetchall()

        print("Printing Records")

        """Write Your Code Here - Using a for loop, iterate through the records to print each record instance of the customer table. 
        Example of the print statement - print("Customer ID", row[0])
        Check the table in your pg admin to know all the records you will print out.
        For Example -  print("Address ID", row[5]) is a record instance of the address_id column
        """"
        closeConnection(connection)  # Closes the connection
    except Error as e:
        print("Error: Reading Record")


# Using the getCustomer function, print out the customer information for customer_id = 34
getCustomer()
