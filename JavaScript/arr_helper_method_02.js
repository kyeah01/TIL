// 4. reduce
/*
    - map은 배열의 각 요소를 변형한다면, reduce는 배열 자체를 변형시킨다.
    - 배열을 값 하나로 줄이는 동작을 한다.(ex, 배열의 합, 배열의 평균 ... 을 의미한다.)
    - reduce는 객체조절 성질도 가지고있다!
    - reduce의 첫번째 매개변수는 '누적값(전 단계의 결과)' 이다.
    - 두번째 매개변수는 현재 배열 요소 그 이후로는 현재 인덱스, 배열 자체순으로 인자를 받을 수 있다.
*/
// 4-1. 총합
const SSAFY = [3,9,2,7]
const sum = SSAFY.reduce((total, x) => total + x, 0) // 0이 초기의 total이 됨
console.log(sum)

// 4-2. 평균
const avg = SSAFY.reduce((total, x) => total + (x /SSAFY.length), 0)
console.log(avg)

// 4-3. 초기값 생략
// 초기값이 생략되면 누적값은 배열의 첫번째 요소가 초기값이 된다.
const sum_2 = SSAFY.reduce((total, x) => total + x)
console.log(sum_2)

// 5. find
/*
    - find는 찾은 요소 한가지만 리턴한다. (인덱스 x)
    - 배열 검색 헬퍼 : find, indexOf, lastIndexOf, some, every
*/

사용 예시
const USERS = [
    { name: 'Thor' },
    { name: 'Steve Rogers' },
    { name: 'Tony Stark' },
]

const ironMan = USERS.find(function(user) {
    return user.name === 'Tony Stark'
})

console.log(ironMan)

// 5-1 users 중에 admin 권한을 가진 요소를 찾아서 admin 에 저장하자.
const PEOPLE = [
    { id: 1, admin: false },
    { id: 2, admin: false },
    { id: 3, admin: true },
]

const admin = PEOPLE.find(person => person.admin)

console.log(admin)

// 5-2 accounts 중에서 잔액이 12 인 object 를 account 에 저장하자.
const ACCOUNTS = [
    { balance: -10 },
    { balance: 12 },
    { balance: 0 },
]

const account = ACCOUNTS.find(account => account.balance === 12)
console.log(account)


// 6. some & every
/*
    - 기존처럼 대상 배열에서 특정요소를 뽑거나, 배열을 return하지 않고 조건에 대해 boolean값을 리턴한다.
    - some : 조건에 맞는 요소를 찾으면 검색을 멈추고 true를 return하고, 끝까지 찾지 못하면 false를 리턴한다.
    - every : 해당 배열의 모든 요소가 조건에 맞아야 true를 리턴하고, 그렇지 않으면 false를 리턴한다.
              조건에 맞지 않는 요소가 있으면 검색을 멈추고 false를 리턴한다.
*/

const arr = [1,2,3,4,5]
console.log(
arr.some(x => x%2 === 0)
)

// 6-1. 컴퓨터의 램이 16보다 큰 요소가 있는지를 some과 every로 비교
const COMPUTERS = [
    { name: 'macbook', ram: 17 },
    { name: 'gram', ram: 8 },
    { name: 'series9', ram: 32 },
]

// const everyComputer = COMPUTERS.every(function (computer) {
//     return computer.ram > 16
// }
const everyComputer = COMPUTERS.every(computer => computer.ram > 16)
console.log(everyComputer)

const someComputer = COMPUTERS.some(computer => computer.ram > 16)
console.log(someComputer)


// 6-2 STUDENTS 배열에서 모두가 hasSubmitted 인지 아닌지를 hasSubmitted 에 저장하라
const STUDENTS = [
    { id: 21, hasSubmitted: true },
    { id: 33, hasSubmitted: false },
    { id: 712, hasSubmitted: true},
]

const hasSubmitted = STUDENTS.every(student => student.hasSubmitted)
console.log(hasSubmitted)

// 6-3 REQUESTS 배열에서 각 요청들 중 status 가 pending 인 요청이 있으면, inProgress 변수에 true 를 저장하라.
const REQUESTS = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]

const inProgress = REQUESTS.some(request => request.status === 'pending')
console.log(inProgress)