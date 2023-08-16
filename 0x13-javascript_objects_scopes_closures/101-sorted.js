#!/usr/bin/node
const data = require('./101-data');
const dic = data.dict;
const newDic = {};
for (const userId in dic) {
  const nb = dic[userId];
  if (!newDic[nb]) {
    newDic[nb] = [];
  }
  newDic[nb].push(userId);
}
console.log(newDic);
