const { read } = require('fs')
const http = require('http')

const server = http.createServer((req, res) => {

    if (req.url === '/'){
        res.end('<h1>Home Page </h1>')
    } else if (req.url === '/about'){
        res.end('<h1>About Page </h1>')
    } else {
        res.end('Page not found')
    }
    
})

server.listen(5000, 'localhost', () => {
    console.log('Server is listening at localhost on port 5000')
})