import os

import pandas as pd
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# # Generate an encryption key
# key = Fernet.generate_key()
# print(key.decode())


class Encrypt:
    def __init__(self):
        """
        Initializes the Encrypt class by loading the environment variables,
        retrieving the encryption key, and initializing the Fernet cipher suite.
        """
        # Load the environment variables from .env
        load_dotenv()

        # Retrieve the encryption key from the .env file
        self.ENC_KEY = os.getenv("ENC_KEY")

        if self.ENC_KEY is None:
            raise ValueError("ENC_KEY is not set in .env file")

        # Initialize the Fernet cipher suite
        self.cipher_suite = Fernet(self.ENC_KEY.encode())

    def encrypt_file(self, file_path):
        """
        Encrypts the content of a CSV file.
        """
        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = self.cipher_suite.encrypt(file_data)

        # Write the encrypted data back to the file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        """
        Decrypts the content of a CSV file.
        """
        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        # Decrypt the file data
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)

        # Write the decrypted data back to the file
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

    def read_csv(self, file_path, *args, **kwargs):
        """
        Decrypts the file, reads the CSV content into a DataFrame, and re-encrypts the file.
        """
        # Decrypt the file
        self.decrypt_file(file_path)

        # Read the CSV file
        df = pd.read_csv(file_path, *args, **kwargs)

        # Re-encrypt the file after reading
        self.encrypt_file(file_path)

        return df

    def to_csv(self, df, file_path, *args, **kwargs):
        """
        Saves the DataFrame to a CSV file and encrypts the file afterward.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save DataFrame to CSV
        df.to_csv(file_path, *args, **kwargs)

        # Encrypt the file after saving
        self.encrypt_file(file_path)
