import pytest, os, sys

from somnus import read_data

def test_load_excel():
    test_path = "data/test_data/test_excel.xlsx"
    sheet_names, df = read_data.load_excel(test_path)

    assert sheet_names == ['sheet_1', 'sheet_2']

    expected = [1,'N3','N3','N3','N3','N3','N3']
    actual =  df['sheet_1'][1].values[2]

    for i,j in zip(expected, actual):
        assert i == j
