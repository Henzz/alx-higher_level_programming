#!/usr/bin/node
exports.addMeMaybe = function (num, callback) {
  num += 1;
  callback(num);
};
