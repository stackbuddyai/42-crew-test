# Crew Estimation Tool

A Python function to estimate the number of crew members needed for moving jobs based on various factors.

## Overview

The `estimate_crew` function calculates the required crew size for moving operations by considering:
- Volume of items to be moved
- Number of bulky items
- Number of stair flights
- Whether it's a long-distance move

## Function Signature

```python
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
```

## Business Rules

The crew estimation follows these rules:

1. **Base crew**: Start with 2 crew members
2. **Volume factor**: If volume > 480 cubic feet, add 1 crew member
3. **Bulky items**: For every 2 bulky items, add 1 crew member
   - 0-1 bulky items = 0 additional crew
   - 2-3 bulky items = 1 additional crew
   - 4-5 bulky items = 2 additional crew
   - And so on...
4. **Stairs**: If there are 3 or more stair flights, add 1 crew member
5. **Long distance**: If it's a long-distance move, add 1 crew member

## Usage

```python
# Import the function
from estimate_crew import estimate_crew

# Example usage
crew_size = estimate_crew(550, 3, 2, False)
print(f"Required crew size: {crew_size}")  # Output: 4
```

## Test Results

### Primary Test Case
```
Input: estimate_crew(550, 3, 2, False)
Output: 4

Calculation breakdown:
- Base crew: 2
- Volume 550 > 480: +1 crew = 3
- 3 bulky items (3//2 = 1): +1 crew = 4
- 2 stair flights < 3: +0 crew = 4
- Long distance False: +0 crew = 4
- Final result: 4 crew members
```

### Additional Test Cases

| Volume | Bulky Items | Stair Flights | Long Distance | Expected | Actual | Status |
|--------|-------------|---------------|---------------|----------|--------|--------|
| 550    | 3           | 2             | False         | 4        | 4      | ✅     |
| 400    | 1           | 1             | False         | 2        | 2      | ✅     |
| 500    | 4           | 3             | True          | 7        | 7      | ✅     |
| 300    | 6           | 1             | False         | 5        | 5      | ✅     |
| 600    | 0           | 4             | True          | 5        | 5      | ✅     |
| 200    | 8           | 2             | False         | 6        | 6      | ✅     |

### Detailed Test Case Explanations

#### Test Case 1: estimate_crew(400, 1, 1, False) = 2
- Base crew: 2
- Volume 400 ≤ 480: +0 crew = 2
- 1 bulky item (1//2 = 0): +0 crew = 2
- 1 stair flight < 3: +0 crew = 2
- Long distance False: +0 crew = 2

#### Test Case 2: estimate_crew(500, 4, 3, True) = 7
- Base crew: 2
- Volume 500 > 480: +1 crew = 3
- 4 bulky items (4//2 = 2): +2 crew = 5
- 3 stair flights ≥ 3: +1 crew = 6
- Long distance True: +1 crew = 7

#### Test Case 3: estimate_crew(300, 6, 1, False) = 5
- Base crew: 2
- Volume 300 ≤ 480: +0 crew = 2
- 6 bulky items (6//2 = 3): +3 crew = 5
- 1 stair flight < 3: +0 crew = 5
- Long distance False: +0 crew = 5

## Running the Tests

To run the function and see all test results:

```bash
python estimate_crew.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## File Structure

```
42-crew-test/
├── estimate_crew.py    # Main function implementation
└── README.md          # This documentation
```
