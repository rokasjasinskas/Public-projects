from twttr import remove_vowels

def test_high():
    assert remove_vowels("TESTAS") == "TSTS"
def test_lower():
    assert remove_vowels("te") == "t"
def test_0():
    assert remove_vowels("0") == "0"
def test_empty():
    assert remove_vowels("") == ""
def test_both():
    assert remove_vowels("aaaaaaBBBBB DDDDD 12345") == "BBBBB DDDDD 12345"
def test_aeiouAEIOU():
    assert remove_vowels("aeiouAEIOU") == ""
