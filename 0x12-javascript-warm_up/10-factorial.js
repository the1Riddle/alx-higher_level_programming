#!/usr/bin/node
function fuct (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * fuct(n - 1));
}
console.log(fuct(Number(process.argv[2])));
