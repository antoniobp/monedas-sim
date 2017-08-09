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
            var promise = UserService.Create(vm.user)
            promise.then(function (response) {
                FlashService.Success('Registration successful', true);
                $location.path('/login');
            });
            promise.fail(function(response) {
                console.log(response);
                FlashService.Error(response.responseJSON.detail);
                vm.dataLoading = false;
            });
        }
    }

})();
