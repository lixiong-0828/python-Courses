import zipfile

def extract_zip(destination,zipfile_name):
    with zipfile.ZipFile(zipfile_name,'r') as zip:
        zip.extractall(destination)

if __name__ == '__main__':
    extract_zip(
        r'C:\MyPython\PythonProject-02\zipFiles\compress',
        r'C:\MyPython\PythonProject-02\zipFiles\compress.zip'
    )