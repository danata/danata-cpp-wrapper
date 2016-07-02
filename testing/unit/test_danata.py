"""Testing features of danata"""

def test_is_danata_available():
    """Test if Tree is available"""
    try:
        import danata
        assert True
    except:
        assert False
