const path = require("path"); // 处理相关文件目录的操作
const ExtractTextPlugin = require("extract-text-webpack-plugin"); // 从bundle中提取文件用的插件

module.exports = {
    mode: "development",
    entry: "./src/js/memo.js", // 入口
    output: {
        // 出口
        filename: "index.js", // 输出的文件名
        path: path.resolve(__dirname, "dist"), // 输出路径
    },
    module: {
        // 定义规则处理scss文件
        rules: [{
            test: /\.scss$/,
            // 将样式嵌套到js中
            // 输出CSS时，需要使用提取插件。从JS中提取
            use: ExtractTextPlugin.extract({
                fallback:
                    // Creates `style` nodes from JS strings
                    "style-loader",
                use: [
                    // Translates CSS into CommonJS
                    "css-loader",
                    // Compiles Sass to CSS
                    "sass-loader",
                ],
            }),
        }]
    },
    externals: {
        jquery: 'jQuery'
    },
    plugins: [
        // 定义输出文件的名字
        new ExtractTextPlugin("style.css"),
    ],
};