(function () {
    'use strict';

    angular
        .module('app')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$route', '$location', 'AuthenticationService', 'FlashService'];
    function LoginController($route, $location, AuthenticationService, FlashService) {
        var vm = this;

        vm.login = login;

        (function initController() {
            AuthenticationService.ClearCredentials();
        })();

        /**
         * Loguea un usuario o si no es posible, utiliza el FlashService para notificar un error
         */
        function login() {
            vm.dataLoading = true;
            AuthenticationService.Login(vm.username, vm.password, function (response) {
                if (response.success) {
                    AuthenticationService.SetCredentials(vm.username, vm.password);
                    $location.path('/');
                    window.location.reload();
                } else {
                    FlashService.Error(response.message || response.data.detail);
                    vm.dataLoading = false;
                }
            });
        };
    }

})();
