
//배열 중복 객체로 표현
array.forEach((x) => { 
    array_result[x] = (array_result[x] || 0)+1; 
});

// 객체 값 가져오는법
for(const key in array){
   key : array[key]
console.log({})
}


// 배열 중복값 제거
function onlyUnique(value, index, self) {
return self.indexOf(value) === index;
}
var unique_report = report.filter(onlyUnique);

//배열 추가
array.push();

//배열 splice 추가
array.spice(1, 0, 'E');

//배열 자르기
array.split(' ');

//new Set()로 배열자르기
var unique_report = new Set(report);
console.log(unique_report);
var arr_unique_report = [];
unique_report.forEach((element) => {
    arr_unique_report.push(element);
})
console.log(arr_unique_report);


//indexOf
string.indexOf(".");

//substr
string.substr(0, string.length);

//includes
array.includes();

//replace
string.replace("abc", "");