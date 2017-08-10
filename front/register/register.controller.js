(function () {
    'use strict';

    angular
        .module('app')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['UserService', '$location', '$rootScope', 'FlashService'];
    function RegisterController(UserService, $location, $rootScope, FlashService) {
        var vm = this;

        vm.register = register;

        function register() {
            vm.dataLoading = true;
            UserService.Create(vm.user)
            .then(function (response) {
                FlashService.Success('Registro exitoso', true);
                $location.path('/login');
            })
            .catch(function(response) {
                console.log(response);
                FlashService.Error(response.responseJSON.detail);
                vm.dataLoading = false;
            });
        }
    }

})();
