
# Project: 0x0D. SQL - Introduction
- A solid database is expected to be **acid**, which means it guarantees:
    - Atomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
    - Consistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
    - Isolation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
    - Durability: unplug your server at any time, boot it back up, and it didn’t lose any data.

- ACID is a cool acronym! CRUD is another cool one

    - Create some data;
    - Read some data;
    - Update some data;
    - Destroy some data.

- Acronyms
    - DDL Data Definition Language
    - SQL Structured Query Language
    - DML Data Manipulation Language

- What is a relational database? (please select all correct answers)
    - a collection of data
    - a table containing only one object representation
    - data are organized by tables, records and columns
    - a database
    - data are organized by tables and indexes
    - a table containing multiple object representation
    - married databases



## Resources

#### Read or watch:

* [What is Database & SQL?](https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw)
* [A Basic MySQL Tutorial](https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
* [Basic SQL statements: DDL and DML](https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
* [Basic queries: SQL and RA](https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
* [SQL technique: functions](https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
* [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
* [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw)
* [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)
* [installing MySQL in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ)
## Learning Objectives

### General

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does <code>DDL</code> and <code>DML</code> stand for
* How to <code>CREATE</code> or <code>ALTER</code> a table
* How to <code>SELECT</code> data from a table
* How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data
* What are <code>subqueries</code>
* How to use MySQL functions
## Tasks

| Task | File |
| ---- | ---- |
| 0. List databases | [0-list_databases.sql](./0-list_databases.sql) |
| 1. Create a database | [1-create_database_if_missing.sql](./1-create_database_if_missing.sql) |
| 2. Delete a database | [2-remove_database.sql](./2-remove_database.sql) |
| 3. List tables | [3-list_tables.sql](./3-list_tables.sql) |
| 4. First table | [4-first_table.sql](./4-first_table.sql) |
| 5. Full description | [5-full_table.sql](./5-full_table.sql) |
| 6. List all in table | [6-list_values.sql](./6-list_values.sql) |
| 7. First add | [7-insert_value.sql](./7-insert_value.sql) |
| 8. Count 89 | [8-count_89.sql](./8-count_89.sql) |
| 9. Full creation | [9-full_creation.sql](./9-full_creation.sql) |
| 10. List by best | [10-top_score.sql](./10-top_score.sql) |
| 11. Select the best | [11-best_score.sql](./11-best_score.sql) |
| 12. Cheating is bad | [12-no_cheating.sql](./12-no_cheating.sql) |
| 13. Score too low | [13-change_class.sql](./13-change_class.sql) |
| 14. Average | [14-average.sql](./14-average.sql) |
| 15. Number by score | [15-groups.sql](./15-groups.sql) |
| 16. Say my name | [16-no_link.sql](./16-no_link.sql) |
| 17. Go to UTF8 | [100-move_to_utf8.sql](./100-move_to_utf8.sql) |
| 18. Temperatures #0 | [101-avg_temperatures.sql](./101-avg_temperatures.sql) |
| 19. Temperatures #1 | [102-top_city.sql](./102-top_city.sql) |
| 20. Temperatures #2 | [103-max_state.sql](./103-max_state.sql) |

