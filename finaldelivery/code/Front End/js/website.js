'use strict';

var app = angular.module('website', ['ngRoute']);
app.config(['$routeProvider',
        function ($routeProvider) {
        $routeProvider.
            when('/dash', {templateUrl: 'dash.html', controller: 'dashCtrl'}).
            when('/chart', {templateUrl: 'chart.html', controller: 'chartCtrl'}).
            when('/bill', {templateUrl: 'bill.html', controller: 'billCtrl'}).
            when('/detail', {templateUrl: 'empty.html', controller: 'emptyCtrl'}).
            when('/login', {templateUrl: 'login.html', controller: 'loginCtrl'}).
            when('/android', {templateUrl: 'android.html', controller: 'androidCtrl'}).
            when('/cserver', {templateUrl: 'cserver.html', controller: 'cserverCtrl'}).

            otherwise({redirectTo: '/dash'});
    }
    ]);

app.controller('billCtrl', billCtrl);

function billCtrl($scope,StateService) {
//morris start
//    alert("alert box!");
    $scope.tle = "Total Cost";
    $scope.bodyy = 'This is the billing page';
    $scope.user = StateService.getUser();
    $scope.team = "All right reserved. Team: 17";
}

app.controller('emptyCtrl', emptyCtrl);

function emptyCtrl($scope,StateService) {
//morris start
//    alert("alert box!");
    $scope.tle = "Details";
    $scope.bodyy = 'Instance detailsh';
    $scope.user = StateService.getUser();
    $scope.team = "All right reserved. Team: 17";
}


app.controller('cserverCtrl', cserverCtrl);

function cserverCtrl($scope,StateService) {
//morris start
//    alert("alert box!");
    $scope.tle = "Server Instance";
    $scope.bodyy = 'Launch Server Instance';
    $scope.user = StateService.getUser();
    $scope.team = "All right reserved. Team: 17";
}


app.controller('androidCtrl', androidCtrl);

function androidCtrl($scope,StateService) {
//morris start
//    alert("alert box!");
    $scope.tle = "Mobile Instance";
    $scope.bodyy = 'Launch Mobile instance';
    $scope.user = StateService.getUser();
    $scope.team = "All right reserved. Team: 17";
}


app.controller('loginCtrl', loginCtrl);

function loginCtrl($scope,StateService) {
//morris start
//    alert("login alert box!");
    $scope.team = "All right reserved. Team: 17";
}

app.controller('chartCtrl', chartCtrl);

function chartCtrl($scope,StateService) {
//morris start
//    alert("hub alert box!");
    $scope.tle = "Hub";
    $scope.bodyy = 'Connect test server with Mobile devices';
    $scope.user = StateService.getUser();
    $scope.team = "All right reserved. Team: 17";
}

app.controller('dashCtrl', dashCtrl);

function dashCtrl($scope, StateService) {
//morris start
//    alert("dashboard alert box!");
    $scope.tle = "DashBoard";
    $scope.bodyy = 'We provide infrastructure for Mobile Testing';
    $scope.team = "All right reserved. Team: 17";
    $scope.user = StateService.getUser();

}

app.factory('StateService', function () {
    var user = 'Admin';
    var getUser = function () {
        return user;
    };
/*
    var setUser = function (m) {
        user = m;
    };
*/

    return {
        getUser: getUser
        //setUser: setUser
    }
})
