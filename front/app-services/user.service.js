(function () {
    'use strict';

    angular
        .module('app')
        .factory('UserService', UserService);

    UserService.$inject = ['$http'];

    function getConfig(method, endpoint, data) {
        return {
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            url: '/' + (endpoint || ''),
            method: method,
            data: data || '',
            headers: {
                'Content-Type': 'application/json'
            }
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
        service.GetMonedas = GetMonedas;
        service.GetOperacionesEnviadas = GetOperacionesEnviadas;
        service.GetOperacionesRecibidas = GetOperacionesRecibidas;
        service.CreateOperacion = CreateOperacion;

        return service;

        function GetAll() {
            return $http(getConfig('GET', 'usuarios/'));
        }

        function GetById(id) {
            return $http(getConfig('GET', 'usuarios/' + id));
        }

        function GetByUsername(username) {
            return $http(getConfig('GET', 'usuarios/' + username));
        }

        function Create(user) {
            return $http(getConfig('POST', 'usuarios/', JSON.stringify(user)));
        }

        function Update(user) {
            return $http(getConfig('PUT', 'usuarios/' + user.id, JSON.stringify(user)));
        }

        function Delete(id) {
            return $http(getConfig('DELETE', 'usuarios/' + id));
        }

        function GetMonedas(id) {
            return $http(getConfig('GET', 'monedas/'));
        }

        function GetOperacionesEnviadas(id) {
            return $http(getConfig('GET', 'operaciones/' + id + '/1'));
        }

        function GetOperacionesRecibidas(id) {
            return $http(getConfig('GET', 'operaciones/' + id + '/0'));
        }

        function CreateOperacion(id, data) {
            return $http(getConfig('POST', 'operaciones/' + id + '/1/', JSON.stringify(data)));
        }

    }

})();
