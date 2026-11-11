from similarity import cosine_similarity, find_most_similar

def test_same_direction_is_one():
    assert cosine_similarity([3, 4], [6, 8 ]) > 0.9999

def test_right_angle_is_zer0():
    assert cosine_similarity([2, 0], [0, 5]) == 0

def test_similar_is_higher_than_different():
    close = cosine_similarity([1, 2], [3, 4])
    far = cosine_similarity([1, 0], [0, 1])
    assert close > far

def test_find_most_similar_picks_closest():
    saved = {"password": [1, 0], "france": [0, 1],}
    key, score = find_most_similar([0.9, 0.1], saved)
    assert key == "password"
    assert score > 0.9

def test_find_most_similar_with_empty_cache():
    key, score  = find_most_similar([1, 0], {})
    assert key is None