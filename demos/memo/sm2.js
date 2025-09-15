function sm2(item, grade) {
  if (grade < 0 || grade > 5) {
    throw new Error('Grade must be between 0 and 5');
  }

  let { repetition = 0, easiness = 2.5, interval = 1 } = item;

  if (grade >= 3) {
    if (repetition === 0) {
      interval = 1;
    } else if (repetition === 1) {
      interval = 6;
    } else {
      interval = Math.round(interval * easiness);
    }
    repetition += 1;
  } else {
    repetition = 0;
    interval = 1;
  }

  easiness = Math.max(1.3, easiness + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)));

  const nextDate = new Date();
  nextDate.setDate(nextDate.getDate() + interval);

  return {
    repetition,
    easiness: Math.round(easiness * 100) / 100,
    interval,
    nextDate
  };
}

module.exports = sm2;