def test_legal_age():
    assert legal_age(25) == "You can do anything"
    assert legal_age(21) == "You can do anything"
    assert legal_age(19) == "You can drive with parents' permission"
    assert legal_age(18) == "You can drive with parents' permission"
    assert legal_age(16) == "You'll have to wait"
    assert legal_age(8) == "You'll have to wait"
