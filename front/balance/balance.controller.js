(function () {
    'use strict';

    angular
        .module('app')
        .controller('BalanceController', BalanceController);

    BalanceController.$inject = ['$location', 'UserService', 'FlashService', '$routeParams'];
    function BalanceController($location, UserService, FlashService, $routeParams) {
        var vm = this;

        vm.user = null;
        vm.monedas = [];

        initController();

        function initController() {

            UserService.GetById($routeParams.id)
                .then(function (user) {
                    vm.user = user.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                    $location.path('/');
                });

            UserService.GetMonedas()
                .then(function (response) {
                    vm.monedas = response.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                    $location.path('/');
                });
        }
    }

})();
