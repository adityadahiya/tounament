=> Swiss Tournament Results
# tournament.py - 

Contains the implementation for the Swiss tournament
# tournament.sql - 

Contains the SQL queries to create the database, tables and views 
# tournament_test.py - 

Contains the test cases for tournament.py
=> To run this project:
1. Start Vagrant
  2. Open Terminal or cmd and browse to the vagrant folder
 and copy this tournament folder into it. 3. Type vagrant up and hit enter 
4. type vagrant ssh and hit enter 5. write psql and hit enter.
6. connect to the database by using \c tournament command. 7. type \q to quit out of PSQL 
8. Change the path to the correct directory by using cd /vagrant/tournament
9. Run the tests
  in the terminal by typing - python tournament_test.py


## Expected Outcome -> 

Success!  All tests pass!