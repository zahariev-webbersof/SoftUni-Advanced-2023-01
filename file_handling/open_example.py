# class MessageWriter(object):
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def __enter__(self):
#         self.file = open(self.file_name, 'w')
#         return self.file
#
#     def __exit__(self, *args):
#         self.file.close()
#
#
# with MessageWriter('my_first_file.txt') as file:
#     file.write('I just created my first file!')

file_path = 'my_first_file.txt'
content = 'I just created my first file!'

with open(file_path, 'w') as file:
    file.write(contentpr)