app.controller('root', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $http.get('/api/v1/version').success(function(data, status, headers, config) {
        $scope.name = data.name;
        $scope.version = data.version;
        $scope.author = data.author;
        $scope.url = data.url;
    })
}]);

app.controller('version', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $http.get('/api/v1/version').success(function(data, status, headers, config) {
        $scope.name = data.name;
        $scope.version = data.version;
        $scope.author = data.author;
        $scope.url = data.url;
    })
}]);

app.controller('echo', ['$scope', '$http', 'ipCookie', function($scope, $http, ipCookie) {
    $scope.onRefresh = false
    $scope.getMessages = function getMessages() {
        if ($scope.onRefresh) {
            return
        }
        $scope.onRefresh = true
        $http.get('/api/v1/echo').success(function(data, status, headers, config) {
            if (data.err) {
                return
            }
            $scope.messages = data.messages;

            for (var i = 0; i < $scope.messages.length; i++) {
                if ($scope.messages[i]['content-type'] == 'application/json') {
                    $scope.messages[i]['body'] = JSON.stringify($scope.messages[i]['body'], null, 2)
                }
            }
            setTimeout(function() {
                $scope.$apply(function() {
                    $scope.onRefresh = false
                })
            }, 1000)
        })
    }

    setTimeout(function() {
        $scope.$apply($scope.getMessages);
    }, 10)

    $scope.autoRefreshSwitch = ipCookie('autoRefreshSwitch')
    ar = null
    $scope.$watch('autoRefreshSwitch', function() {
        if ($scope.autoRefreshSwitch) {
            ar = setInterval(function() {
                $scope.$apply($scope.getMessages);
            }, 10000);
        } else {
            clearInterval(ar)
        }
        ipCookie('autoRefreshSwitch', $scope.autoRefreshSwitch)
    });
}]);
