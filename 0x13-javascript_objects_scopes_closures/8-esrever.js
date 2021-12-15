#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length;
  let revlist = [];
  for (l; l > 0; l--) {
    revlist += list[l - 1];
    if (l > 1) revlist += ',';
  }
  return revlist.split(',');
};
