import unittest
from solution import TimeMap

class TestTimeMap(unittest.TestCase):
    def test_1_basic_example(self):
        # Example 1 from problem description
        tm = TimeMap()
        tm.set("alice", "happy", 1)
        self.assertEqual(tm.get("alice", 1), "happy")
        self.assertEqual(tm.get("alice", 2), "happy")
        tm.set("alice", "sad", 3)
        self.assertEqual(tm.get("alice", 3), "sad")

    def test_2_key_not_exist(self):
        # Get on an uninitialized key
        tm = TimeMap()
        self.assertEqual(tm.get("bob", 1), "")

    def test_3_timestamp_before_first(self):
        # Key exists but requested timestamp is before the first set
        tm = TimeMap()
        tm.set("foo", "bar", 5)
        self.assertEqual(tm.get("foo", 4), "")

    def test_4_multiple_keys(self):
        # Different keys should not interfere with each other
        tm = TimeMap()
        tm.set("k1", "v1", 1)
        tm.set("k2", "v2", 2)
        self.assertEqual(tm.get("k1", 3), "v1")
        self.assertEqual(tm.get("k2", 3), "v2")

    def test_5_exact_match(self):
        # Exact timestamp match on a single entry
        tm = TimeMap()
        tm.set("a", "b", 10)
        self.assertEqual(tm.get("a", 10), "b")

    def test_6_between_timestamps(self):
        # Requested timestamp falls strictly between two set timestamps
        tm = TimeMap()
        tm.set("a", "val1", 10)
        tm.set("a", "val2", 20)
        self.assertEqual(tm.get("a", 15), "val1")

    def test_7_large_timestamp(self):
        # Requesting with a massive timestamp returns the last value
        tm = TimeMap()
        tm.set("a", "val1", 10)
        self.assertEqual(tm.get("a", 10000000), "val1")

    def test_8_same_value_different_timestamps(self):
        # Setting the identical value at different increasing timestamps
        tm = TimeMap()
        tm.set("a", "val", 1)
        tm.set("a", "val", 2)
        self.assertEqual(tm.get("a", 1), "val")
        self.assertEqual(tm.get("a", 3), "val")

    def test_9_start_at_zero(self):
        # Edge case: timestamp starts at 0 (allowed by constraints)
        tm = TimeMap()
        tm.set("zero", "hero", 0)
        self.assertEqual(tm.get("zero", 0), "hero")
        self.assertEqual(tm.get("zero", 1), "hero")

    def test_10_large_number_of_sets(self):
        # Ensures binary search performs well and correctly retrieves values
        tm = TimeMap()
        for i in range(1, 1001):
            tm.set("loop", f"val{i}", i)
        self.assertEqual(tm.get("loop", 500), "val500")
        self.assertEqual(tm.get("loop", 1005), "val1000")

    def test_11_alternating_set_get(self):
        # Repeated set and get pattern
        tm = TimeMap()
        tm.set("k", "v1", 1)
        self.assertEqual(tm.get("k", 1), "v1")
        tm.set("k", "v2", 2)
        self.assertEqual(tm.get("k", 2), "v2")

    def test_12_single_letter_strings(self):
        # Minimum length constraint testing
        tm = TimeMap()
        tm.set("a", "b", 1)
        self.assertEqual(tm.get("a", 2), "b")

    def test_13_digits_in_strings(self):
        # Validating constraints for string characters (lowercase and digits)
        tm = TimeMap()
        tm.set("key123", "val456", 10)
        self.assertEqual(tm.get("key123", 10), "val456")

    def test_14_independent_keys_subsequent_time(self):
        # Two keys, checking timestamp queries after both are inserted
        tm = TimeMap()
        tm.set("k1", "v1", 10)
        tm.set("k2", "v2", 11)
        self.assertEqual(tm.get("k1", 11), "v1")
        self.assertEqual(tm.get("k2", 11), "v2")

    def test_15_get_before_any_set(self):
        # Call get before calling set at all
        tm = TimeMap()
        self.assertEqual(tm.get("k", 10), "")

if __name__ == '__main__':
    unittest.main()