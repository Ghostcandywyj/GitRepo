import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

import com.numericalmethod.suanshu.stats.timeseries.datastructure.univariate.realtime.inttime.SimpleTimeSeries;
import com.numericalmethod.suanshu.stats.timeseries.linear.univariate.arima.ARIMAForecastMultiStep;
import com.numericalmethod.suanshu.stats.timeseries.linear.univariate.arima.ARIMAModel;
import com.numericalmethod.suanshu.stats.timeseries.linear.univariate.stationaryprocess.arma.ConditionalSumOfSquares;


public class ArimaExample {
	public static void main(String[] args){
		try{
		//read time series from file to ArrayList
		BufferedReader br = new BufferedReader(new FileReader("arimademo.txt"));
		String line = null;
		ArrayList<Double> arr = new ArrayList<Double>();
		while((line = br.readLine()) != null){
			arr.add(Double.valueOf(line));
		}
		//get the last value
		double last = arr.get(arr.size()-1);
		//remove last value
		arr.remove(arr.size()-1);
		//new a double array
		double[] series = new double[arr.size()];
		for(int i = 0; i < arr.size(); i++){
			series[i] = arr.get(i);
		}
		//build ARIMA model and then forecast next value
		ConditionalSumOfSquares instance = new ConditionalSumOfSquares(series, 1, 1, 1);
		ARIMAModel arima = instance.getModel();
		ARIMAForecastMultiStep forecast = new ARIMAForecastMultiStep(new SimpleTimeSeries(series), arima, 1);
		System.out.println("prediction = "+forecast.xHat());
		System.out.println("error = "+forecast.var());
		System.out.println("real = "+last);
		br.close();
		}catch(Exception e){
		e.printStackTrace();
		}
	}
}