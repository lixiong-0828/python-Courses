import zipfile
import pathlib
import time

def make_zip(files,destination,zipfile_name='zipfile' ):
    data = time.strftime('%Y%m%d %H-%M-%S')
    zipfile_name = f"{zipfile_name}_{data}.zip"
    dest_path = pathlib.Path(destination,zipfile_name)
    with zipfile.ZipFile(dest_path , 'w') as zip:
        for file in files:
            zip.write(file, arcname=pathlib.Path(file).name )

if __name__ == '__main__':
    make_zip(files=["../files/English.txt","../files/German.txt"],destination="../zipFiles",zipfile_name="myzip.zip")