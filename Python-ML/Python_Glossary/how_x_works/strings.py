'''
capitalize(): Converts the first character of a string to uppercase and the rest to lowercase.

casefold(): Returns a casefolded version of the string, suitable for case-insensitive comparisons.

center(width, fillchar): Returns a centered string with the specified width, padded with a fill character (default is space).

count(substring, start, end): Returns the number of non-overlapping occurrences of a substring in the string.

encode(encoding='utf-8', errors='strict'): Returns an encoded version of the string using the specified encoding.

endswith(suffix, start, end): Checks if the string ends with the specified suffix.

expandtabs(tabsize=8): Returns a copy of the string with tab characters replaced by spaces.

find(substring, start, end): Returns the lowest index of the substring in the string, or -1 if not found.

format(*args, **kwargs): Formats the string with the specified values and placeholders.

format_map(mapping): Formats the string using the values from a mapping (dictionary).

index(substring, start, end): Returns the lowest index of the substring in the string, or raises a ValueError if not found.

isalnum(): Checks if all characters in the string are alphanumeric (letters and digits).

isalpha(): Checks if all characters in the string are alphabetic (letters).

isascii(): Checks if all characters in the string are ASCII characters.

isdecimal(): Checks if all characters in the string are decimal digits.

isdigit(): Checks if all characters in the string are digits.

isidentifier(): Checks if the string is a valid Python identifier.

islower(): Checks if all characters in the string are lowercase letters.

isnumeric(): Checks if all characters in the string are numeric characters.

isprintable(): Checks if all characters in the string are printable.

isspace(): Checks if all characters in the string are whitespace characters.

istitle(): Checks if the string follows title-casing rules (first letter of each word is capitalized).

isupper(): Checks if all characters in the string are uppercase letters.

join(iterable): Combines the elements of an iterable (e.g., a list) into a single string using the string as a separator.

ljust(width, fillchar): Returns a left-justified string with the specified width, padded with a fill character (default is space).

lower(): Converts all characters in the string to lowercase.

lstrip(chars): Removes leading characters (default is whitespace) from the string.

maketrans(x[, y[, z]]): Creates a translation table for use with translate().

partition(separator): Splits the string into three parts based on the first occurrence of the separator.

replace(old, new, count): Returns a string with occurrences of old replaced by new (optional count limits replacements).

rfind(substring, start, end): Returns the highest index of the substring in the string, or -1 if not found.

rindex(substring, start, end): Returns the highest index of the substring in the string, or raises a ValueError if not found.

rjust(width, fillchar): Returns a right-justified string with the specified width, padded with a fill character (default is space).

rpartition(separator): Splits the string into three parts based on the last occurrence of the separator.

rsplit(sep=None, maxsplit=-1): Splits the string into a list of words, starting from the right, using the specified separator.

rstrip(chars): Removes trailing characters (default is whitespace) from the string.

split(sep=None, maxsplit=-1): Splits the string into a list of words using the specified separator.

splitlines(keepends=False): Splits the string into a list of lines, optionally keeping line endings.

startswith(prefix, start, end): Checks if the string starts with the specified prefix.

strip(chars): Removes leading and trailing characters (default is whitespace) from the string.

swapcase(): Swaps the case of all characters in the string (e.g., 'Hello' becomes 'hELLO').

title(): Converts the string to title case (capitalizes the first letter of each word).

upper(): Converts all characters in the string to uppercase.

zfill(width): Pads the string with zeros on the left until it reaches the specified width.
'''
x = "x"
y = float(0.5)
z = 5
print(y)
# is 'hello'.equals("hello")?

#how to get the first char of string
w = "test"[0]
print(w)
replace_text = "ab#cd"

new_text = replace_text.replace("#", "$")
print(new_text)


