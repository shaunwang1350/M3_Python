# M3_Python Challenge
## Objectives

* Calculate the oter turnout for each county as well as the percentage of votes each county contributed to the eleciton
* Determine which country had the largest turnout.
* Save the results to output file (election_results.txt)

## Summary

The following summarizes the general logic of PyPoll_Challenge.py:

*Imports / Paths / Declarations

    *The code begins by importing modules and creating relative path variables. Followed by declaring variables needed for later.

*Input

    *The code states a 'with' function to retrieve data from input file (election_results.txt) 
    *The code traverse through the rows within the input data inorder to get totalvotes, candidate names, county names, and the count of votes for each variable.
    *The code retrieves possible candidate options, and create a dictionary for each. Then the value for each candidate key-pair dict is incremented.
    *Similar to the candidate code above, the following code retrievies possible county options and creates a dictionary for each. hen the value for each candidate key-pair dict is incremented.

*Output

    *The code ends the previous 'with' function and begins a new 'with' function inorder to write an output data.
    *The code prints and writes previous variables into analysis.txt, as it traverses through existing county and candidate options (list variable) inorder to select winner for each. 
    *It then write/print out each candidate/county's count and percentage of vote.
    *The code creates print/write strings for election results, and total votes.
    *The code loops through the county dictionary to create vote percentages. Then county vote and county vote percentages are compared to select the largest. The winner is then printed/written out in a summary variable.
    * Similar to above, the code loops through candidate dictionary to create vote percentages. Then candidate vote and candidate vote percentages are compared to select the largest. The winner is then printed/written out in a summary variable.

## Notes:
*Added dashs variable to standardize all dash lengths.
*Added end='' at every print statement inorder to prevent double lines when printing from terminal.
