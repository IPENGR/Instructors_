/**
 * Counts the number of odd integers in the inclusive range between low and high.
 *
 * @param {number} low - The lower bound of the range.
 * @param {number} high - The upper bound of the range.
 * @returns {number} - The count of odd integers in the range.
 * @throws {Error} - Throws an error for invalid inputs.
 */
function countOdds(low, high) {
  // Validate input
  if (!Number.isInteger(low) || !Number.isInteger(high) || low > high) {
    throw new Error(
      "Invalid input. Please provide valid integer values with low <= high."
    );
  }

  const oddNumbers = [];

  for (let num = low; num <= high; num++) {
    if (num % 2 === 1) {
      oddNumbers.push(num);
    }
  }
  console.log(oddNumbers);
  return oddNumbers.length;
}

// Example usage:
try {
  const result = countOdds(3, 7);
  console.log("Count of Odd Numbers:", result);
} catch (error) {
  console.error(error.message);
}
