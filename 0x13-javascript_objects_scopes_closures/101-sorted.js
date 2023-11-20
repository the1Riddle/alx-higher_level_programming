#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence
 */
const dict = require('./101-data').dict;

const newDict = {};

for (const [key, val] of Object.entries(dict)) {
  newDict[val] ? newDict[val].push(key) : (newDict[val] = [key]);
}
console.log(newDict);
