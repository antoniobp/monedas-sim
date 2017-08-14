(function () {
    'use strict';

    angular
        .module('app')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['UserService', '$location', '$rootScope', 'FlashService', '$routeParams'];
    function RegisterController(UserService, $location, $rootScope, FlashService, $routeParams) {
        var vm = this;

        vm.register = register;
        vm.id = $routeParams.id;

        if (vm.id) {
            initUser();
        }

        /**
         * Si la vista es de edicion, inicializa el usuario a editar
         */
        function initUser() {
            UserService.GetById(vm.id)
                .then(function (response) {
                    vm.user = response.data;
                })
                .catch(function (response) {
                    FlashService.Error(response.data.message || response.data.detail);
                    $location.path('/');
                });
        }

        /**
         * Crea un usuario o si es vista de edicion, llama a edit()
         */
        function register() {
            vm.dataLoading = true;

            if (!vm.id) {
                UserService.Create(vm.user)
                    .then(function (response) {
                        FlashService.Success('Registro exitoso', true);
                        $location.path('/login');
                    })
                    .catch(function(response) {
                        console.log(response);
                        FlashService.Error(response.data.message || response.data.detail);
                        vm.dataLoading = false;
                    });
            } else edit();
        }

        /**
         * Edita un usuario
         */
        function edit() {
            UserService.Update(vm.user)
                .then(function (response) {
                    FlashService.Success('Edición terminada', true);
                    $location.path('/');
                })
                .catch(function(response) {
                    console.log(response);
                    FlashService.Error(response.message || response.data.detail);
                    vm.dataLoading = false;
                });
        }
    }

})();
