package storm.starter;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import org.apache.thrift7.TException;

import backtype.storm.generated.DRPCExecutionException;
import backtype.storm.utils.DRPCClient;

public class DRPCDemo {
	public static void main(String[] args) throws TException, DRPCExecutionException{
		long startTime = System.currentTimeMillis();
		DRPCClient client = new DRPCClient("127.0.0.1", 3772);
		String result = client.execute("sweetfm","21>22>23>24>25");
		System.err.println(result);
		long endTime = System.currentTimeMillis();
		System.err.println("Consumed:"+(endTime-startTime));
	}
}