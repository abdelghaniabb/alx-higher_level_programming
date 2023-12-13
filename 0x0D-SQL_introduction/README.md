# 0x0D. SQL - Introduction

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


