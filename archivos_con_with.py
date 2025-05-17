# Opens a file using the with statement
with open('UPS_DOT_EMPLOYEES_REPORT.txt', 'r', encoding='utf8') as file:
   lines_list = file.readlines()

# Creaton of a new list
new_IDs_list = []

# Iterates each read line
for line in lines_list:
   position = lines_list.index(line)
   if position == 0:
       line = f"'{line.strip()}'" #strip is the equivalent to trim in other languages
       new_IDs_list.append(line)
   else:
       line =f",'{line.strip()}'"
       new_IDs_list.append(line)

# Writing the output file
with open('output/employees_list.txt', 'w', encoding='utf8') as file:
   for line in new_IDs_list:
       file.write(line + "\n")


