(function () {
    'use strict';

    angular
        .module('app')
        .factory('UserService', UserService);

    UserService.$inject = ['$http'];

    function getAjaxConfig(method, endpoint, data) {
        return {
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            url: '/' + (endpoint || ''),
            method: method,
            data: data || ''
        };
    }

    function UserService($http) {
        var service = {};

        service.GetAll = GetAll;
        service.GetById = GetById;
        service.GetByUsername = GetByUsername;
        service.Create = Create;
        service.Update = Update;
        service.Delete = Delete;

        return service;

        function GetAll() {
            return $http.get('/usuarios').then(handleSuccess, handleError('Error getting all users'));
        }

        function GetById(id) {
            //return $http.get('/usuarios/' + id).then(handleSuccess, handleError('Error getting user by id'));
            return $.ajax(getAjaxConfig('GET', 'usuarios/' + id));
        }

        function GetByUsername(username) {
            //return $http.get('/usuarios/' + username).then(handleSuccess, handleError('Error getting user by username'));
            return $.ajax(getAjaxConfig('GET', 'usuarios/' + username));
        }

        function Create(user) {
            //return $http.post('/usuarios/', user).then(handleSuccess, handleError('Error creating user'));
            return $.ajax(getAjaxConfig('POST', 'usuarios/', JSON.stringify(user)));
        }

        function Update(user) {
            //return $http.put('/usuarios/' + user.id, user).then(handleSuccess, handleError('Error updating user'));
            return $.ajax(getAjaxConfig('PUT', 'usuarios/' + user.id, JSON.stringify(user)));
        }

        function Delete(id) {
            //return $http.delete('/usuarios/' + id).then(handleSuccess, handleError('Error deleting user'));
            return $.ajax(getAjaxConfig('DELETE', 'usuarios/' + id));
        }

        // private functions

        function handleSuccess(res) {
            return res.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }

})();
