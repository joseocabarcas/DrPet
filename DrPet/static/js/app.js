var miAplicacion = angular.module('drpet',[]);


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
                $scope.Medicos={};
            });
	  });


	//$scope.$watch($scope.Medicos_Especialidad)
	
}])



miAplicacion.controller('CtrlCitasMedcio', ['$scope', '$http', function($scope, $http){

   
  
    $scope.$watch('id_fecha',function(data){
         var my_data = (data);
            var horariodia;
            switch(new Date(my_data).getDay()){
                        
                case 1: horariodia='Lunes';break;
                case 2: horariodia='Martes';break;
                case 3: horariodia='Miercoles';break;
                case 4: horariodia='Jueves';break;
                case 5: horariodia='Viernes';break;
                case 6: horariodia='Sabado';break;
                case 0: horariodia='Domingo';break;
                default:horariodia='';break;
            }

            var datas= {
                fecha:horariodia,
                medico_id:$scope.medico_id
            }
         
                $http.post('../../agenda-disp',datas)
                .success(function(data){



                  $scope.total=[]

                  $scope.agenda_id=data.agenda[0].id;
                    console.log(data.agenda[0]);
            
                    var inicio = moment(data.agenda[0].hora_ini,'HH:mm').format('HH:mm')
                    var fin = moment(data.agenda[0].hora_fin,'HH:mm').format('HH:mm')
                    var frecuencia = moment(data.agenda[0].frecuencia,'mm').format('mm')

                    
                    //$scope.total=[];
                    var comienzo=moment(inicio,'HH:mm').add(frecuencia, 'minutes').format('HH:mm');

                    console.log(comienzo);
                    console.log(fin);
                    
                  while(comienzo<=fin){
                    $scope.total.push(comienzo);
                    comienzo=moment(comienzo,'HH:mm').add(frecuencia, 'minutes').format('HH:mm');
                    console.log($scope.total);
                  }
                    
                    
                })
                .error(function(data) {
                    console.log(data)
                })

    });




}])




miAplicacion.controller('CtrlAgenda', ['$scope', '$http', function($scope, $http){
$scope.dato=[];//Simplemente un array que contiene las horas de inicio y fin



$scope.calculo = function () {
      //console.log($scope.dato.inicio);
      /*Variables que me ayudan a desfragmentar la hora
        t1 y t2 guardan los valores que se tienen
        dot1 y dot2 guarda el indice donde se encuentran los :
        m1 y m2 guardan los datos que se encuentran a la izq, es decir, la hora
        s1 y s2 guardan los datos que se encuentran a la der, es decir, los minutos
       */
      var t1 =$scope.dato.inicio;
      var t2 =$scope.dato.fin;
      var dot1 = t1.indexOf(":");
      var dot2 = t2.indexOf(":");
      var m1 = t1.substr(0, dot1);//M dan las horas
      var m2 = t2.substr(0, dot2);
      var s1 = t1.substr(dot1 + 1);
      var s2 = t2.substr(dot2 + 1);
      console.info(m1 + " " + m2);
      console.info(s1 + " " + s2);
      if (m1<m2) {
        console.log("Todo bn");
        $scope.validadorHoras = true;
      }else if(m1>m2){
        console.log("Todo mal");
        $scope.validadorHoras = false;
      }else {
        if (s1<s2) {
          console.log("Todo bn");
          $scope.validadorHoras = true;
        }else if(s1>s2){
          console.info("Todo mal");
          $scope.validadorHoras = false;
        }else{
          console.info("Todo mal no pueden ser iguales");
          $scope.validadorHoras = false;
        }
      }
    }

    //Objeto Watch que esta constantemente vigilando para saber si hay algun cambio en la 
    //funcion que se le pase
    $scope.$watch($scope.calculo);
    $scope.calcularHoras = function () {

              //hacemos uso de $http para obtener los datos del json
          $http.get('frecuenciaInicio.json')
          .success(function (data) {
              //Convert data to array.
              //datos lo tenemos disponible en la vista gracias a $scope
              $scope.datosInicio = data;
              console.log($scope.datosInicio);
          })
          .error(function(data) {
              console.log(data);
          });

          $http.get('frecuenciaFin.json')
          .success(function (data) {
              //Convert data to array.
              //datos lo tenemos disponible en la vista gracias a $scope
              $scope.datosFin = data;
              console.log($scope.datosFin);
          })
          .error(function(data) {
              console.log(data);
          });



              //hacemos uso de $http para obtener los datos del json
          $http.get('../../../frecuenciaInicio.json')
          .success(function (data) {
            $scope.dato.fin="";
            $scope.dato.inicio="";
              //Convert data to array.
              //datos lo tenemos disponible en la vista gracias a $scope
              $scope.datosInicio = data;
              console.log($scope.datosInicio);
          })
          .error(function(data) {
              console.log(data);
          });

          $http.get('../../../frecuenciaFin.json')
          .success(function (data) {
              //Convert data to array.
              //datos lo tenemos disponible en la vista gracias a $scope
              $scope.datosFin = data;
              console.log($scope.datosFin);
          })
          .error(function(data) {
              console.log(data);
          });
          
           
        } 
   
    
 




}])



 