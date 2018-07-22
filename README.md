# Server mutiple executor

Traditionally, a test platform only executes test case one after another.
Saying, we have 4 test cases, it spends 5 minutes to execute one in average. To run 4 of them, we need 20 minutes.
When worked as a leader, I had to consider the cost of functional, so why not created an agent. This agent can run test instead of test platform.

This is the idea of shortening test time, but this is not the originally method which used in Celestica.
I’ll use Mongo database to store test log and python which cause less confusion.

I assumed that no one would have the same requirement as me, nobody would be interested with this code.
