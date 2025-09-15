# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/srs.spec.md
# (spec:47e4e2ce) (code:53023cac)

from datetime import date, timedelta
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
    # Validate grade
    if not (0 <= grade <= 5):
        raise ValueError("Grade must be between 0 and 5")
    
    # Get current values with defaults
    repetition = item.get('repetition', 0)
    easiness = item.get('easiness', 2.5)
    interval = item.get('interval', 1)
    
    # Handle incorrect responses (grades 0-2)
    if grade < 3:
        new_repetition = 0
        new_interval = 1
    else:
        # Handle correct responses (grades 3-5)
        new_repetition = repetition + 1
        
        if repetition == 0:
            new_interval = 1
        elif repetition == 1:
            new_interval = 6
        else:
            new_interval = round(interval * easiness)
    
    # Calculate new easiness factor
    new_easiness = max(1.3, easiness + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)))
    new_easiness = round(new_easiness, 2)
    
    # Calculate next review date
    next_date = date.today() + timedelta(days=new_interval)
    
    return {
        'repetition': new_repetition,
        'easiness': new_easiness,
        'interval': new_interval,
        'next_date': next_date
    }
