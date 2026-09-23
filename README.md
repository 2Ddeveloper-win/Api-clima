# Api-clima
Un proyecto simple de back-end que conecta con una Api de clima de terceros y guarda en caché la información obtenida

Cabe aclara que para la base de datos se utilizo redis, para el microframework se uso flask con la extensión de limit para limitar las peticiones a 6 por dia y por ultimo la api de clima de www.visualcrossing.com para obtener la información dada una respectiva ciudad

Cabe decir que los html son sencillos debido a que el punto principal del proyecto es
1.pedir el clima
2.chequer si esta en caché y si estar recuperarlo de cache y devolverlo
3.en caso de no estar en caché pedirle la información meteorológica a al servicio de www.visualcrossing.com
4. si se obtuvo la información de www.visualcrossing.com a través de API guardarla en cache   
