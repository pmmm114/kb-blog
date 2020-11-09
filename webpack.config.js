const path = require('path');
const glob = require('glob');

const projectPath = '/kbblog';

module.exports = {
    entry: {
        profiles: ['@babel/polyfill'].concat(glob.sync('./kbblog/static/profiles/devjs/index.ts')),
        common: ['@babel/polyfill'].concat(glob.sync('./kbblog/static/common/devjs/index.ts')),
    },
    output: {
        filename: '[name]/js/[name].js',
        path: path.resolve(__dirname, projectPath + '/static'),
        publicPath: '/static',
    },
    module: {
        rules: [
            {
                enforce: 'pre',
                test: /\.tsx?$/,
                exclude: /node_modules/,
                use: {
                    loader: 'eslint-loader',
                    options: {
                        eslintPath: require.resolve('eslint'),
                        emitError: true,
                        emitWarning: true,
                        failOnError: true,
                        fix: true,
                    }, 
                },
            },
            {
                test: /\.tsx?$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            "@babel/preset-typescript",
                            "@babel/preset-env"
                        ],
                    },
                }
            }
        ]
    },
    devServer: {
        port: 9000,
        liveReload: true,
        publicPath: '/static',
        contentBase: path.resolve(__dirname, '/static'),
        contentBasePublicPath: '/static',
        watchContentBase: true,
        watchOptions: {
            poll: true
        },
        proxy: {
            '/': 'http://localhost:8000'
        }
    }
};