import os.path
import zipfile
import pytest
from pypdf import PdfReader
import csv


@pytest.fixture
def create_test_files():
    current_dir = os.path.dirname(__file__)
    resources_dir = os.path.join(current_dir, 'resources')

    os.makedirs(resources_dir, exist_ok=True)

    pdf_file = os.path.join(resources_dir, "test_pdf.pdf")
    with open(pdf_file, 'wb') as f:
        f.write(b'PDF content here')

    xlsx_file = os.path.join(resources_dir, "test_xlsx.xlsx")
    with open(xlsx_file, 'wb') as f:
        f.write(b'XLSX content here')

    csv_file = os.path.join(resources_dir, "test_csv.csv")
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write('CSV content here')

    yield pdf_file, xlsx_file, csv_file


@pytest.fixture
def create_archive(create_test_files):
    current_dir = os.path.dirname(__file__)
    resources_dir = os.path.join(current_dir, 'resources')

    os.makedirs(resources_dir, exist_ok=True)

    pdf_file_path = os.path.join(resources_dir, 'test_pdf.pdf')
    xlsx_file_path = os.path.join(resources_dir, 'test_xlsx.xlsx')
    csv_file_path = os.path.join(resources_dir, 'test_csv.csv')

    archive_path = os.path.join(resources_dir, 'test_zip.zip')

    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(pdf_file_path, 'test_pdf.pdf')
        zipf.write(xlsx_file_path, 'test_xlsx.xlsx')
        zipf.write(csv_file_path, 'test_csv.csv')

    yield archive_path

    if os.path.exists(archive_path):
        os.remove(archive_path)


def test_read_pdf_from_archive(create_archive):
    with zipfile.ZipFile(create_archive, 'r') as zipf:
        content_pdf = zipf.read('test_pdf.pdf')
        assert content_pdf == b'PDF content here'


def test_read_xlsx_from_archive(create_archive):
    with zipfile.ZipFile(create_archive, 'r') as zipf:
        content_xlsx = zipf.read('test_xlsx.xlsx')
        assert content_xlsx == b'XLSX content here'


def test_read_csv_from_archive(create_archive):
    with zipfile.ZipFile(create_archive, 'r') as zipf:
        content_csv = zipf.read('test_csv.csv')
        assert content_csv == b'CSV content here'

