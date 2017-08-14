(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['$location', 'UserService', 'AuthenticationService', '$rootScope'];
    function HomeController($location, UserService, AuthenticationService, $rootScope) {
        var vm = this;

        vm.user = null;
        vm.operacionesEnviadas = [];
        vm.operacionesEntrantes = [];
        vm.logout = logout;
        vm.addNew = addNew;
        vm.editUser = editUser;
        vm.balanceDetail = balanceDetail;

        initController();

        /**
         * Completa los datos iniciales para el controlador
         */
        function initController() {

            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user.data;
                    loadOperacionesEnviadas(vm.user.id);
                    loadOperacionesEntrantes(vm.user.id);
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        /**
         * Carga las operaciones que el usuario realizo
         */
        function loadOperacionesEnviadas(id) {
            UserService.GetOperacionesEnviadas(id)
                .then(function (op) {
                    vm.operacionesEnviadas = op.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        /**
         * Carga las operaciones que el usuario recibio
         */
        function loadOperacionesEntrantes(id) {
            UserService.GetOperacionesRecibidas(id)
                .then(function (op) {
                    vm.operacionesEntrantes = op.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        /**
         * Utiliza el metodo de AuthenticationService para cerrar sesion
         */
        function logout() {
            AuthenticationService.Logout();
        }

        /**
         * Redirige a la vista de agregar una nueva operacion
         */
        function addNew() {
            $location.path('/user/' + vm.user.id + '/operaciones/new');
        }

        /**
         * Redirige a la vista de editar los datos de usuario
         */
        function editUser() {
            $location.path('/user/' + vm.user.id);
        }

        /**
         * Redirige a la vista del detalle del balance del usuario
         */
        function balanceDetail() {
            $location.path('/user/' + vm.user.id + '/balance');
        }

    }

})();