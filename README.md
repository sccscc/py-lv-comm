# Python-LabVIEW Communication
---

Scripts to communicate between Python and LabVIEW

**Application example:** You have some nice scripts written in Python and want to exploit the easy GUI-creation in LabVIEW to display results from the Python scripts. Or maybe you already have a LabVIEW program and want to extend its capabilities using Python.

## Features
* You can do virtually anything you could do from a Python terminal
* You can interact with a "living" Python program. You can e.g. create and manipulate objects.

## Requirements
* Python 3
* LabVIEW 2013
* [ZeroMQ](http://zeromq.org/)
  * [For Python](http://zeromq.org/bindings:python) (can be installed via pip)
  * [For LabVIEW](http://zeromq.org/bindings:labview)
 
## Examples
### py-server_lv-client_simple
A very simple example, demonstrating the communication between Python and LabVIEW. 
* Start the Python-server and the LabVIEW-client. 
* Send the command `test()` from LabVIEW to Python. It should return "*It works!*"
* You can add more functions in the Python script that you can then call from LabVIEW.

### py-server_lv-client
 A more advanced example, demonstrating handling of standard data types + numpy arrays.
 * Start the Python-server (*py-lv-comm_python-server.py*) and the LabVIEW-client (*py-lv-comm_labview-client.vi*).
 * You can either send a command directly from LabVIEW or read various data types using the corresponding buttons.
   * The Python script creates an object called *test*. Type e.g. `test.var_int` and hit *Read Int* in LabVIEW to read the value of the variable *test.var_int*.
   * Look into the Python scripts for more variables and methods. It is self-explaining.
