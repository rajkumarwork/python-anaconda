CHUNK_SIZE = 500
file_number = 1
with open('innovators.csv') as f:
    chunk = f.read(CHUNK_SIZE)
    print(chunk)
    while chunk:
        with open('my_csv_' + str(file_number), 'w+') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)