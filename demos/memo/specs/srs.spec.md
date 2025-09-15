# Spaced Repetition System (SM2)

Implements the SM2 (SuperMemo 2) spaced repetition algorithm for calculating optimal review intervals for learning items.

## API

```python { .api }
from datetime import date
from typing import Dict, Any, Union

def sm2(item: Dict[str, Any], grade: int) -> Dict[str, Union[int, float, date]]:
    """
    Calculate SM2 spaced repetition values for a learning item.

    Args:
        item: Dictionary containing current SRS values with keys:
            - repetition (int, optional): Current repetition count, defaults to 0
            - easiness (float, optional): Current easiness factor, defaults to 2.5
            - interval (int, optional): Current interval in days, defaults to 1
        grade: Integer between 0-5 representing quality of response
            - 0-2: Incorrect response (resets progress)
            - 3-5: Correct response (advances progress)

    Returns:
        Dictionary with updated SRS values:
            - repetition (int): Updated repetition count
            - easiness (float): Updated easiness factor (rounded to 2 decimal places)
            - interval (int): Updated interval in days
            - next_date (date): Next review date

    Raises:
        ValueError: If grade is not between 0 and 5
    """
```

## Target

[@generate](../memo/srs.py)

## Capabilities

### Calculate SM2 algorithm updates

Takes an item with current SRS values and a grade, returns updated values according to SM2 algorithm.

- Validates grade is between 0 and 5 (inclusive)
- For grades 3-5 (correct responses): progresses repetition count and calculates new interval
- For grades 0-2 (incorrect responses): resets repetition to 0 and interval to 1
- Updates easiness factor based on grade performance
- Calculates next review date by adding interval days to current date

### Handle repetition progression

For successful reviews (grade >= 3):
- First repetition (repetition == 0): sets interval to 1 day
- Second repetition (repetition == 1): sets interval to 6 days
- Subsequent repetitions: interval = round(previous_interval * easiness_factor)
- Increments repetition count

### Calculate easiness factor

Updates easiness factor using SM2 formula: max(1.3, easiness + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)))
- Ensures minimum easiness of 1.3
- Rounds result to 2 decimal places

### Calculate next review date

Adds interval days to current date to determine when item should be reviewed next.
