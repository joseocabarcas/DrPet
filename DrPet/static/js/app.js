var miAplicacion = angular.module('drpet',['ngCookies']);

miAplicacion.config(function($httpProvider,$interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});



miAplicacion.controller('CtrlCitas', ['$scope', '$http', function($scope, $http){

	$scope.Medicos_Especialidad = function(){

		var datos= {
			especialidad:$scope.id_especialidad
		}
		console.log(datos)
		$http.post('cita/especialidad-medico',datos)
            .success(function(data){
            	console.log(data);
            })
            .error(function(data) {
            	console.log(data)
            })
	}

	$scope.$watch('id_especialidad',function (data) {
	     var datos= {
			especialidad:data
		}
	      console.log(datos)
		$http.post('cita/especialidad-medico',datos)
            .success(function(data){
            	$scope.Medicos=data.medicos;
            	console.log($scope.Medicos)
            })
            .error(function(data) {
            	//console.log(data)
            });
	  });


	//$scope.$watch($scope.Medicos_Especialidad)
	
	$scope.AgendaDisponible = function(){
		var my_url = 'cita/agenda-disp';
		var my_data = new Date($scope.id_fecha);
		var horariodia;
		switch(my_data.getDay()){
					
			case 1: horariodia='Lunes';break;
    		case 2: horariodia='Martes';break;
    		case 3: horariodia='Miercoles';break;
    		case 4: horariodia='Jueves';break;
    		case 5: horariodia='Viernes';break;
    		case 6: horariodia='Sabado';break;
    		case 0: horariodia='Domingo';break;
		}
		//console.log(horariodia)
		var datas= {
			fecha:horariodia
		}
		console.log(datas)



		  /*$http({
            method:'POST',
            url:'cita/agenda-disp',
            data:datas
            }).success(function(data){
                  console.log(data);
            })*/

            $http.post('cita/agenda-disp',datas)
            .success(function(data){
            	console.log(data);
            })
            .error(function(data) {
            	console.log(data)
            })


		  /*$http({
            method:'POST',
            url:'cita/agenda-disp',
            data:datas,
            headers:{'Content-Type': 'application/x-www-form-urlencoded'},
            }).success(function(data){
                  console.log(data);
            })*/
	}
}])