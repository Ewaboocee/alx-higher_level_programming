#!/usr/bin/node

exports.esrever = function(list) {
    for (let i = 0; i < Math.floor(list.length / 2); i++) {
        // Swap elements at positions i and (list.length - i - 1)
        const temp = list[i];
        list[i] = list[list.length - i - 1];
        list[list.length - i - 1] = temp;
    }
    return list;
};
