#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This would be O(n) //linear: The while loop only has one operation. 


b) This would be O(n^c) //quadratic time
    The algorithm increases the number of operations it performs as a quadratic function of the input size n. 
    The number of operations increases quickly.

    This would be like creating a family tree with different inherited traits. 
    It will get out of hand quickly and will quickly contain a lot of info and a lot of extra work with each additional branch. 


c) this would be O(n) //linear : 
    There is only one operation being run. 
    The algorithm increases the number of operations it performs as a linear function of the input size n. 

    The number of additional operations the algorithm needs to perform grows in direct proportion to the increase in input size n.
    This would be like adding pennies to a jar one at a time. The amount of time it takes to complete the operation is directly related to how many
    pennies there are to add to the jar. 


## Exercise II

If I have a certain number of floors and I am trying to figure out where the "break point" {no pun intentended} is to see where the eggs will break,
I'd split the number of floors in half and start from there. 

If I have 10 floors, I'd start at the 5th floor. If I drop an egg from there and it doesn't break, I'd split the top 5 in half and go up to the 7th floor and drop it. If it breaks at 
7 but didn't at 5 then 6 is the floor. 

But, if it broke at 5, I would split the bottom 5 in half and go to the 2nd floor to drop an egg. If it doesn't break, I'd go up to the 4th floor. 
If it breaks there, I'd go down to 3rd floor. If it doesn't break there, that is the floor. 

Regardless of the number of floors, I'd split the floors and continue to split the floors in a "binary search tree" until I found the "f-floor".

The run time complexity would be O(log(n)): //Logorithmic time
    The algorithm increases the number of operations it performs as the logarithmic function of the input size n.

    The function log n grows very slowly. As n gets larger, the number of operations the algorithm needs to perform does not increase by very much. It tapers off. 

    This would also be like kooking something up in the dictionary.
    We don’t start from the beginning and work our way through. We have a general idea of where
    the word is that we are looking for. We can skip to the general location. 


