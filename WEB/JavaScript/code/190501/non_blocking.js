// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)
// // 얘는 콜백스택으로 가서, 3초를 알아서 실행하고 온다.
// console.log('end program')

// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)


// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 0)
// third()

// func1() 을 호출했을때, 아래와같이 콘솔에 출력

// func1
// func3
// func2

let func2 = () => {
    console.log('func2')
}

let func3 = () => {
    console.log('func3')
}

func1 = () => {
    console.log('func1')
    setTimeout(func2, 0)
    func3()
}

func1()