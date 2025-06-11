import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app.main import app

klien = app.test_client()

def test_beranda():
    respons = klien.get("/")
    assert respons.status_code == 200
    assert b"Kalkulator sederhana aktif" in respons.data

def test_tambah():
    respons = klien.get("/tambah?a=5&b=3")
    data = json.loads(respons.data)
    assert respons.status_code == 200
    assert data["hasil"] == 8.0

def test_kurang():
    respons = klien.get("/kurang?a=5&b=3")
    data = json.loads(respons.data)
    assert respons.status_code == 200
    assert data["hasil"] == 2.0

def test_kali():
    respons = klien.get("/kali?a=5&b=3")
    data = json.loads(respons.data)
    assert respons.status_code == 200
    assert data["hasil"] == 15.0

def test_bagi():
    respons = klien.get("/bagi?a=6&b=3")
    data = json.loads(respons.data)
    assert respons.status_code == 200
    assert data["hasil"] == 2.0

def test_bagi_nol():
    respons = klien.get("/bagi?a=6&b=0")
    assert respons.status_code == 400
    assert b"tidak diperbolehkan" in respons.data

def test_input_tidak_valid():
    respons = klien.get("/tambah?a=salah&b=2")
    assert respons.status_code == 400
    assert b"Input tidak valid" in respons.data
