#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length;
  const revlist = [];
  for (l; l > 0; l--) {
    revlist.push(list.pop());
    // another form revlist.push(list[l - 1]);
  }
  return revlist;
};
