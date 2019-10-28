// var 함수스코프() - 함수 바깥으로 나가면 알아볼 수 없음
// let const 블록스코프{}


// let은 블록스코프
{
    let x = '정운지'
    console.log(x)          // 정운지
    {
        let x = 1
        console.log(x)      // 1
    }
    console.log(x)          // 정운지
}
console.log(typeof x)       // undefined

// var로 선언했을 경우, 정운지, 1, 1, number가 나옴.
// 이를 전역변수의 오염이라고 함.
// var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며,
// 심지어 선언하기도 전에 사용할 수 있다.
// let으로 선언하면, 선언하기 전에는 존재하지 않는다.
// 선언되지 않은 변수와, undefind 값을 가진 변수는 다르다.
// Uncaute ReferenceError |  

// JS가 알아들은 코드
var x
x
x = 1
x

if (x !== 1) {
    console.log(y)
    var y = 3
    if (y ===3) {
        var x = 1
    }
    console.log(y)
}
if (x === 1) {
    console.log(y)
}


// var로 변수를 선언하면, 자바스크립트는 같은 변수를 여러번 정의하더라도 무시한다.
var x = 1
if (x == 1) {
    var x = 2
    console.log(x)
}
console.log(x)

var x
x = 1
if (x == 1) {
    x = 2
    console.log(x)
}
console.log(x)


// 함수의 hoisting
ssafy()
function ssafy() {
    console.log('hoising!')
}

// 함수를 만약 변수에 할당하는 형식으로 정의하면, reference error가 뜬다.
// hoisting 되지 않는다!(var로 정의해도 마찬가지.)
let ssafy = funcion() {
    console.log('hoisting!')
}

