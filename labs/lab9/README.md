# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md)
```shell
python labs 9*
```

Welcome to lab 9! First things first: If you haven't gone through
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
the bottom of the left bar). Then run e.g. `from lab9.core.unsorted_list_priority_queue.exercise import *` (changing the lab number
and exercise name to whatever you're working on), after which you'll be able to run things like
```pycon
>>> priority_queue = UnsortedListPriorityQueue()
>>> priority_queue.get_length()
0
>>> priority_queue.insert(12, "%")
>>> priority_queue.insert(11, "-")
>>> priority_queue.insert(3, "or")
>>> priority_queue.insert(5, "not")
>>> priority_queue.insert(12, "*")
>>> priority_queue.insert(4, "and")
>>> priority_queue.insert(11, "+")
>>> priority_queue.insert(12, "/")
>>> priority_queue.insert(14, "**")
>>> priority_queue.insert(12, "//")
>>> for priority, item in priority_queue.iterator():
...     print(f"precedence: {priority} -- operator: {item}")
...
precedence: 14 -- operator: "**"
precedence: 12 -- operator: "%"
precedence: 12 -- operator: "*"
precedence: 12 -- operator: "/"
precedence: 12 -- operator: "//"
precedence: 11 -- operator: "-"
precedence: 11 -- operator: "+"
precedence: 5 -- operator: "not"
precedence: 4 -- operator: "and"
precedence: 3 -- operator: "or"
>>> priority_queue.get_length()
10
```

---

- [Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md)
  - Heap Sort
  - Binary Heaps
  - Unsorted List Priority Queues
  - Sorted List Priority Queues
  - AVL Tree Priority Queues
  - Binary Heap Priority Queues
- [Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/plus/README.md)
  - Median Maintenance
  - Huffman Revisited
