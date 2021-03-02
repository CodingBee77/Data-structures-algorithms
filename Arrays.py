'''
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

# Answer 1,2,3
exp = [2200, 2350, 2600, 2130, 2190, 2000]
feb_extra_exp = exp[1] - exp[0]
quarter_exp = sum(exp[:3])
two_thousand_spent = [(exp.index(x) + 1) for x in exp if x == 2000]

print("In feb this much extra was spent compared to jan:{0}".format(feb_extra_exp))

print("Expense for first quarter:{0}".format(quarter_exp))

print("Did I spent 2000$ in any month? ", two_thousand_spent)

# Answer 4
exp.append(1980)
print("Expenses at the end of June:", exp)

# Answer 5
exp[3] -= 200
print("Expenses after 200$ return in April:", exp)

##################################

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

"""1. Length of the list"""
print("Length of the list: {0}".format(len(heros)))

"""2. Add 'black panther' at the end of this list"""

heros.append('black panther')

"""3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'"""

heros.pop(-1)
heros.insert(3, 'black panther')
print(heros)

"""4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code."""

heros[1:3] = ['doctor strange']
print(heros)

""" 5. Sort the list in alphabetical order"""
heros.sort()
print(heros)

#####################
"""Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function"""

max_num = int(input("Give me a max number: "))
list_odd = list(x for x in range(1, max_num) if not (x % 2 == 0))
print(list_odd)
