<?php 
try
{
  mysql_connect ('127.0.0.1', 'root', 'monMotDePasseMySQL');
  mysql_select_db('myBDD');
  echo 'Connexion réussi a la base de donnée<br>';
}
catch (Exception $e)
{
  die('Erreur : ' . $e->getMessage());
}
?>

<table width="400px">
  <thead>
    <tr>
      <td with="40%"> Heure</td>
      <td with="20%"> Hauteur</td>
      <td with="20%"> pH</td>
      <td with="20%"> Température</td>
    </tr>
  </thead>
  <tbody>

    <?php
    $result = mysql_query('SELECT * FROM Mesures ORDER BY Date DESC');
      while ($row = mysql_fetch_array($result, MYSQL_NUM)) 
      {
            echo "<tr><td>".$row[0]."</td><td>".$row[3]."</td><td>".$row[2]."</td><td>".$row[1]."</td></tr>";
      }
    ?>
  </tbody>
</table>