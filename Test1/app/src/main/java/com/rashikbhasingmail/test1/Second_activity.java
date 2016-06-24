package com.rashikbhasingmail.test1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;


import org.w3c.dom.Text;

import java.util.ArrayList;

public class Second_activity extends AppCompatActivity {

    public ImageLoader imageLoader;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second_activity);

//    ArrayList<model> a=(ArrayList<model>) getIntent().getSerializableExtra("mylist");
//
//        model data=a.get(0);

        Bundle bundle = getIntent().getExtras();
        String message = bundle.getString("mylist");
        RelativeLayout layout=(RelativeLayout)findViewById(R.id.content);
//
//       // imageLoader=new ImageLoader(this);
        String name="";
        String price="";
        String des="";
        String url="";

        String curr="";
        int j=1;
        for(int i=0;i<message.length();i++)
        {
            if(message.charAt(i)!=','){
                curr=curr+message.charAt(i);
            }
            else if(j==1)
            {
                name=curr;
                curr="";
                j=j+1;
            }
            else if(j==2)
            {
                price=curr;
                curr="";
                j++;
            }
            else if(j==3)
            {
                des=curr;
                curr="";
                j++;
            }
            else
            {
                url=curr;
            }
        }
//
//      ImageView image=(ImageView)findViewById(R.id.image1);
        TextView t1=(TextView)findViewById(R.id.text11);
        TextView t2=(TextView)findViewById(R.id.text22);
        TextView t3=(TextView)findViewById(R.id.text33);

//
        t1.setText(name);
        t2.setText(price);
        t3.setText(des);
//
//
//      //  RelativeLayout a=new RelativeLayout(this);
//        //imageLoader.DisplayImage(data.getUrl(), image);
////
//
//
//        TextView t=new TextView(this);
//        t.setText(name);
//
//        layout.addView(t);

//        layout.addView(t2);
//        layout.addView(t3);

    }


}
