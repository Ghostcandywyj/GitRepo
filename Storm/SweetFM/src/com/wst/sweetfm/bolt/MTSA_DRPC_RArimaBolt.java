/**
 * MTSA_DRPC_AnalyzeSpout.java
 * 版权所有(C) 2014 
 * 创建:wwssttt 2014-03-08 22:13:00
 * 描述:接收DRPCServer传来的参数进行计算
 */
package com.wst.sweetfm.bolt;

import java.util.Map;

import org.rosuda.REngine.RList;
import org.rosuda.REngine.Rserve.RConnection;

import backtype.storm.task.ShellBolt;
import backtype.storm.topology.BasicOutputCollector;
import backtype.storm.topology.IRichBolt;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseBasicBolt;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Tuple;
import backtype.storm.tuple.Values;

public class MTSA_DRPC_RArimaBolt extends ShellBolt implements IRichBolt{	
	
	public MTSA_DRPC_RArimaBolt() {
	      super("Rscript", "arima.R");
	    }

    @Override
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	declarer.declare(new Fields("id", "result"));
	}
    
    @Override
    public Map<String, Object> getComponentConfiguration() {
    	return null;
    }
}