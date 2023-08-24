#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name_searched".format(sys.argv[0]))
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Use parameterized query to ensure the input is treated as data and not as part of the query
        query = "SELECT cities.name FROM cities LEFT JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"
        
        results = cursor.execute(query, (state_name_searched,))

        # Fetch and display the results
        print(results)
    
    
    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        if db:
            db.close()
