'''
CTEC 121 - Lab No. 5

Overview: This lab will have students work with the TextBlob library
TextBlob library documentation - https://textblob.readthedocs.io/en/dev/

================================================================================
PLEASE CAREFULLY READ THROUGH ALL OF THE INSTRUCTIONS PRIOR TO STARTING THIS LAB
================================================================================

Step 1: Install the textblob library:

School computers: pip3.7 install textblob
Persoanl computers: pip3.8 install textblob

Step 2: Edit the text file and name it texttoprocess.txt
Step 3: In the texttoprocess.txt file, create 10 meaningful sentences about random topics. Make sure each sentence has 8 - 15 words. Press enter after each sentence. Make sure to save the file.
Step 4: Follow the instructions in the code below

'''

# PLACE YOUR NAME HERE

import time
from textblob import TextBlob


def main():
    '''
    1) Open the texttoprocess.txt file for read access and assign it to a meaningful variable name

    2) Open a file named results.txt for write access and assign it to a meaningful variable name

    3) Create code that will read in one line at a time from the texttoprocess.txt file

    4) With each line of text read from the file, calculate the sentences "polarity" and "subjectivity"

    5) Make sure to strip off the line feed at the end of each line

    6) Use the documentation on the TextBlob site to figure out how to do this

    7) You also need to calculate the average polarity and subjectivity and display it at the end of the program

    8) Write out the following string as the first line of the results.txt file:
       Polarity,Subjectivty,Text

    9) You need to write the polarity, subjectivty and the text of the sentence to the results.txt file. Each should be separated by a comma. This format is known in industry as CSV (Comma Separated Value) 

    10) Close both files after they have been read through.

    11) Once you have read through all of the text from texttoprocess.txt, calculate and display the average polarity and subjectivity and display it.

    12) Show the instructor your results.

    13) Clone this repository back to GitHub for review and grading.
    '''

    # YOUR CODE GOES HERE


main()
