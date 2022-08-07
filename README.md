# Coffee_Bootcamp
Data_Science_Assignments

Basic Python
1. Write a Python program which accepts the user's first and last name and prints them in
reverse order with a space between them.
2. Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
3. Write a Python program to display the first and last colours from the following list.
color_list = ["Red","Green","White" ,"Black"]
4. Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).
Sample function : abs()
Expected Result : mat
abs(number) -> number
Return the absolute value of the argument.
5. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
6. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
7. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
8. Write a Python program to create a histogram from a given list of integers.
9. Write a Python program to concatenate all elements in a list into a string and return it.
10. Write a Python program to print out a set containing all the colors from color_list_1 which are
not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
11. Write a Python program to check whether a file exists.
12. Write a python program to call an external command in Python.
13. Write a Python program to find out the number of CPUs using.
14. Write a Python program to list all files in a directory in Python.
15. Write a python program to access environment variables.
16. Write a Python program to get the current username
17. Write a program to get execution time for a Python method.
18. Write a Python program to get an absolute file path.
19. Write a Python program to get file creation and modification date/times.
20. Write a Python program to sort three integers without using conditional statements and
loops.
21. Write a Python program to sort files by date.
22. Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script.
23. Write a Python program to find the available built-in modules.
24. Write a Python program to get the size of an object in bytes.
25. Write a Python program to get the current value of the recursion limit.
26. Write a Python program to count the number occurrence of a specific character in a string.
27. Write a Python program to get the system time.
28. Write a Python program to clear the screen or terminal.
29. Write a Python program to get the name of the host on which the routine is running.
30. Write a Python program to access and print a URL's content to the console.
Python Data Structure
Array
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
2. Write a Python program to reverse the order of the items in the array.
3. Write a Python program to get the number of occurrences of a specified element in an
array.
4. Write a Python program to remove the first occurrence of a specified element from an
array.
Dictionary
1. Write a Python script to sort (ascending and descending) a dictionary by
value.
2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
3. Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
4. Write a Python program to iterate over dictionaries using for loops.
5. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
6. Write a Python program to remove a key from a dictionary.
7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
9. Write a Python program to print a dictionary in table format.
10. Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
11. Write a Python program to convert a list into a nested dictionary of keys.
12. Write a Python program to check multiple keys exists in a dictionary.
13. Write a Python program to count number of items in a dictionary value
that is a list.
Sets
1. Write a Python program to create a set.
2. Write a Python program to iteration over sets.
3. Write a Python program to add member(s) in a set.
4. Write a Python program to remove item(s) from set
5. Write a Python program to remove an item from a set if it is present in the set.
6. Write a Python program to create an intersection of sets.
7. Write a Python program to create a union of sets.
8. Write a Python program to create set difference.
9. Write a Python program to create a symmetric difference.
10. Write a Python program to clear a set.
11. Write a Python program to use of frozensets.
12. Write a Python program to find maximum and the minimum value in a set.
List
1. Write a Python program to sum all the items in a list.
2. Write a Python program to multiplies all the items in a list.
3. Write a Python program to get the smallest number from a list.
4. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
5. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
6. Write a Python program to remove duplicates from a list.
7. Write a Python program to clone or copy a list.
8. Write a Python program to find the list of words that are longer than n from a
given list of words.
9. Write a Python function that takes two lists and returns True if they have at
least one common member.
10. Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
11. Write a Python program to generate all permutations of a list in Python.
12. Write a Python program to get the difference between the two lists.
13. Write a Python program to append a list to the second list.
14. Write a python program to check whether two lists are circularly identical.
15. Write a Python program to find common items from two lists.
16. Write a Python program to split a list based on first character of word.
17. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
Tuple
1. Write a Python program to create a tuple.
2. Write a Python program to create a tuple with different data types.
3. Write a Python program to unpack a tuple in several variables.
4. Write a Python program to create the colon of a tuple.
5. Write a Python program to find the repeated items of a tuple.
6. Write a Python program to check whether an element exists within a tuple.
7. Write a Python program to convert a list to a tuple.
8. Write a Python program to remove an item from a tuple.
9. Write a Python program to slice a tuple.
10. Write a Python program to reverse a tuple.
Strings
1. Write a Python program to calculate the length of a string.
2. Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
3. Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
4. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
5. Write a Python function that takes a list of words and returns the length of the longest
one.
6. Write a Python script that takes input from the user and displays that input back in
upper and lower cases.
7. Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
8. Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
9. Write a Python program to display formatted text (width=50) as output.
10. Write a Python program to count occurrences of a substring in a string.
11. Write a Python program to reverse a string.
12. Write a Python program to lowercase first n characters in a string.
