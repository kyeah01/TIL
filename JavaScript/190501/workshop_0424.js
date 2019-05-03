const axios = require('axios')

const url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts'

// // get 요청
// axios.get(url)
//     .then(response => {
//         console.log(response.data)
//     })

// post 요청
const data = {
    'post' : {
        'title' : 'mytitle',
        'content' : 'mycontent',
        'author' : 'yewon',
    }
}

const write = data => {
    axios.post(url, data)
        .then(response => {
            console.log(response.data)
        })
}

write(data)