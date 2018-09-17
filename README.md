# Paxos

## Getting started

You can get up and running by just running `./bootstrap.sh`.

It will start:

 - 1 Proposer/Leader
 - 3 Acceptors
 - 1 Learner

Then you can call them using `client.py` by running 

```
python3 client.py
```

Check out these resources for more information:

 - https://en.wikipedia.org/wiki/Paxos_(computer_science)#Phase_2b:_Accepted
 - https://www.datastax.com/dev/blog/lightweight-transactions-in-cassandra-2-0
 - http://www.cs.utexas.edu/users/lorenzo/corsi/cs380d/past/03F/notes/paxos-simple.pdf