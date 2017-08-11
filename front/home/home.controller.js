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

        initController();

        function initController() {

            var promise = UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user.data;
                    loadOperacionesEnviadas(vm.user.id);
                    loadOperacionesEntrantes(vm.user.id);
                })
                .catch(function (e) {
                    console.error(e);
                });
        }

        function loadOperacionesEnviadas(id) {
            UserService.GetOperacionesEnviadas(id)
                .then(function (op) {
                    vm.operacionesEnviadas = op.data;
                })
                .catch(function (e) {
                    console.error(e);
                });
        }

        function loadOperacionesEntrantes(id) {
            UserService.GetOperacionesRecibidas(id)
                .then(function (op) {
                    vm.operacionesEntrantes = op.data;
                })
                .catch(function (e) {
                    console.error(e);
                });
        }

        function logout() {
            AuthenticationService.Logout();
        }

        function addNew() {
            $location.path('/user/' + vm.user.id + '/operaciones/new');
        }

    }

})();