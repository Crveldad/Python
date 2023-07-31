<?php

$conn = new mysqli("192.xxx.xx.xxx", "nombreservidor", "contraseñaRdsfDFDfx", "nombre_bd", null, "/var/run/mysqld/mysqld.sock");

if (!$conn) {
    die("Conexión fallida: " . mysqli_connect_error());
}

$sql = "SELECT * FROM bbdd_random";

$result = mysqli_query($conn, $sql);
$res = [];

if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        $res[] = $row;
    }
    mysqli_free_result($result);
}

mysqli_close($conn);

//con reset

// $Conn = obtenerBD();
// $sql = "SELECT id FROM gf_pedidosproveedores_ventas WHERE id_pedido='$idPedido' AND tienda='$tienda'";
// $result = EjecutaQuery($Conn, $sql);
// $res = mysql_fetch_row($result);

// return reset($res);


$flog = fopen('logAlejandro.log', 'a');
fwrite($flog, print_r($sql, true));
fwrite($flog, PHP_EOL . str_repeat('*', 50) . PHP_EOL);
fclose($flog);
?>
<script>
    //IMPORTANTE DESACTIVAR FORM POR DEFECTO
    function mostrarInforme() {
        var empleado = document.getElementById('empleado').value;
        var tienda = document.getElementById('tienda').value;
        var dia = document.getElementById('dia').value;
        var mes = document.getElementById('mes').value;
        var ano = document.getElementById('ano').value

        var data = {
            usuario: <?= $_SESSION['id_usuario'] ?>,
            empleado: empleado,
            tienda: tienda,
            dia: dia,
            mes: mes,
            ano: ano,
            funcion: "comprobarInforme"
        };

        $.ajax({
            type: "POST",
            url: "interfaz.php",
            data: data,
            success: function (result) {
                var div = document.getElementById('mostrar');
                div.innerHTML = result;
            },
            error: function (error) {
                console.log("ERROR!");
                console.log(error);
            }
        });
    }
</script>