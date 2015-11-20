var miAplicacion = angular.module('drpet',['chart.js']);


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


miAplicacion.controller('CtrlMedicos',['$scope','$http',function($scope,$http){
$scope.error=false;
  $scope.Buscar_pacientes = function (){

    var datos = {
      identificacion:$scope.id_identificacion
    }

    $http.post('pacientes',datos)
    .then(function successCallback(response) {
      console.log(response.data)
      $scope.citas = response.data

    }, function errorCallback(response) {
      console.log(response)
      $scope.error=true;
    });

  }


}])



miAplicacion.controller('CtrlAuditorias',['$scope','$http',function($scope,$http){
$scope.labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    $scope.series = ['Citas Grabadas', 'Citas Canceladas'];
    $scope.legend = true;
    /*$scope.colours = [{fillColor: ["#5a72ff","#ffdb00","#219d55"],
     strokeColor: ["#5a72ff","#ffdb00","#219d55"],
     highlightFill: ["#5a72ff","#ffdb00","#219d55"],
     highlightStroke: ["#5a72ff","#ffdb00","#219d55"]}];*/

    $scope.data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ];


   

    $http({
      method: 'GET',
      url: '../reporte-ajax/'
    }).then(function successCallback(response) {

      console.log(response.data.auditorias[0])
      console.log(response.data.auditorias[1])

      var fechacancelada =response.data.auditorias[0].fecha;
      var fechapedida =response.data.auditorias[1].fecha;

      var cantidadcancelada =response.data.auditorias[0].total_operaciones;
      var cantidadpedida =response.data.auditorias[1].total_operaciones;

      $scope.data[0].splice(fechacancelada-1, 1,cantidadcancelada )

      $scope.data[1].splice(fechapedida-1, 1,cantidadpedida )
    /*
    var grabadas =response.grabadas;
    var consultadas =response.consultadas;

    angular.forEach(grabadas, function (grabada) {
      $scope.data[1].splice(grabada.mes-1, 1,grabada.cantidad )
                //Otra forma
                //$scope.datos[1][grabada.mes-1]=grabada.cantidad;
              });
    angular.forEach(consultadas, function (consultada) {
      $scope.data[0].splice(consultada.mes-1, 1,consultada.cantidad )
                //Otra forma
                //$scope.datos[0][consultada.mes-1]=consultada.cantidad;
              });
*/

  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
  });

   



}])



miAplicacion.controller('CtrlCitasMedcio', ['$scope', '$http', function($scope, $http){

$scope.err_not_found= false;


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

    console.info(data);

    if (!data.agenda[0]) {
      console.error("yo");
      $scope.err_not_found= true;
    }else{
       $scope.err_not_found= false;
    }
    $scope.total=[]

    $scope.agenda_id=data.agenda[0].id;
    console.log(data.agenda[0]);

    var inicio = moment(data.agenda[0].hora_ini,'HH:mm').format('HH:mm')
    var fin = moment(data.agenda[0].hora_fin,'HH:mm').format('HH:mm')
    //var frecuencia = moment(data.agenda[0].frecuencia,'mm').format('mm')
    var frecuencia =moment.duration(data.agenda[0].frecuencia, "minutes").format('HH:mm') ;
    //$scope.total=[];


if (frecuencia<60) {
  var comienzo=moment(inicio,'HH:mm').add(frecuencia,'m').format('HH:mm') ;
  console.error( comienzo )
}else{
  var comienzo=moment.duration(inicio,'HH:mm').add(frecuencia,'HH:mm').format('HH:mm') ;
  console.log( comienzo )
}
    


    console.info(inicio);
    console.info(fin);
    console.info( frecuencia);
    console.log( comienzo )



    $scope.total.push(inicio);

    while(comienzo<fin){
      $scope.total.push(comienzo);
      //comienzo=moment(comienzo,'HH:mm').add(frecuencia, 'minutes').format('HH:mm');
      //comienzo=moment(comienzo,'HH:mm').add(frecuencia,'HH:mm').format('HH:mm') ;

      if (frecuencia<60) {
        comienzo=moment(comienzo,'HH:mm').add(frecuencia,'m').format('HH:mm') ;
        console.error( comienzo )
      }else{
        comienzo=moment.duration(comienzo,'HH:mm').add(frecuencia,'HH:mm').format('HH:mm') ;
        console.log( comienzo )
      }
      console.log($scope.total);
    }


    var fecha= {
      fecha:moment(my_data).format('YYYY-MM-DD')
    }

    $scope.citas_hora=[]

    $http.post('../../citas-hora',fecha)
    .success(function(data){
      angular.forEach(data.citas_hora, function(dato) {
        $scope.citas_hora.push(moment(dato.hora_cita,'HH:mm').format('HH:mm'));
      });
      //console.info($scope.citas_hora)



      //console.info($scope.total.length);
      //console.info($scope.citas_hora.length);

      for( var i =$scope.total.length - 1; i>=0; i--){
        for( var j=0; j< $scope.citas_hora.length; j++){
          if($scope.total[i] == $scope.citas_hora[j]){
            $scope.total.splice(i, 1);
            //console.error($scope.total[i])
            //console.error($scope.citas_hora[j])
          }
          else{
            //console.error($scope.total[i])
            //console.error($scope.citas_hora[j])
          }
        }
      }

      console.log($scope.total);



    })
    .error(function(data) {
      console.log(data)
    })




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



