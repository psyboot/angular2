var myApp = angular.module("myApp",["LocalStorageModule"] );
 

myApp.controller("saveController", function($scope,$http,localStorageService) {

    //$scope.model={"text1":"text1","text2":"text2","text3":"text3"};
    
    if(!localStorageService.get("boats")){
        //localStorageService.set("model1", $scope.model1);
        console.log("boats not exists");
        $http.get("data/data.json").success(function(data) {
        $scope.boats = data;
        //console.log(data);
        });        
        console.log(localStorageService.set("boats",$scope.data));        
    }
    
    $scope.boats= localStorageService.get("boats");

    $scope.Save = function (nboats) {        
        //localStorageService.set("boats",nboats);
        console.log("Nboats:" + nboats[0]["sea"]);
    }

    $scope.RemoveAll = function (nboats) {        
        localStorageService.clearAll();
    }

    //$scope.boats_jsonstring=JSON.stringify($scope.model);
    
});