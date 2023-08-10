# 0x00. Python - Hello, World
## 10-check_cycle.c, lists.h
done but with 2 efficiency fails
## 100-write.py 
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

- Use the function write from the sys module
- You are not allowed to use print
- Your script should print to stderr
- Your script should exit with the status code 1

https://www.youtube.com/watch?v=5za6eRdHjpw

- stdin 
- stdout
- strerr
## 101-compile
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
## 102-magic_calculation.py
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
~~~bash
 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
~~~

- Disassembler for Python bytecode https://docs.python.org/3.4/library/dis.html
