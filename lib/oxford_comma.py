def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]


#check if the length is 0 or 1: if length is 0, return empty string
#if length is 1, return the only element as a string
# if > 1, create a new empty array to store the result
# #iterate over items(array of strings) using a loop
#append each element to the result string, followed by a comma and space
#if the element is the second to last element, append "and" instead of a comma and a space
#append last element to the string
#return the string

