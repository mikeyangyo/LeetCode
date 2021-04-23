# 83. Remove Duplicates from Sorted List
Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return the *linked list **sorted** as well*.

## **Example 1**
```
Input: head = [1,1,2]
Output: [1,2]
```

## **Example 2**
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
``` 

## **Constraints**
- The number of nodes in the list is in the range `[0, 300]`.
- `100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## **Solution Idea**
Just check wether next node's value is same with current node's value.
if they are same, just skip next nodes util next node's value is not same with current node's value.