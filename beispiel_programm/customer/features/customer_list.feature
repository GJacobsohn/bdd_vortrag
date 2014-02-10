Feature: All Customers should be display in a sortable Table



Scenario: On the first load all customer should be sorted by last name

Given: there are the following Customers in the Database:
       | id | first_name | last_name |
       | 1  | Gabriel    | Jacobsohn |
       | 2  | Mike       | Hansen    |
       | 3  | Michel     | Zerdan    |
   And: I'm in the Customer section
When: I'm doing nothing
Then: The table "customer_list" should be:
       | id | name                  |
       | 3  | Michel Zerdan         |
       | 2  | Mike Hansen           |
       | 1  | Gabriel Jacobsohn     |




