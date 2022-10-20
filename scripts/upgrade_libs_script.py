"""
This script will remove versions of libraries in requirements.txt and then install latest versions of libraries and
finally freeze latest versions again in requirements.txt
"""
req_file = open('../requirements.txt', 'rb')
updated_req_file = open('../updated_requirements.txt', 'w')
for library in req_file:
    lib = '{updated_lib}\n'.format(updated_lib=library.decode().split('==')[0])
    updated_req_file.write(lib)
req_file.close()
updated_req_file.close()
