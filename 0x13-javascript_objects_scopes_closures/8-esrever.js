#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  let first = 0;
  while ((last - first) > 0) {
    const rev = list[last];
    list[last] = list[first];
    list[first] = rev;
    first++;
    last--;
  }
  return list;
};
