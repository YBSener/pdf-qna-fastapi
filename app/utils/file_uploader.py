from fastapi import UploadFile

def save_uploaded_file(uploaded_file: UploadFile, destination: str):
    with open(destination, "wb") as file:
        file.write(uploaded_file.file.read())
