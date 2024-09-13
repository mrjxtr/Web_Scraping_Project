import os
from config import Encrypt

enc = Encrypt()

# * ------------------------------------------------------
# * DECRYPT YOUR FILE HERE
# * ------------------------------------------------------

script_dir = os.path.dirname(__file__)
file_path = os.path.join(
    script_dir, "../../data/processed/FILE_TO_DECRYPT.csv"
)  # path to the file you want to decrypt

enc.decrypt_file(file_path)
