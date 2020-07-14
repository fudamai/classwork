const gulp = require('gulp');
const sass = require('gulp-sass');  
const concat = require('gulp-concat');  
const uglify = require('gulp-uglify');

gulp.task('html', function () {
    return gulp.src('src/**/*.html').pipe(gulp.dest('dist'));
});

gulp.task('data', function () {
    return gulp.src('src/data/**').pipe(gulp.dest('dist/data'));
});

sass.compiler = require('node-sass');

gulp.task('sass', function () {
    return gulp.src('src/**/*.scss')// 开发目录
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('dist'));// 产品目录
});

gulp.task('js', function () {
    return gulp.src('src/js/*.js')
    .pipe(concat('fubai.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('dist/js'))
});

exports.watch = function() {
    // ignoreInitial设置为false，调用watch时就执行任务
    gulp.watch('src/**/*.html', { ignoreInitial: false }, gulp.series('html'));
    gulp.watch('src/data/**', { ignoreInitial: false }, gulp.series('data'));
    gulp.watch('src/**/*.scss', { ignoreInitial: false }, gulp.series('sass'));
    gulp.watch('src/js/*.js', { ignoreInitial: false }, gulp.series('js'));
};
