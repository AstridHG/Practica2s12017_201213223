

package practica2_edd;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
/**
 *
 * @author Astrid Hernandez
 */
public class Practica2_EDD {
public static OkHttpClient webClient = new OkHttpClient();
   
/**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Inicio ini = new Inicio();
        ini.setVisible(true);
    }
}
