package com.rashikbhasingmail.test1;

/**
 * Created by rashik on 24/6/16.
 */
import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class LazyAdapter extends BaseAdapter {

    private Activity activity;
    //private String[] data;

    JSONArray jsonArray;

    private static LayoutInflater inflater=null;
    public ImageLoader imageLoader;

    public LazyAdapter(Activity a,  JSONArray j) {
        activity = a;
        jsonArray=j;
        inflater = (LayoutInflater)activity.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        imageLoader=new ImageLoader(activity.getApplicationContext());
    }

    public int getCount() {
        return jsonArray.length();
    }

    public Object getItem(int position) {
        return position;
    }

    public long getItemId(int position) {
        return position;
    }

    public View getView(int position, View convertView, ViewGroup parent) {
        View vi=convertView;
        if(convertView==null)
            vi = inflater.inflate(R.layout.row_listview_item, null);

        TextView text=(TextView)vi.findViewById(R.id.text);

        TextView text1=(TextView)vi.findViewById(R.id.text1);

        ImageView image=(ImageView)vi.findViewById(R.id.image);
//        text.setText("item "+position);
//        imageLoader.DisplayImage(data[position], image);
        for(int i=0;i<jsonArray.length();i++)
        {
            try {
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                String name = jsonObject.optString("name").toString();
                String desc = jsonObject.optString("Desc").toString();
                text.setText(name);
                text1.setText(desc);

                imageLoader.DisplayImage(jsonObject.getString("url"), image);
            }
            catch(JSONException e) {e.printStackTrace();}
        }
        return vi;
    }
}
