from mlproject.distance import haversine

def test_if_correct():
    assert haversine(48.865070, 2.393, 48.235, 2.380009) ==  70.01472400932725
