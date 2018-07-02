# SimpleSearch

A simple search engine using only python3 native libs.

## Getting Started

For running the system, no setup is necessary, just run the server script and the search will be up and running.

### Prerequisites

**python3**: any version of python 3 with no additional libs.

**port 9001** available: The server will run over port 9001 

### How to query

Run the server.py script to index all the files inside the data folder and run the engine.
Then, *on a separate terminal*, run "search.py <query>" to query the search engine and print the results.

***example***
```
python3 server.py
Starting server at localhost:9001
Waiting for connections...
```
```
python3 search.py "Walt disney"

Foram encontradas 53 ocorrências pelo termo: "Walt disney"
data\a-cowboy-needs-a-horse.txt
data\alice-and-the-three-bears.txt
data\alice-helps-the-romance.txt
data\alice-s-fishy-story.txt
data\alpine-climbers.txt
data\billposters.txt
...
```

In unix based systems, can use the "time" command to check the time taken for the search to respond. 

```
time python3 search.py "alien"
Foram encontradas 12 ocorrências pelo termo: "alien"
data/alien-apocalypse.txt
data/alien-origin.txt
...
data/sex-files-alien-erotica-ii.txt
data/time-enough-the-alien-conspiracy.txt

real	0m0,039s
user	0m0,034s
sys	0m0,004s

```

## How to run the tests

The tests for the server and the engine run indepentently.
For each test case, it's necessary to just run the test script.

```
 python3 test_engine.py
 ..
 ----------------------------------------------------------------------
 Ran 2 tests in 0.002s
 
 OK
```
```
python3 test_server.py
/mnt/c/Users/Urso/PycharmProjects/simpleSearch/server.py:15: ResourceWarning: unclosed <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Starting server at localhost:9002
Waiting for connections...
Results: 0. Time spent: 501
.
----------------------------------------------------------------------
Ran 1 test in 3.007s

OK
```
