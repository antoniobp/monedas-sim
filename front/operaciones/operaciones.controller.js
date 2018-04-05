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

        /**
         * Completa los datos iniciales para el controlador (usuarios y monedas)
         */
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
                    FlashService.Error(e.data.message || e.data.detail);
                });
            
            UserService.GetMonedas()
                .then(function (response) {
                    vm.monedas = response.data;
                })
                .catch(function (e) {
                    console.error(e);
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        /**
         * Crea una operacion para un usuario o si no es posible, utiliza el FlashService para notificar un error
         */
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
                        console.log(response);
                        FlashService.Error(response.data.message || response.data.detail);
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