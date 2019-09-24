<center>

# 1st Assignment

</center>

## Intro

This program finds the **optimal path of a graph**.

It also calculates the path that a person will get, influenced by the **present bias** (*Behavioral Economics*).

## A few words about the Present Bias

Suppose we have a graph beginning with *s* and ending with *t*.

The available paths from point s to point t are as follows:

+ *s-a-b-t* at a cost of 16+2+2 = 20
+ *s-c-d-t* at a cost of 8+8+8 = 24
+ *s-c-e-t* at a cost of 8+2+16 = 26

The person who is influenced by the present bias, when he is in a node, estimates the cost of the nodes adjacent to the node with a cost degraded by a factor of b<1 and so the cost is:

With b=1/2 the person will take:

1. At the beginning of the node you calculate the cost of the paths:

    + *s-a-b-t* at a cost of 16+(1/2)*2+(1/2)*2 = 20
    + *s-c-d-t* at a cost of 8+(1/2)*8+(1/2)*8 = 24
    + *s-c-e-t* at a cost of 8+(1/2)*2+(1/2)*16 = 26

    and selects the node **c**

2. Starting from node c, calculates:

    + *c-d-t* at a cost of 8+(1/2)*8 = 12
    + *c-e-t* at a cost of 2+(1/2)*16 = 10

    and selects the node **e**

Based on factor b the person will choose *s-c-e-t* at a cost of 26.

## Description

The purpose of the program is, given a graph and a parameter b, to calculate the optimal path and path that a person will be affected by present bias.

The process of executing the program is:

1. Clone the repository
2. cd `../assignment-2018-1`
3. Type python present_bias.py <input_file> <bias_parameter> <start_node> <end_node>
    + `input_file` The file name which include the graph (see the examples example_1 | example_2 | example_3). 
    + `bias_parameter` The parameter b
    + `start_node` The starting node for example "s"
    + `end_node` The ending node for example "e"
