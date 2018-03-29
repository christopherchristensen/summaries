'use strict';

function arrayToUpperCase(array) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let isStringArray = true;
            if(array instanceof Array) {
                array.forEach((element) => {
                    if(element instanceof String) {
                        isStringArray = false;
                        console.log(array);
                    }
                });
                if(isStringArray) {
                    let upperCaseArray = [];
                    array.forEach((element) => {
                        upperCaseArray.push(element.toUpperCase());
                    });
                    console.log('Array is uppercase now: '+upperCaseArray);
                    resolve(upperCaseArray);
                } else {
                    reject(Error('Parameter contained elements other than type String'));
                }
            } else {
                reject(Error('Parameter was not an instance of Array'));
            }

        }, 2000);
    });
}

function sortArrayOfStrings(array) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if(array instanceof Array) {
                array = array.sort();
                console.log('Array is sorted now: '+array);
                resolve(array);
            } else {
                reject(Error('Parameter was not an instance of Array'));
            }
        }, 1000);
    });
}

function manipulateStringArrays(...args) {
    let arrays = [];
    args.forEach((element) => {
        arrays.push(element);
    });

    Promise.all(arrays)
        .then(arrayToUpperCase)
        .then(sortArrayOfStrings)
        .then(console.log('first, because not promise!'));
}

manipulateStringArrays("firstIndex", "secondIndex", "hi", "aloha");