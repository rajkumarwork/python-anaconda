import pysftp

CHUNK_SIZE = 500
file_number = 1

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None    # disable host key checking.
with pysftp.Connection('test.rebex.net', username='demo', password='password',cnopts=cnopts) as sftp:
    print(sftp.listdir('/'))
    remoteFilePath = '/readme.txt'
    localFilePath = './copiedreadme.txt'
    sftp.get(remoteFilePath, localFilePath)
    sftp.close()

#with open('innovators.csv') as f:
#    chunk = f.read(CHUNK_SIZE)
#    print(chunk)
#    while chunk:
#        with open('my_csv_' + str(file_number), 'w+') as chunk_file:
#            chunk_file.write(chunk)
#        file_number += 1
#        chunk = f.read(CHUNK_SIZE)