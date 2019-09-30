# 3rd Assignment

## Intro

This program Simplifies an Evaluation Norm.

### Evaluation Norms

With a dono and the recipient, we want to illustrate the ways in which the donor's reputation will be affected by the choice to make a transaction with the recipient. 

We have four factors to consider:

* Choosing the donor, to help or not to help.
* The donor's current reputation, good or bad.
* The recipient's current reputation, good or bad.
* The previous reputation of the recipient, good or bad.

The references can be assigned to a binary variable as follows:

* If the donor choose to help **A=1**, and if not **A=0**.
* If the donor has good current reputation **B=1**, and if not **B=0**.
* If the recipient has good current reputation **C=1**, and if not **C=0**.
* If the recipient has good previous reputation **D=1**, and if not **D=0**.

Thus we have 16 different combinations of A, B, C, D describing a transaction between donor and recipient, as shown in the following figure.

In any combination now, we can give a value of 1 if the donor's reputation is good as a result of the transaction, and a value of 0 if the donor's reputation is bad as a result of the transaction. This way fills the above shape.


![](./images/sample.png)


## Description

 The purpose of the program is, given a Evaluation Norm, to Simplify the Norm.

 The process of executing the program is:

 1. Clone the repository
 2. cd `../assignment-2018-3`
 3. Type `python boolean_complexity.py <list of values>`
    + `<list of values>` is a series of integers corresponding to the positions of the square where we set the value 1. We take each value and convert it to a four-bit binary number, eg **b*1*b*2*b*3*b*4***.
    We find the point of the square with coordinates **A=b*1***, **B=b*2***, **C=b*3***, **D=b*4***.

The output of the program will be the simplified binary representation that describes the norm and its complexity.




