# while True:
#     b = input('enter a word:')
#     if b == 'quit' or b == 'exit':
#         break
#     elif len(b) < 3:
#         print('too short')
#         continue
#     print('ok,now length of your input is over 3, your input is ', b)
# print('Done')


database=[('zhang3','123'),('li4','123'),('wang5','123')]
username=input('input your username:')
passwd=input('input your passwd:')

if username in database:
    print('right')
else:
    print('false')

