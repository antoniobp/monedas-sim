(function () {
    'use strict';

    angular
        .module('app')
        .controller('OperacionesController', OperacionesController);

    OperacionesController.$inject = ['UserService', '$routeParams', '$location', '$rootScope', 'FlashService'];
    function OperacionesController(UserService, $routeParams, $location, $rootScope, FlashService) {
        var vm = this;

        vm.create = create;
        vm.users = [];
        vm.monedas = [];
        vm.currentUser = $rootScope.globals.currentUser;

        initController();

        function initController() {

            UserService.GetAll()
                .then(function (data) {
                    vm.users = data.map(function(user) {
                        if (user.username != vm.currentUser.username) return user;
                    });
                    vm.users.splice(-1,1)
                })
                .catch(function (e) {
                    console.error(e);
                });
            
            UserService.GetMonedas()
                .then(function (data) {
                    vm.monedas = data;
                })
                .catch(function (e) {
                    console.error(e);
                });
        }

        function create() {
            vm.dataLoading = true;

            vm.remitente = $routeParams.id;

            UserService.CreateOperacion($routeParams.id)
                .then(function (response) {
                    FlashService.Success('Operacion creada', true);
                    $location.path('/');
                })
                .catch(function(response) {
                    console.log(response);
                    FlashService.Error(response.responseJSON.detail);
                    vm.dataLoading = false;
                });
        }
    }

})();