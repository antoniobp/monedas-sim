(function () {
    'use strict';

    angular
        .module('app')
        .factory('UserService', UserService);

    UserService.$inject = ['$http'];

    /**
     * Obtiene la configuracion de la request
     */
    function getConfig(method, endpoint, data) {
        return {
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            url: '/' + (endpoint || ''),
            method: method,
            data: data || '',
            headers: {
                'Content-Type': 'application/json',
                'Data-Type': 'json',
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

        /**
         * Obtiene todos los usuarios
         */
        function GetAll() {
            return $http(getConfig('GET', 'usuarios/'));
        }

        /**
         * Obtiene un usuario segun el ID
         */
        function GetById(id) {
            return $http(getConfig('GET', 'usuarios/' + id));
        }

        /**
         * Obtiene un usuario segun el nombre
         */
        function GetByUsername(username) {
            return $http(getConfig('GET', 'usuarios/' + username));
        }

        /**
         * Crea un usuario
         */
        function Create(user) {
            var config = getConfig('POST', 'usuarios/', JSON.stringify(user));
            config.headers["Authorization"] = 'Token ' + window.btoa(user.username + ':' + user.password);

            return $http(config);
        }

        /**
         * Actualiza un usuario
         */
        function Update(user) {
            return $http(getConfig('PUT', 'usuarios/' + user.id, JSON.stringify(user)));
        }

        /**
         * Borra un usuario
         */
        function Delete(id) {
            return $http(getConfig('DELETE', 'usuarios/' + id));
        }

        /**
         * Obtiene todas las monedas
         */
        function GetMonedas(id) {
            return $http(getConfig('GET', 'monedas/'));
        }

        /**
         * Obtiene todas las operaciones realizadas por un usuario
         */
        function GetOperacionesEnviadas(id) {
            return $http(getConfig('GET', 'operaciones/' + id + '/1'));
        }

        /**
         * Obtiene todas las operaciones destinadas a un usuario
         */
        function GetOperacionesRecibidas(id) {
            return $http(getConfig('GET', 'operaciones/' + id + '/0'));
        }

        /**
         * Permite a un usuario crear una operacion
         */
        function CreateOperacion(id, data) {
            return $http(getConfig('POST', 'operaciones/' + id + '/1/', JSON.stringify(data)));
        }

    }

})();
