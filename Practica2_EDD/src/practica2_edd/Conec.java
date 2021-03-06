package practica2_edd;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Astrid Hernandez
 */
public class Conec {
     public static OkHttpClient webClient = new OkHttpClient();


public static String InsertarLista(String dato){
RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/insertarLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
           
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
public static String Buscar(String dato){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/buscarLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;  
}
public static String IngresarCola(int dato){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/insertarCola");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;  
}
public static String SacarCola(){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "")
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/saleCola");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;  
}
public static String IngresarPila(int dato){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/insertarPila");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;  
}
public static String eliminarLista(int dato){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/eliminarLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
           // System.out.println(request);
            Response response = webClient.newCall(request).execute();
           //System.out.println(response);
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
   
       return null;  
}
public static String SacarPila(){
  RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "")
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/salePila");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
}
public static String ingresarMatriz(String entrada){
  RequestBody formBody = new FormEncodingBuilder()
                .add("entrada", entrada)
                .add("fila", entrada)
                .add("columna",entrada)
                .add("orden1", entrada)
                .build();
try {
            URL url = new URL("http://0.0.0.0:5000/insertarMatriz");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            System.out.println(response_string);
            
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
}
}
