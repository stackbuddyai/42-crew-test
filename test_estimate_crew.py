import pytest
from estimate_crew import estimate_crew


class TestEstimateCrew:
    """Test cases for the estimate_crew function."""
    
    def test_primary_case(self):
        """Test the primary case: estimate_crew(550, 3, 2, False) = 4"""
        result = estimate_crew(550, 3, 2, False)
        assert result == 4, f"Expected 4, got {result}"
    
    def test_base_crew(self):
        """Test base crew size of 2"""
        result = estimate_crew(100, 0, 0, False)
        assert result == 2, f"Expected 2, got {result}"
    
    def test_volume_threshold(self):
        """Test volume threshold at 480 cubic feet"""
        # Just under threshold
        result_under = estimate_crew(480, 0, 0, False)
        assert result_under == 2, f"Expected 2 for volume 480, got {result_under}"
        
        # Just over threshold
        result_over = estimate_crew(481, 0, 0, False)
        assert result_over == 3, f"Expected 3 for volume 481, got {result_over}"
    
    def test_bulky_items(self):
        """Test bulky items calculation"""
        test_cases = [
            (0, 0),  # 0-1 bulky items = 0 additional crew
            (1, 0),  # 0-1 bulky items = 0 additional crew
            (2, 1),  # 2-3 bulky items = 1 additional crew
            (3, 1),  # 2-3 bulky items = 1 additional crew
            (4, 2),  # 4-5 bulky items = 2 additional crew
            (5, 2),  # 4-5 bulky items = 2 additional crew
            (6, 3),  # 6-7 bulky items = 3 additional crew
            (8, 4),  # 8-9 bulky items = 4 additional crew
        ]
        
        for bulky_count, expected_additional in test_cases:
            result = estimate_crew(100, bulky_count, 0, False)
            expected_total = 2 + expected_additional
            assert result == expected_total, f"Expected {expected_total} for {bulky_count} bulky items, got {result}"
    
    def test_stair_flights(self):
        """Test stair flights threshold at 3"""
        # Under threshold
        result_under = estimate_crew(100, 0, 2, False)
        assert result_under == 2, f"Expected 2 for 2 stair flights, got {result_under}"
        
        # At threshold
        result_at = estimate_crew(100, 0, 3, False)
        assert result_at == 3, f"Expected 3 for 3 stair flights, got {result_at}"
        
        # Over threshold
        result_over = estimate_crew(100, 0, 5, False)
        assert result_over == 3, f"Expected 3 for 5 stair flights, got {result_over}"
    
    def test_long_distance(self):
        """Test long distance flag"""
        result_false = estimate_crew(100, 0, 0, False)
        assert result_false == 2, f"Expected 2 for short distance, got {result_false}"
        
        result_true = estimate_crew(100, 0, 0, True)
        assert result_true == 3, f"Expected 3 for long distance, got {result_true}"
    
    def test_combined_factors(self):
        """Test combinations of all factors"""
        test_cases = [
            # (volume, bulky, stairs, long_dist, expected, description)
            (400, 1, 1, False, 2, "Small volume, few items"),
            (500, 4, 3, True, 7, "Large volume, many bulky items, stairs, long distance"),
            (300, 6, 1, False, 5, "Many bulky items, no stairs"),
            (600, 0, 4, True, 5, "Large volume, no bulky items, stairs, long distance"),
            (200, 8, 2, False, 6, "Many bulky items, no stairs"),
            (1000, 10, 5, True, 10, "Maximum complexity case"),
        ]
        
        for volume, bulky, stairs, long_dist, expected, description in test_cases:
            result = estimate_crew(volume, bulky, stairs, long_dist)
            assert result == expected, f"Failed for {description}: expected {expected}, got {result}"
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Zero values
        result = estimate_crew(0, 0, 0, False)
        assert result == 2, f"Expected 2 for all zeros, got {result}"
        
        # Large values
        result = estimate_crew(10000, 100, 100, True)
        expected = 2 + 1 + 50 + 1 + 1  # base + volume + bulky + stairs + long_distance
        assert result == expected, f"Expected {expected} for large values, got {result}"
    
    def test_negative_values(self):
        """Test behavior with negative values"""
        result = estimate_crew(-100, -5, -2, False)
        # With negative bulky items (-5), we get -5//2 = -3, so 2 + (-3) = -1
        # This is expected behavior for negative inputs
        assert result == -1, f"Expected -1 for negative values, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
