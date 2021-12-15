#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let iter = 0;
  let count = 0;

  for (iter; iter < list.length; iter++) {
    if (searchElement === list[iter]) {
      count++;
    }
  }
  return count;
};
