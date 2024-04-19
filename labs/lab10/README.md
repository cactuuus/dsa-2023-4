# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 10: Graphs & Breadth-first Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/README.md)
```shell
python labs 10*
```

Welcome to lab 10! First things first: If you haven't gone through
[lab 1](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md), then make sure to read through
what it says about getting your system ready for working on these labs. As a reminder, if you're on a lab machine you'll
need to first:
- Open the Software Hub and launch:
  - Python 3.11.3
  - PyCharm Community Edition
  - Git for Windows
- Open PowerShell and run:
  - `pip install textual`
  - If you haven't cloned this repository before, then:
    - `cd N:/`
    - `git clone https://github.com/bertie-wheen/dsa-2023-4 dsa`
    - `cd dsa`
  - If you have, then:
    - `cd N:/dsa`
    - `git pull`
    - If you get an error "fatal: detected dubious ownership in repository ..." (which you likely will),
      then run the command it recommends, which is:
      - `git config --global --add safe.directory '%(prefix)///smbhome.uscs.susx.ac.uk/<username>/dsa'`
        (where `<username>` is your username)
      - Then again run `git pull`
- Open PyCharm and:
  - Open the `labs/` directory (i.e. `N:/dsa/labs/`) as a project
  - Switch the scope to "Exercises & Solutions" or "Exercises, Solutions & Notes" by clicking on the word "Project"
    above the directory tree in the left sidebar

There's a great setup guide (thanks to Joshua Kybett) about all of this (with screenshots and extra tips) available on
Canvas, which is worth a read-through (particularly if you don't understand a step or are having problems). There's
also a Mac-specific guide on Canvas for those of you who need it (thanks to Val Knight).

---

Another little reminder from lab 1:

Sometimes, you may want to not just run the test suite, but load the file you're working on into the Python REPL and
play around with it. To do this, first open PyCharm's Python Console, which you can do by going to the top menu and
selecting `Tools -> Python or Debug Console`, or by clicking the little Python icon in the bottom-left (that is, towards
the bottom of the left bar). Then run e.g. `from lab10.core.graph.exercise import *` (changing the lab number
and exercise name to whatever you're working on), after which you'll be able to run things like
```pycon
>>> a = Vertex(1)
>>> b = Vertex(2)
>>> c = Vertex(3)
>>> d = Vertex(4)
>>> e = Vertex(5)
>>> f = Vertex(6)
>>> g = Vertex(7)
>>> from lib.iterator import iterator
>>> graph = Graph(
...     iterator(a, b, c, d, e, f, g),
...     iterator(
...         Edge(a, b, None),
...         Edge(b, d, None),
...         Edge(b, e, None),
...         Edge(d, a, None),
...         Edge(d, e, None),
...         Edge(e, d, None),
...         Edge(f, c, None),
...     ),
... )
>>> graph.degree(b)
2
>>> for vertex in graph.neighbours(b):
...     print(vertex.get_item())
...
4
5
```

---

- [Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/core/README.md)
  - Graphs
  - Breadth-first Search
- [Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/plus/README.md)
