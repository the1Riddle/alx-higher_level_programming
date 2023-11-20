#!/usr/bin/node
/* function that returns the reversed version of a list */
exports.esrever = function (list) {
  return list.map((_, idx, arr) => arr[arr.length - 1 - idx]);
};
