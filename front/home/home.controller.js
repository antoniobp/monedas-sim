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

        function loadOperacionesEnviadas(id) {
            UserService.GetOperacionesEnviadas(id)
                .then(function (op) {
                    vm.operacionesEnviadas = op.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        function loadOperacionesEntrantes(id) {
            UserService.GetOperacionesRecibidas(id)
                .then(function (op) {
                    vm.operacionesEntrantes = op.data;
                })
                .catch(function (e) {
                    FlashService.Error(e.data.message || e.data.detail);
                });
        }

        function logout() {
            AuthenticationService.Logout();
        }

        function addNew() {
            $location.path('/user/' + vm.user.id + '/operaciones/new');
        }

        function editUser() {
            $location.path('/user/' + vm.user.id);
        }

        function balanceDetail() {
            $location.path('/user/' + vm.user.id + '/balance');
        }

    }

})();