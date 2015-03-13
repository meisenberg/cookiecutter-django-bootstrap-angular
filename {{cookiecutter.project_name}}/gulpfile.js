// Include gulp
var gulp = require('gulp');
var args   = require('yargs').argv;

// Include Our Plugins
var less = require('gulp-less');
var karma = require('gulp-karma');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var jshint = require('gulp-jshint');
var bg = require("gulp-bg");

var vendorJsFiles = [
  '{{cookiecutter.project_name}}/static/bower_components/jquery/dist/jquery.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/jquery.cookie/jquery.cookie.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular/angular.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-resource/angular-resource.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-route/angular-route.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-sanitize/angular-sanitize.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-cookies/angular-cookies.min.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-ui-router/release/angular-ui-router.min.js',
];

var appFiles = [
  '{{cookiecutter.project_name}}/static/js/app/**/*.js',
  '{{cookiecutter.project_name}}/static/js/app/controllers/**/*.js'
];

// Include files to test with karma
var testFiles = [
  '{{cookiecutter.project_name}}/static/bower_components/angular/angular.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-route/angular-route.js',
  '{{cookiecutter.project_name}}/static/bower_components/angular-mocks/angular-mocks.js',
  '{{cookiecutter.project_name}}/static/js/app/**/*.js',
  '{{cookiecutter.project_name}}/static/js/app/controllers/**/*.js',
  '{{cookiecutter.project_name}}/static/js/test/unit/**/*.js'
];

// Compile the Less files
gulp.task('less', function() {
    return gulp.src('{{cookiecutter.project_name}}/static/css/*.less')
        .pipe(less())
        .pipe(gulp.dest('{{cookiecutter.project_name}}/static/css'));
});

// Concatenate js vendo files
gulp.task('concatjs:vendor', function () {
  return gulp.src(vendorJsFiles)
    .pipe(concat('vendor.js'))
    .pipe(uglify())
    .pipe(gulp.dest('{{cookiecutter.project_name}}/static/js'));
});

// Concatenate js app files
gulp.task('concatjs:app', function () {
  return gulp.src(appFiles)
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter('default'))
    .pipe(concat('app.js'))
    .pipe(uglify())
    .pipe(gulp.dest('{{cookiecutter.project_name}}/static/js'));
});

// Unit testing with karma
gulp.task('karma', function() {
  // Be sure to return the stream
  return gulp.src(testFiles)
    .pipe(karma({
      configFile: '{{cookiecutter.project_name}}/static/js/test/karma.conf.js',
      action: 'run'
    }))
    .on('error', function(err) {
      // Make sure failed tests cause gulp to exit non-zero
      throw err;
    });
});

// Unit testing with karma and watching for changes
gulp.task('karma:watch', function () {
  return gulp.src(testFiles)
    .pipe(karma({
      configFile: 'karma.conf.js',
      action: 'watch'
    }))
    .on('error', function(e) {throw e;});
});

// Concatenations
gulp.task('concat', ['concatjs:app', 'concatjs:vendor']);

// Tests
gulp.task('test', ['karma']);

// Serve django project
gulp.task("server", bg("bin/django-serve"));

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('{{cookiecutter.project_name}}/static/css/*.less', ['less']);
    gulp.watch(testFiles, ['test']);
    gulp.watch(appFiles, ['concatjs:app']);
});

// Default Task
gulp.task('default', ['less', 'test', 'concat']);
