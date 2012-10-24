To build and view notes on Ubuntu:

0) python should already be installed.

1) install pip, the python package manager:
    sudo apt-get install pip

2) install sphinx and the sphinx block diagram plugin:
    sudo pip install sphinx sphinxcontrib-blockdiag

3) while in this directory, run:
    make html

4) now you can view the generated HTML in a browser, for example by running this command inside this directory:
    yourbrowsername _build/html/index.html
