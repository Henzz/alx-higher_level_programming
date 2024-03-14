#!/usr/bin/node
exports.callMeMoby = function (repeat, callback) {
  let i = 1;
  while (i <= repeat) {
    callback();
    i++;
  }
};
