module.exports = {
    pages: {
        'index': {
            entry: './src/pages/home/main.js',
            template: 'public/index.html',
            filename: 'index.html',
            title: 'Home Page',
            chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
        },
        'about': {
            entry: './src/pages/about/main.js',
            template: 'public/index.html',
            filename: 'about.html',
            title: 'About Us',
            chunks: [ 'chunk-vendors', 'chunk-common', 'about' ]
        },
        'login': {
            entry: './src/pages/login/main.js',
            template: 'public/index.html',
            filename: 'login.html',
            title: 'Login',
            chunks: [ 'chunk-vendors', 'chunk-common', 'login' ]
        }
    }
}