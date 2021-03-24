"""
What is PIP?
PIP is a package manager for Python packages, or modules if you like.

Full form of PIP is Pip Installs Python or PIP Installs Packages Alternatively,
 pip stands for "preferred installer program".

Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.
"""

# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following:
#
# Example
# Check PIP version:
#
# NOTE: This is for windows
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# Install PIP
# If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

# Download a Package
# Downloading a package is very easy.
#
# Open the command line interface and tell PIP to download the package you want.
#
# Navigate your command line to the location of Python's script directory, and type the following:

# Download a package named "camelcase":
#
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase


"""Linux installation of pip3"""
# To install pip3 on Ubuntu or Debian Linux, open a new Terminal window and enter sudo apt-get install python3-pip .
# To install pip3 on Fedora Linux, enter sudo yum install python3-pip into a Terminal window.
# You will need to enter the administrator password for your computer in order to install this software.
# type at terminal to confirm $ pip3 --version

# First you have to download the camelcase package using pip3
# in terminal type:
# $ pip3 install camelcase
# once it has successfully installed the proceed

# Using a Package
# Once the package is installed, it is ready to use.
#
# Import the "camelcase" package into your project.

# Import and use "camelcase":
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
# This method capitalizes the first letter of each word.


# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package
# Use the uninstall command to remove a package:

# Example
# pip3 uninstall camelcase
# The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:
# Press y and the package will be removed.

# List Packages
# Use the list command to list all the packages installed on your system:
# pip3 list
