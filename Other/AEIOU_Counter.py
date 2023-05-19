var = input()

a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0

for i in (var):
    if i == 'a' or i == 'A':
        a_counter += 1
    elif i == 'e' or i == 'E':
        e_counter += 1
    elif i == 'i' or i == 'I':
        i_counter += 1
    elif i == 'o' or i == 'O':
        o_counter += 1
    elif i == 'u' or i == 'U':
        u_counter += 1

print(a_counter)
print(e_counter)
print(i_counter)
print(o_counter)
print(u_counter)
