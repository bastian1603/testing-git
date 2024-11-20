<?php 
    include 'koneksi.php';

    $judul_catatan = $_POST['catatan_judul'];
    $isi_catatan = $_POST['catatan_isi'];

    $input = mysqli_query($conn, "INSERT INTO catatan(judul_catatan, isi_catatan) values ('$judul_catatan', '$isi_catatan')");

    if($input) {
        echo "<script>
                    alert('Data Berhasil Disimpan');
                    window.location.href = 'dashboard.php';
            </script>";
    }else{
        echo "<script>
                    alert('Data Berhasil Disimpan');
                    window.location.href = 'dashboard.php';
            </script>";
    }

?>



