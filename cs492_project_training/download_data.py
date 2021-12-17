import gdown
from zipfile import ZipFile

google_ = 'https://drive.google.com/uc?id='
zips = '1LVsKGJ8hlMn2cpUJfjDkhh450uNiGh45'
gdown.download(google_+zips, 'my_data.zip', quiet=False)

test_file_name = "my_data.zip"
with ZipFile(test_file_name, 'r') as zip:
    zip.printdir()
    zip.extractall('datasets') 
