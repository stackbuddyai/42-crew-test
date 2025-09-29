def estimate_crew(volume_cuft, bulky_count, stair_flights, long_distance):
    """
    Estimate the number of crew members needed for a moving job.
    
    Args:
        volume_cuft (int): Volume in cubic feet
        bulky_count (int): Number of bulky items
        stair_flights (int): Number of stair flights
        long_distance (bool): Whether it's a long distance move
    
    Returns:
        int: Final crew size
    """
    # Start with 2 crew
    crew_size = 2
    
    # If volume_cuft > 480, add 1 crew
    if volume_cuft > 480:
        crew_size += 1
    
    # For every 2 bulky items (0–1 = 0, 2–3 = 1, 4–5 = 2, …), add 1 crew
    crew_size += bulky_count // 2
    
    # If stair_flights >= 3, add 1 crew
    if stair_flights >= 3:
        crew_size += 1
    
    # If long_distance is True, add 1 crew
    if long_distance:
        crew_size += 1
    
    return crew_size


# Test the function with the provided input
if __name__ == "__main__":
    print("=== Crew Estimation Test Results ===\n")
    
    # Primary test case
    result = estimate_crew(550, 3, 2, False)
    print(f"Primary test case:")
    print(f"estimate_crew(550, 3, 2, False) = {result}")
    print(f"Expected: 4, Actual: {result}, Status: {'✅ PASS' if result == 4 else '❌ FAIL'}\n")
    
    # Additional test cases to verify the logic
    print("Additional test cases:")
    test_cases = [
        (400, 1, 1, False, 2, "Small volume, few items"),
        (500, 4, 3, True, 7, "Large volume, many bulky items, stairs, long distance"),
        (300, 6, 1, False, 5, "Many bulky items, no stairs"),
        (600, 0, 4, True, 5, "Large volume, no bulky items, stairs, long distance"),
        (200, 8, 2, False, 6, "Many bulky items, no stairs")
    ]
    
    for volume, bulky, stairs, long_dist, expected, description in test_cases:
        actual = estimate_crew(volume, bulky, stairs, long_dist)
        status = "✅ PASS" if actual == expected else "❌ FAIL"
        print(f"estimate_crew({volume}, {bulky}, {stairs}, {long_dist}) = {actual}")
        print(f"  Expected: {expected}, Actual: {actual}, Status: {status}")
        print(f"  Description: {description}\n")
