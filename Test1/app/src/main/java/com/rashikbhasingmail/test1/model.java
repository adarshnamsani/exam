package com.rashikbhasingmail.test1;

import org.json.JSONException;
import org.json.JSONObject;

/**
 *
 * Created by rashik on 24/6/16.
 */
public class model {
    String name;
    String url;
    String des;
    int price;

    public model(String name, String url, int price, String des){
            this.name = name;
            this.url = url;
            this.des = des;
            this.price = price;
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
}
