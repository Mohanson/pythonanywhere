'use strict';

var app = angular.module('app', ['ngRoute', 'ipCookie']);

// 常量
app.constant('global', {
    name: 'Pyseed',
});

app.config(function($httpProvider, $routeProvider, $locationProvider, $interpolateProvider) {

    $httpProvider.defaults.headers.post = {
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/', {
            templateUrl: '/static/html/root.html'
        })
        .when('/version', {
            templateUrl: '/static/html/version.html'
        })
        .when('/echo', {
            templateUrl: '/static/html/echo.html'
        })
        .otherwise({
            redirectTo: '/'
        });
});
