var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1,46)
let lottery = _.sampleSize(numbers, 6)
let pick = _.sample(list)

let menu = {
    짜장면: 'https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiXsaLsjPfhAhVAyosBHTqADCAQjRx6BAgBEAU&url=%2Furl%3Fsa%3Di%26source%3Dimages%26cd%3D%26ved%3D%26url%3Dhttp%253A%252F%252Fwww.10000recipe.com%252Frecipe%252F6852009%26psig%3DAOvVaw0ItNcOQSm02eDHsLKOdpC1%26ust%3D1556689072668197&psig=AOvVaw0ItNcOQSm02eDHsLKOdpC1&ust=1556689072668197',
    짬뽕:'https://t1.daumcdn.net/cfile/tistory/265BEF3F5614FAEB31',
    볶음밥:'http://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/58d359a9ac359adbc4c7fa2603f2e504.jpg',
}

console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)

let getMin = (a,b) => {
    if (a>b) {
        return b
    }
    return a
}

let getMinimunFromArray = (nums) => {
    let min = Infinity  //양의 무한대, sys.maxsize같은거네
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1,2,3,4,5]

console.log(getMinimunFromArray(ssafy))