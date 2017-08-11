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
        vm.user = null;

        initController();

        function initController() {

            UserService.GetAll()
                .then(function (response) {
                    console.log(response.data);
                    response.data.forEach(function(user) {
                        if (user.username != vm.currentUser.username) {
                            vm.users.push(user);
                        } else vm.user = user;
                    });
                })
                .catch(function (e) {
                    console.error(e);
                });
            
            UserService.GetMonedas()
                .then(function (response) {
                    vm.monedas = response.data;
                })
                .catch(function (e) {
                    console.error(e);
                });
        }

        function create() {
            vm.dataLoading = true;

            vm.operacion.remitente = $routeParams.id;
            vm.operacion.moneda = JSON.parse(vm.operacion.moneda.replace('\\/g', ""));
            if (vm.user.balance >= vm.operacion.importe * vm.operacion.moneda.valor_dolar) {
                vm.operacion.moneda = vm.operacion.moneda.id;
                UserService.CreateOperacion($routeParams.id, vm.operacion)
                    .then(function (response) {
                        FlashService.Success('Operacion creada', true);
                        $location.path('/');
                    })
                    .catch(function(response) {
                        FlashService.Error(response.data.message);
                        vm.dataLoading = false;
                    });
            } else {
                FlashService.Error("Fondos insuficientes para realizar la operación. \n" +
                    "Balance: " + parseFloat(vm.user.balance).toFixed(2) + " U$D. \n" +
                    "Importe operación: " + parseFloat(vm.operacion.importe).toFixed(2) + " " + vm.operacion.moneda.simbolo +
                    "\n Valor moneda: " + parseFloat(vm.operacion.moneda.valor_dolar).toFixed(2) + " U$D");
                vm.dataLoading = false;
            }
        }
    }

})();