# Fastapi Commands

> python3 -m pip --version
> python3 -m venv fastapienv
> source venv/bin/activate
> deactivate
> source fastapienv/bin/activate
> pip install "fastapi[standard]"
> fastapi dev books.py
> fastapi dev book2.py
> uvicorn books2:app --reload
> uvicorn main:app --reload
> pip install sqlalchemy
> brew install sqlite3

~/projects/fastapi/TodoApp (main*) » sqlite3 todos.db
SQLite version 3.51.0 2025-06-12 13:14:41
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE todos (
        id INTEGER NOT NULL, 
        title VARCHAR, 
        description VARCHAR, 
        priority INTEGER, 
        complete BOOLEAN, 
        PRIMARY KEY (id)
);
sqlite> .tables
sqlite> .schema
sqlite> .exit

CREATE INDEX ix_todos_id ON todos (id);
sqlite> insert into todos (title, description, priority, complete) values ("Go to the store", 'pick up eggs', 5, False);

sqlite> select * from todos;
1|Go to the store|pick up eggs|5|0


sqlite> insert into todos (title, description, priority, complete) values ("Cut the lawn", 'Grass is getting long', 3, False);
sqlite> select * from todos;                                                                              

1|Go to the store|pick up eggs|5|0
2|Cut the lawn|Grass is getting long|3|0

 
sqlite> insert into todos (title, description, priority, complete) values ("Feed the dog", 'He is getting hungry', 5, False);

> sqlite> .mode column
> sqlite> select * from todos;

id  title            description            priority  complete
--  ---------------  ---------------------  --------  --------
1   Go to the store  pick up eggs           5         0       
2   Cut the lawn     Grass is getting long  3         0       
3   Feed the dog     He is getting hungry   5         0       

> sqlite> .mode markdown
> sqlite> select * from todos;

| id |      title      |      description      | priority | complete |
|----|-----------------|-----------------------|----------|----------|
| 1  | Go to the store | pick up eggs          | 5        | 0        |
| 2  | Cut the lawn    | Grass is getting long | 3        | 0        |
| 3  | Feed the dog    | He is getting hungry  | 5        | 0        |


> sqlite> .mode table
> sqlite> select * from todos;

+----+-----------------+-----------------------+----------+----------+
| id |      title      |      description      | priority | complete |
+----+-----------------+-----------------------+----------+----------+
| 1  | Go to the store | pick up eggs          | 5        | 0        |
| 2  | Cut the lawn    | Grass is getting long | 3        | 0        |
| 3  | Feed the dog    | He is getting hungry  | 5        | 0        |
+----+-----------------+-----------------------+----------+----------+
