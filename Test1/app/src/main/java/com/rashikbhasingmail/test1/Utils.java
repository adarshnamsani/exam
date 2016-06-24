package com.rashikbhasingmail.test1;

/**
 *
 * Created by rashik on 24/6/16.
 */
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class Utils {

    static String imageUrls[] = {
            "http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg",
            "https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg",
            "http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg",
            "http://elektrodomek.pl/wp-content/uploads/2015/05/lights__vector_background_by_colorsark-d53prik.jpg",
            "http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg",
            "https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg",
            "http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg",
            "http://elektrodomek.pl/wp-content/uploads/2015/05/lights__vector_background_by_colorsark-d53prik.jpg", "http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg",
            "https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg"
    };

    static String names[] = {"Product1", "Product2", "Product3", "Product4","Product5", "Product6", "Product7", "Product8", "Product9", "Product10"};
    static int prices[] = {1001,2334,4552,2121,1234,4566,7890,1533,2435,8739};
  //  static String strJson="{{\"Desc\":\"This is 1st desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"This is 2nd desc and so on...So hello there\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"}}";

    public static void CopyStream(InputStream is, OutputStream os)
    {
        final int buffer_size=1024;
        try
        {
            byte[] bytes=new byte[buffer_size];
            for(;;)
            {
                int count=is.read(bytes, 0, buffer_size);
                if(count==-1)
                    break;
                os.write(bytes, 0, count);
            }
        }
        catch(Exception ex){}
    }

    public static List<model> createListData(){
        List<model> listData = new ArrayList<>();
        for(int i=0;i<10;i++) {
            int j=i+1;
            listData.add(new model(names[i],imageUrls[i], prices[i], "description "+j));
        }
        return listData;
    }
}