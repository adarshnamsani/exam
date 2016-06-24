package com.rashikbhasingmail.test1;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

/**
 *
 * Created by rashik on 24/6/16.
 */
public class model {
    String name;
    String url;
    String des;
    int price;
    ArrayList<ArrayList<String>> urls;

    public model(String name, String url, int price, String des,ArrayList<String> arr){
            this.name = name;
            this.url = url;
            this.des = des;
            this.price = price;
            this.urls.add(arr);
    }

    public String getName() {
        return name;
    }

    public String getUrl() {
        return url;
    }

    public String getDes() {
        return des;
    }

    public int getPrice() {
        return price;
    }

    public ArrayList<ArrayList<String>> getUrls(){
        return urls;
    }
}
