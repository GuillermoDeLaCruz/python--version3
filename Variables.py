"""
NAMING AND USING VARIABLE

When you're using variables in Python, you need guidelines.
Breaking some of these rules will cause errors; other
guidelines just help you write code that's easier to read and
understand. Be Sure to keep the following variable rules in mind:

I. Variable names can contain only letters, numbers, and underscores.
   They can start with a letter or an underscore, but not with a number.
   For instance, you can call a variable message_1 but not 1_message.

II.Spaces are not allowed in variable names, but underscores can be used to
   separate words in variable names. For example, greeting_message works,
   but greeting message will cause errors.

III.Avoid using Python keywords and function names as variable names; that is,
    Do not use words that Python has reserved for a particular programmatic purpose,
    such as the word print.

IV. Variable names should be short but descriptive. For example, names is better than n,
    student_name is better than s_n and name_length is better
    than length_of_persons_name.

V.  Be careful when using the lower l and upper O
    because they could be confused with the name 1 and 0.


"""


message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)