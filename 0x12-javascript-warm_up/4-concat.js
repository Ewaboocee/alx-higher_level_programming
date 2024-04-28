#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!arg1 && !arg2) {
  console.log('No arguments passed');
} else if (!arg2) {
  console.log(`${arg1} is undefined`);
} else if (!arg1) {
  console.log(`undefined is ${arg2}`);
} else {
  console.log(`${arg1} is ${arg2}`);
}
