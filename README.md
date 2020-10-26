# Programacion entera-mixta
<h1>Universidad Distrital Francisco Jose de Caldas</h1>
<h2>Integrantes:</h2>
<h3>Andres Felipe Wilches Torres -20172020114, Nicolas Andrade Perdomo - 20172020097 y Luis Alejandro Ocampo Gamboa - 20172020050</h3>

  <dt>
            <h3>Tabla de contenidos</h3>
        </dt>
        <dd>
            <ul>
                <li>Descripcion del proyecto</li>
                <li>Resumen</li>
                <li>Introduccion</li>
                <li>Objetivos</li>
                <li>Ejemplo de problema de PEM</li>
                <li>Bibliografia</li>
            </ul>
        </dd>
<ol>
    <li>
      <h4>Descripcion del proyecto</h4>
      <p>Algoritmo en python que soluciona problemas de programacion entera-mixta, con graficos mediante el uso de la libreria Matplotlib.</p>
    </li>
  <li>
<h4>Resumen</h4>
    <h4>¿Que es la programacion entera-mixta?</h4>
        <p align="justify">Para hablar de la programacion entera - mixta, primero se debe hablar de la programacion entera, a la cual pertenece. <br> 
           La programacion lineal entera es una tecnica que permite modelar y resolver problemas cuya caracterıstica principal
           es que el conjunto de soluciones factibles es discreto. A veces, algunas variables pueden ser enteras y otras continuas, en
           este caso hablamos de programacion lineal entera mixta. 
        </p>
<p>La programación entera mixta (PEM), es un caso de la programación entera donde algunas variables (por ejemplo, 1 de ellas) pueden no estar restringidas a valores enteros, por lo que es incorrecto usar el corte fraccional que se usaba en la rama de el algoritmo de la programación entera fraccional (entero puro).. Sin embargo puede emplearse un nuevo corte basado en la misma idea general, como se verá a continuación .
</p>
 </li>
<li><h4>Introduccion</h4></li>
  <p>En algunas situaciones que pueden representarse con modelos lineales nos encontramos con que sólo tienen sentido aquellas soluciones de la región factible que son enteras, así pueden representarse mediante modelos matemáticos ligeramente diferentes a los de programación lineal. Si todas las variables son enteras tenemos un problema de programación lineal entera, si sólo algunas deben serlo se trata de un problema de programación lineal mixta. Programación Entera es un término general para los modelos de programación matemática que presentan condiciones de integridad (condiciones que estipulan que algunas o todas las variables de decisión deben tener valores enteros).

Muchos problemas de decisión involucran no solo variables que pueden representarse por valores reales, sino decisiones de tipo discreto que están representadas de forma natural por variables enteras o binarias.
Estos problemas de optimización híbridos con variables reales y enteras se denominan de programación entera mixta. Es de modelo Lineal (vistas en P.L.) agregando que las variables de decisión deben ser enteras. Otras veces, el planteamiento del problema involucra, junto a los modelos cuantitativos, reglas o condiciones lógicas adicionales.
Estos problemas de optimización híbridos con variables reales y enteras se denominan de programación mixta entera  Si las decisiones son solo de tipo entero el problema se denomina de programación entera. 
</p>
<h4>Métodos de solución</h4>
<ul>
        <li>La aproximación de tratar las variables enteras como reales y luego aproximarse al entero más
            próximo suele dar resultados erróneos, excepto quizás cuando el número de valores posibles de una variable entera es alto. Rara vez con variables binarias</li>
        <li>
            Examen inteligente de alternativas enteras: Branch and Bound (B&B), siendo de los más efectivos para este tipos de problemas.</li>
</ul>
  
En este documento explicamos el funcionamiento de Branch and Bound (Ramificación y acotamiento) para la problemas de programación entera mixta

Generalmente los problemas de la PEM tienen la siguiente estructura:
