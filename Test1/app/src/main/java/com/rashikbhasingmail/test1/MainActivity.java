package com.rashikbhasingmail.test1;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ListView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends Activity {

    ListView list;
    LazyAdapter adapter;

    String strJson="{ \"Data\" :[{\"Desc\":\"This is 1st desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 2nd Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 3rd Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is also a desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 4th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 5th Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is 6th desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 7th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 8th Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is 9th desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 10th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 11th Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is 12th desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 13th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 15th Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is 16th desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 17th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 18th Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"},{\"Desc\":\"This is 19th desc and so on...So hello there\",\"name\":\"Sonoo Jaiswal\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg\"},{\"Desc\":\"this is 20th Description...whats up...how u doing\",\"name\":\"Vimal Jaiswal\",\"url\":\"https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg\"},{\"Desc\":\"this is 21st Description...random desc...\",\"name\":\"Rashik Bhasin\",\"url\":\"http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg\"}] }";

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    try {
        JSONObject jsonRootObject = new JSONObject(strJson);
        JSONArray jsonArray = jsonRootObject.optJSONArray("Data");


        list = (ListView) findViewById(R.id.listView1);
        // adapter=new LazyAdapter(this, imageUrls);

        adapter = new LazyAdapter(this, jsonArray);
        list.setAdapter(adapter);
    }
    catch(JSONException e) {e.printStackTrace();}
    }

    @Override
    public void onDestroy()
    {
        list.setAdapter(null);
        super.onDestroy();
    }

    private String imageUrls[] = {
            "http://static.vecteezy.com/system/resources/previews/000/084/251/original/christmas-bokeh-vector-background.jpg",
            "https://image.freepik.com/free-photo/lens-flare-abstract-backgound_21276999.jpg",
            "http://static.vecteezy.com/system/resources/previews/000/093/720/original/vector-abstract-style-background-illustration.jpg",
            "http://elektrodomek.pl/wp-content/uploads/2015/05/lights__vector_background_by_colorsark-d53prik.jpg"

    };
}

