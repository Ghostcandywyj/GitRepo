package com.wst.sweetfm.bolt;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Random;

import backtype.storm.coordination.BatchOutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseBatchBolt;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Tuple;
import backtype.storm.tuple.Values;

public class MTSA_DRPC_SeriesAnalyzeBatchBolt extends BaseBatchBolt{
	private BatchOutputCollector _collector;
    private HashMap<Integer,String> _topicOutput = new HashMap<Integer,String>();
    private Object _id;
	@Override
	public void prepare(Map conf, TopologyContext context,
			BatchOutputCollector collector, Object id) {
		// TODO Auto-generated method stub
		_collector = collector;
	}

	@Override
	public void execute(Tuple tuple) {
		// TODO Auto-generated method stub
		_id = tuple.getValue(0);
		String subSeq = tuple.getString(1);
	   	String[] items = subSeq.split("#");
	    Integer tid = Integer.valueOf(items[0]);
	    if(!_topicOutput.containsKey(tid)){
	    	String topicStr = items[1];
		   	String[] topicItems = topicStr.split(">");
		   	double[] topicProbability = new double[topicItems.length];
		   	for(int i = 0; i < topicItems.length; i++){
		   		topicProbability[i] = Double.valueOf(topicItems[i]);
		   	}	
		   	double nextProbability = exponentSmoothingSingle(topicProbability);
	   		String resultStr = tid+":"+nextProbability;
	   		//System.err.println(" origin = "+subSeq+" result = "+resultStr);
	   		_topicOutput.put(tid, resultStr);
	    }
	}

	@Override
	public void finishBatch() {
		// TODO Auto-generated method stub
		Iterator<Entry<Integer, String>> iter = _topicOutput.entrySet().iterator();
		while(iter.hasNext()){
			//Integer tid = iter.next().getKey();
			String resultStr = iter.next().getValue();
			_collector.emit(new Values(_id,resultStr));
		}
	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		// TODO Auto-generated method stub
		declarer.declare(new Fields("id","predicted_probability"));
	}

	private static double exponentSmoothingSingle(double[] series){
		int arrSize = series.length;
        double s[] = new double[arrSize];
        double sse = 0, mse = 2E16, alpha = 0;
        s[0] = 0;
        // ac - different values of alpha
        for(double ac=0;ac<=1;ac+=0.1)
        {
            s[1] = series[0];
            sse = 0;
            double temp = 0;
            for(int i =2;i<arrSize;i++)
            {
                s[i] = (ac * series[i-1]) + ((1-ac)*s[i-1]);
                sse += Math.pow(s[i] - series[i],2);
            }
            temp = sse/ arrSize;
            if(temp < mse)
            {
                mse = temp;
                alpha = ac;
            }
        }
        double next = alpha * series[arrSize-1] + (1 - alpha) * s[arrSize - 1];
        return next;
	}
}