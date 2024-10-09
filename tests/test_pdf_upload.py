from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_pdf_success():
    pdf_file_path = r"C:\Users\batuh\Desktop\7apps_Case\tests\Yigit_Batuhan_Sener_CV_2024.pdf"

    with open(pdf_file_path, "rb") as pdf_file:
        response = client.post(
            "/v1/pdf",
            files= {"files" : ("Yigit_Batuhan_Sener_CV_2024.pdf", pdf_file, "application/pdf")}
        )
    assert response.status_code == 200
    assert "uploaded_pdfs" in response.json()

def test_upload_invalid_file():
    with open("tests/sample.txt", "rb") as invalid_file:
        response = client.post(
            "/v1/pdf",
            files= {"files": ("sample.txt", invalid_file, "tex/plain")}
        )
        assert response.status_code ==400
        assert response.json()["detail"] == "Invalid file type"