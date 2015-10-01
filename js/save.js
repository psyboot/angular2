var myApp = angular.module("myApp",["LocalStorageModule"] );
 

myApp.controller("saveController", function($scope,localStorageService) {

    $scope.model={"text1":"text1","text2":"text2","text3":"text3"};
    
    if(!localStorageService.get("model3")){
        //localStorageService.set("model1", $scope.model1);
        console.log("Model3 not exists");
        localStorageService.set("model3","test");
    }
    
    $scope.model2= localStorageService.get("model");
    $scope.model2_jsonstring=JSON.stringify($scope.model);
    console.log($scope.model2_jsonstring);
});