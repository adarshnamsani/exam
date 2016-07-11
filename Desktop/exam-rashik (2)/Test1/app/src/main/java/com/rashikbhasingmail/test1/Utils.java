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
            "https://www.smashingmagazine.com/images/nature-wallpapers/22.jpg",
            "https://www.zotks.si/sites/default/files/nature_040.jpg",
            "https://www.colourbox.com/preview/4188354-tropical-park-nature-background.jpg",
            "https://s-media-cache-ak0.pinimg.com/736x/d9/6e/f3/d96ef380f6788a2f159af96c23dd8261.jpg",
            "http://4.bp.blogspot.com/--5V3EawiHy0/UuNct6qpZ2I/AAAAAAAAEo0/mE1TPzzaZus/s1600/very+nice+natural+wallpaper.jpg",
            "http://www.100bestdesign.com/wp-content/uploads/2013/02/27-landscapes-nature_00416338.jpg",
            "https://dncache-mauganscorp.netdna-ssl.com/thumbseg/1950/1950777-bigthumbnail.jpg",
            "http://hdwallpaperbackgrounds.net/wp-content/uploads/2015/11/Morning-Nature-Desktop-Wallpapers.jpg",
            "http://webneel.com/wallpaper/sites/default/files/images/04-2013/mediterranean-beach-wallpaper.jpg",
           "http://all4desktop.com/data_images/original/4238677-nature-background.jpg"
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