import time
from lru import LRUCache

def test_get_returns_saved_value():
    c = LRUCache(2)
    c.put("A",1)
    assert c.get("A") == 1

def test_get_missing_key_return_none():
    c = LRUCache(2)
    assert c.get("X") is None

def test_evicts_least_recently_used():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    c.put("C", 3)
    assert c.get("A") is None
    assert c.get("B") == 2
    assert c.get("C") == 3

def test_get_makes_item_recently_used():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    c.get("A")
    c.put("C", 3)
    assert c.get("B") is None
    assert c.get("A") ==1

def test_put_existing_key_updates_value():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("A", 99)
    assert c.get("A") == 99
    assert len(c.map) == 1

def test_capacity_is_never_exceeded():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    c.put("C", 3)
    c.put("D", 4)
    c.put("E", 5)
    assert len(c.map) == 2

def test_capacity_one():
    c = LRUCache(1)
    c.put("A", 2)
    c.put("B", 1)
    assert c.get("A") is None

def test_update_make_item_recent():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    c.put("A", 99)
    c.put("C", 3) 
    assert c.get("B") is None

def test_miss_does_not_change_cache():
    c = LRUCache(1)
    c.put("A", 1)
    c.get("x")
    assert c.get("A") == 1

def test_many_operations():
    c = LRUCache(3)
    for i in range(10):
        c.put(f"k{i}", i)
    assert c.get("k9") == 9
    assert c.get("k0") is None

def test_answer_is_fresh_before_expiry():
    c = LRUCache(2)
    c.put("rate", "83.2", ttl=5)
    assert c.get("rate") == "83.2"

def test_answer_expires_after_ttl():
    c = LRUCache(2)
    c.put("rate", "83.2", ttl=1)
    time.sleep(2)
    assert c.get("rate") is None

def test_cleaner_removes_expired_entries():
    c = LRUCache(3)
    c.put("rate", "83.2", ttl=1)
    c.put("news", "x", ttl=30)
    time.sleep(2)
    c.put("faq", "y")
    assert "rate" not in c.map
    assert "news" in c.map
    assert len(c.map) == 2

def test_cleaner_skips_entry_already_evicted():
    c = LRUCache(1)
    c.put("A", 1, ttl=1)
    c.put("B", 2)
    time.sleep(2)
    c.put("C", 3)
    assert c.get("C") == 3
    assert "A" not in c.map