'use strict';

/* Directives */


angular.module('{{cookiecutter.project_name}}.directives', []).
  directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }]);
